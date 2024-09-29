
from PySide6 import QtWidgets
from mapclientplugins.meshrotationstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.StandardButton.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(
                self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        if valid:
            self._ui.lineEditIdentifier.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEditIdentifier.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {
            'datapoint-coordinates': self._ui.lineEditDatapointCoordinates.text(),
            'identifier': self._ui.lineEditIdentifier.text(),
            'mesh-coordinates': self._ui.lineEditMeshCoordinates.text(),
            'normal-from': [self._ui.doubleSpinBoxNormalFromX.value(), self._ui.doubleSpinBoxNormalFromY.value(), self._ui.doubleSpinBoxNormalFromZ.value()],
            'normal-to': [self._ui.doubleSpinBoxNormalToX.value(), self._ui.doubleSpinBoxNormalToY.value(), self._ui.doubleSpinBoxNormalToZ.value()],
        }
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.lineEditDatapointCoordinates.setText(config['datapoint-coordinates'])
        self._ui.lineEditMeshCoordinates.setText(config['mesh-coordinates'])
        self._ui.doubleSpinBoxNormalFromX.setValue(config['normal-from'][0])
        self._ui.doubleSpinBoxNormalFromY.setValue(config['normal-from'][1])
        self._ui.doubleSpinBoxNormalFromZ.setValue(config['normal-from'][2])
        self._ui.doubleSpinBoxNormalToX.setValue(config['normal-to'][0])
        self._ui.doubleSpinBoxNormalToY.setValue(config['normal-to'][1])
        self._ui.doubleSpinBoxNormalToZ.setValue(config['normal-to'][2])
