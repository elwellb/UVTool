# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_uiForm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(475, 413)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 441, 386))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.importFileLabel = QLabel(self.verticalLayoutWidget)
        self.importFileLabel.setObjectName(u"importFileLabel")

        self.horizontalLayout.addWidget(self.importFileLabel)

        self.importBrowse = QPushButton(self.verticalLayoutWidget)
        self.importBrowse.setObjectName(u"importBrowse")

        self.horizontalLayout.addWidget(self.importBrowse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.remeshCheck = QCheckBox(self.verticalLayoutWidget)
        self.remeshCheck.setObjectName(u"remeshCheck")

        self.verticalLayout.addWidget(self.remeshCheck)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.exportCheck = QCheckBox(self.verticalLayoutWidget)
        self.exportCheck.setObjectName(u"exportCheck")
        self.exportCheck.setEnabled(False)
        self.exportCheck.setChecked(True)

        self.verticalLayout.addWidget(self.exportCheck)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.exportLabel = QLabel(self.verticalLayoutWidget)
        self.exportLabel.setObjectName(u"exportLabel")
        self.exportLabel.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.exportLabel)

        self.exportBrowse = QPushButton(self.verticalLayoutWidget)
        self.exportBrowse.setObjectName(u"exportBrowse")
        self.exportBrowse.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.exportBrowse)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.openFileCheck = QCheckBox(self.verticalLayoutWidget)
        self.openFileCheck.setObjectName(u"openFileCheck")
        self.openFileCheck.setEnabled(False)

        self.verticalLayout.addWidget(self.openFileCheck)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.fixAssetPush = QPushButton(self.verticalLayoutWidget)
        self.fixAssetPush.setObjectName(u"fixAssetPush")
        self.fixAssetPush.setEnabled(False)

        self.verticalLayout.addWidget(self.fixAssetPush)

        self.uvShellCheck = QCheckBox(self.verticalLayoutWidget)
        self.uvShellCheck.setObjectName(u"uvShellCheck")
        self.uvShellCheck.setEnabled(False)

        self.verticalLayout.addWidget(self.uvShellCheck)

        self.clearButton = QPushButton(self.verticalLayoutWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setEnabled(False)

        self.verticalLayout.addWidget(self.clearButton)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.timeLabel = QLabel(self.verticalLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")

        self.verticalLayout.addWidget(self.timeLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Remesh and UV Tool", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Import", None))
        self.importFileLabel.setText(QCoreApplication.translate("Form", u"Empty", None))
        self.importBrowse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.remeshCheck.setText(QCoreApplication.translate("Form", u"Remesh? (Will increase cooking time SIGNIFICANTLY)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Export", None))
        self.exportCheck.setText(QCoreApplication.translate("Form", u"Export to Original Directory", None))
        self.exportLabel.setText(QCoreApplication.translate("Form", u"Empty", None))
        self.exportBrowse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.openFileCheck.setText(QCoreApplication.translate("Form", u"Open File Location when Complete", None))
        self.fixAssetPush.setText(QCoreApplication.translate("Form", u"Fix Asset", None))
        self.uvShellCheck.setText(QCoreApplication.translate("Form", u"Show UV Shells", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"Clear ALL Nodes", None))
        self.timeLabel.setText("")
    # retranslateUi

