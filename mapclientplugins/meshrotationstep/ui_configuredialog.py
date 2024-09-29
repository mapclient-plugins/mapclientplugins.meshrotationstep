# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 357)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelIdentifier)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.labelMeshCoordinates = QLabel(self.configGroupBox)
        self.labelMeshCoordinates.setObjectName(u"labelMeshCoordinates")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelMeshCoordinates)

        self.lineEditMeshCoordinates = QLineEdit(self.configGroupBox)
        self.lineEditMeshCoordinates.setObjectName(u"lineEditMeshCoordinates")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditMeshCoordinates)

        self.labelDatapointCoordinates = QLabel(self.configGroupBox)
        self.labelDatapointCoordinates.setObjectName(u"labelDatapointCoordinates")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDatapointCoordinates)

        self.lineEditDatapointCoordinates = QLineEdit(self.configGroupBox)
        self.lineEditDatapointCoordinates.setObjectName(u"lineEditDatapointCoordinates")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditDatapointCoordinates)

        self.labelNormalFrom = QLabel(self.configGroupBox)
        self.labelNormalFrom.setObjectName(u"labelNormalFrom")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelNormalFrom)

        self.labelNormalFromX = QLabel(self.configGroupBox)
        self.labelNormalFromX.setObjectName(u"labelNormalFromX")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelNormalFromX)

        self.doubleSpinBoxNormalFromX = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalFromX.setObjectName(u"doubleSpinBoxNormalFromX")
        self.doubleSpinBoxNormalFromX.setDecimals(4)
        self.doubleSpinBoxNormalFromX.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalFromX.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalFromX.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBoxNormalFromX)

        self.labelNormalFromY = QLabel(self.configGroupBox)
        self.labelNormalFromY.setObjectName(u"labelNormalFromY")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelNormalFromY)

        self.doubleSpinBoxNormalFromY = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalFromY.setObjectName(u"doubleSpinBoxNormalFromY")
        self.doubleSpinBoxNormalFromY.setDecimals(4)
        self.doubleSpinBoxNormalFromY.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalFromY.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalFromY.setSingleStep(0.100000000000000)
        self.doubleSpinBoxNormalFromY.setValue(1.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBoxNormalFromY)

        self.labelNormalFromZ = QLabel(self.configGroupBox)
        self.labelNormalFromZ.setObjectName(u"labelNormalFromZ")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelNormalFromZ)

        self.doubleSpinBoxNormalFromZ = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalFromZ.setObjectName(u"doubleSpinBoxNormalFromZ")
        self.doubleSpinBoxNormalFromZ.setDecimals(4)
        self.doubleSpinBoxNormalFromZ.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalFromZ.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalFromZ.setSingleStep(0.100000000000000)
        self.doubleSpinBoxNormalFromZ.setValue(0.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBoxNormalFromZ)

        self.labelNormalTo = QLabel(self.configGroupBox)
        self.labelNormalTo.setObjectName(u"labelNormalTo")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.labelNormalTo)

        self.labelNormalToX = QLabel(self.configGroupBox)
        self.labelNormalToX.setObjectName(u"labelNormalToX")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.labelNormalToX)

        self.doubleSpinBoxNormalToX = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalToX.setObjectName(u"doubleSpinBoxNormalToX")
        self.doubleSpinBoxNormalToX.setDecimals(4)
        self.doubleSpinBoxNormalToX.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalToX.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalToX.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBoxNormalToX)

        self.labelNormalToY = QLabel(self.configGroupBox)
        self.labelNormalToY.setObjectName(u"labelNormalToY")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.labelNormalToY)

        self.doubleSpinBoxNormalToY = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalToY.setObjectName(u"doubleSpinBoxNormalToY")
        self.doubleSpinBoxNormalToY.setDecimals(4)
        self.doubleSpinBoxNormalToY.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalToY.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalToY.setSingleStep(0.100000000000000)
        self.doubleSpinBoxNormalToY.setValue(0.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.doubleSpinBoxNormalToY)

        self.labelNormalToZ = QLabel(self.configGroupBox)
        self.labelNormalToZ.setObjectName(u"labelNormalToZ")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.labelNormalToZ)

        self.doubleSpinBoxNormalToZ = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxNormalToZ.setObjectName(u"doubleSpinBoxNormalToZ")
        self.doubleSpinBoxNormalToZ.setDecimals(4)
        self.doubleSpinBoxNormalToZ.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalToZ.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalToZ.setSingleStep(0.100000000000000)
        self.doubleSpinBoxNormalToZ.setValue(1.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.doubleSpinBoxNormalToZ)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Mesh Rotation", None))
        self.configGroupBox.setTitle("")
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
        self.labelMeshCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"Mesh coordinates:", None))
        self.lineEditMeshCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"coordinates", None))
        self.labelDatapointCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"Datapoint coordinates:", None))
        self.lineEditDatapointCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"coordinates", None))
        self.labelNormalFrom.setText(QCoreApplication.translate("ConfigureDialog", u"Normal from", None))
        self.labelNormalFromX.setText(QCoreApplication.translate("ConfigureDialog", u"x:", None))
        self.labelNormalFromY.setText(QCoreApplication.translate("ConfigureDialog", u"y:", None))
        self.labelNormalFromZ.setText(QCoreApplication.translate("ConfigureDialog", u"z:", None))
        self.labelNormalTo.setText(QCoreApplication.translate("ConfigureDialog", u"Normal to", None))
        self.labelNormalToX.setText(QCoreApplication.translate("ConfigureDialog", u"x:", None))
        self.labelNormalToY.setText(QCoreApplication.translate("ConfigureDialog", u"y:", None))
        self.labelNormalToZ.setText(QCoreApplication.translate("ConfigureDialog", u"z:", None))
    # retranslateUi

