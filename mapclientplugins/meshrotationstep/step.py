
"""
MAP Client Plugin Step
"""
import json
import os.path

from PySide6 import QtGui
from cmlibs.maths.vectorops import axis_angle_to_rotation_matrix, angle, cross
from cmlibs.utils.zinc.node import rotate_nodes
from cmlibs.zinc.context import Context

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.meshrotationstep.configuredialog import ConfigureDialog


class MeshRotationStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(MeshRotationStep, self).__init__('Mesh Rotation', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Fitting'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/meshrotationstep/images/fitting.png')
        # Ports:
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file')
                      ])
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file')
                      ])
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._portData1 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        # Config:
        self._config = {
            'datapoint-coordinates': 'coordinates',
            'identifier': '',
            'mesh-coordinates': 'coordinates',
            'normal-from': [0, 1, 0],
            'normal-to': [0, 0, 1],
        }

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        context = Context("rotate")
        region = context.createRegion()
        region.readFile(self._portData0)

        normal_from = self._config['normal-from']
        normal_to = self._config['normal-to']
        theta = angle(normal_to, normal_from)
        rot_mx = axis_angle_to_rotation_matrix(cross(normal_from, normal_to), theta)

        rotation_point = [0, 0, 0]

        rotate_nodes(region, rot_mx, rotation_point, self._config['mesh-coordinates'], self._config['datapoint-coordinates'])

        self._portData1 = self._define_output_location()
        region.writeFile(self._portData1)
        self._doneExecution()

    def _define_output_location(self):
        local_output_dir = os.path.join(self._location, self._config['identifier'] + "_output")
        if not os.path.exists(local_output_dir):
            os.makedirs(local_output_dir)

        return os.path.join(local_output_dir, "rotated.exf")

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        self._portData0 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        return self._portData1  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


