# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.4.1
#
import funktionen
import os
import os.path
import shutil
import time
import platform
import xml.dom.minidom
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.labelSourceIn = QtWidgets.QLabel(self.centralwidget)
        self.labelSourceIn.setObjectName("labelSourceIn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSourceIn)
        self.labelSourceOut = QtWidgets.QLabel(self.centralwidget)
        self.labelSourceOut.setObjectName("labelSourceOut")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSourceOut)
        self.labelTargetIn = QtWidgets.QLabel(self.centralwidget)
        self.labelTargetIn.setObjectName("labelTargetIn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTargetIn)
        self.labelTargetOut = QtWidgets.QLabel(self.centralwidget)
        self.labelTargetOut.setObjectName("labelTargetOut")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelTargetOut)
        self.labelIngestToolIn = QtWidgets.QLabel(self.centralwidget)
        self.labelIngestToolIn.setObjectName("labelIngestToolIn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelIngestToolIn)
        self.labelIngestToolOut = QtWidgets.QLabel(self.centralwidget)
        self.labelIngestToolOut.setObjectName("labelIngestToolOut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelIngestToolOut)
        # Settings tabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        ## Settings Packagetab
        self.Package = QtWidgets.QWidget()
        self.Package.setObjectName("Package")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Package)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelPackageId = QtWidgets.QLabel(self.Package)
        self.labelPackageId.setObjectName("labelPackageId")
        self.gridLayout_2.addWidget(self.labelPackageId, 0, 0, 1, 1)
        self.lineEditPackageID = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageID.setObjectName("lineEditPackageID")
        self.gridLayout_2.addWidget(self.lineEditPackageID, 0, 1, 1, 1)
        self.labelPackageName = QtWidgets.QLabel(self.Package)
        self.labelPackageName.setObjectName("labelPackageName")
        self.gridLayout_2.addWidget(self.labelPackageName, 0, 2, 1, 1)
        self.lineEditPackageName = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageName.setObjectName("lineEditPackageName")
        self.gridLayout_2.addWidget(self.lineEditPackageName, 0, 3, 1, 1)
        self.labelPackageVersion = QtWidgets.QLabel(self.Package)
        self.labelPackageVersion.setObjectName("labelPackageVersion")
        self.gridLayout_2.addWidget(self.labelPackageVersion, 1, 0, 1, 1)
        self.lineEditPackageVersion = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageVersion.setObjectName("lineEditPackageVersion")
        self.gridLayout_2.addWidget(self.lineEditPackageVersion, 1, 1, 1, 1)
        self.labelPackageDate = QtWidgets.QLabel(self.Package)
        self.labelPackageDate.setObjectName("labelPackageDate")
        self.gridLayout_2.addWidget(self.labelPackageDate, 1, 2, 1, 1)
        self.lineEditPackageDate = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageDate.setObjectName("lineEditPackageDate")
        self.gridLayout_2.addWidget(self.lineEditPackageDate, 1, 3, 1, 1)
        self.labelPackageClass = QtWidgets.QLabel(self.Package)
        self.labelPackageClass.setObjectName("labelPackageClass")
        self.gridLayout_2.addWidget(self.labelPackageClass, 2, 0, 1, 1)
        self.comboBoxPackageClass = QtWidgets.QComboBox(self.Package)
        self.comboBoxPackageClass.setObjectName("comboBoxPackageClass")
        self.comboBoxPackageClass.addItem("")
        self.comboBoxPackageClass.addItem("")
        self.comboBoxPackageClass.addItem("")
        self.comboBoxPackageClass.addItem("")
        self.comboBoxPackageClass.addItem("")
        self.comboBoxPackageClass.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxPackageClass, 2, 1, 1, 1)
        self.labelPackageEnviroment = QtWidgets.QLabel(self.Package)
        self.labelPackageEnviroment.setObjectName("labelPackageEnviroment")
        self.gridLayout_2.addWidget(self.labelPackageEnviroment, 2, 2, 1, 1)
        self.comboBoxPackageEnviroment = QtWidgets.QComboBox(self.Package)
        self.comboBoxPackageEnviroment.setObjectName("comboBoxPackageEnviroment")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.comboBoxPackageEnviroment.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxPackageEnviroment, 2, 3, 1, 1)
        self.labelPackageVolumeCount = QtWidgets.QLabel(self.Package)
        self.labelPackageVolumeCount.setObjectName("labelPackageVolumeCount")
        self.gridLayout_2.addWidget(self.labelPackageVolumeCount, 3, 0, 1, 1)
        self.lineEditPackageVolumeCount = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageVolumeCount.setObjectName("lineEditPackageVolumeCount")
        self.gridLayout_2.addWidget(self.lineEditPackageVolumeCount, 3, 1, 1, 1)
        self.labelPackageReserved = QtWidgets.QLabel(self.Package)
        self.labelPackageReserved.setObjectName("labelPackageReserved")
        self.gridLayout_2.addWidget(self.labelPackageReserved, 3, 2, 1, 1)
        self.lineEditPackageReserved = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageReserved.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditPackageReserved.setObjectName("lineEditPackageReserved")
        self.gridLayout_2.addWidget(self.lineEditPackageReserved, 3, 3, 1, 1)
        self.labelPackageDescription = QtWidgets.QLabel(self.Package)
        self.labelPackageDescription.setObjectName("labelPackageDescription")
        self.gridLayout_2.addWidget(self.labelPackageDescription, 4, 0, 1, 1)
        self.plainTextEditPackageDescription = QtWidgets.QPlainTextEdit(self.Package)
        self.plainTextEditPackageDescription.setObjectName("plainTextEditPackageDescription")
        self.gridLayout_2.addWidget(self.plainTextEditPackageDescription, 4, 1, 1, 3)
        self.labelPackageRemarks = QtWidgets.QLabel(self.Package)
        self.labelPackageRemarks.setObjectName("labelPackageRemarks")
        self.gridLayout_2.addWidget(self.labelPackageRemarks, 5, 0, 1, 1)
        self.plainTextEditPackageRemarks = QtWidgets.QPlainTextEdit(self.Package)
        self.plainTextEditPackageRemarks.setObjectName("plainTextEditPackageRemarks")
        self.gridLayout_2.addWidget(self.plainTextEditPackageRemarks, 5, 1, 1, 3)
        self.labelPackageIngestDate = QtWidgets.QLabel(self.Package)
        self.labelPackageIngestDate.setObjectName("labelPackageIngestDate")
        self.gridLayout_2.addWidget(self.labelPackageIngestDate, 6, 0, 1, 1)
        self.dateEditPackageIngestDate = QtWidgets.QDateEdit(self.Package)
        self.dateEditPackageIngestDate.setObjectName("dateEditPackageIngestDate")
        self.gridLayout_2.addWidget(self.dateEditPackageIngestDate, 6, 1, 1, 1)
        self.labelPackageArchivist = QtWidgets.QLabel(self.Package)
        self.labelPackageArchivist.setObjectName("labelPackageArchivist")
        self.gridLayout_2.addWidget(self.labelPackageArchivist, 6, 2, 1, 1)
        self.lineEditPackageArchivist = QtWidgets.QLineEdit(self.Package)
        self.lineEditPackageArchivist.setObjectName("lineEditPackageArchivist")
        self.gridLayout_2.addWidget(self.lineEditPackageArchivist, 6, 3, 1, 1)
        self.tabWidget.addTab(self.Package, "")
        ## Settings Volumetab
        self.Volume = QtWidgets.QWidget()
        self.Volume.setObjectName("Volume")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Volume)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelVolumeId = QtWidgets.QLabel(self.Volume)
        self.labelVolumeId.setObjectName("labelVolumeId")
        self.gridLayout_3.addWidget(self.labelVolumeId, 0, 0, 1, 1)
        self.lineEditVolumeId = QtWidgets.QLineEdit(self.Volume)
        self.lineEditVolumeId.setObjectName("lineEditVolumeId")
        self.gridLayout_3.addWidget(self.lineEditVolumeId, 0, 1, 1, 1)
        self.labelVolumeName = QtWidgets.QLabel(self.Volume)
        self.labelVolumeName.setObjectName("labelVolumeName")
        self.gridLayout_3.addWidget(self.labelVolumeName, 0, 3, 1, 1)
        self.lineEditVolumeName = QtWidgets.QLineEdit(self.Volume)
        self.lineEditVolumeName.setObjectName("lineEditVolumeName")
        self.gridLayout_3.addWidget(self.lineEditVolumeName, 0, 4, 1, 1)
        self.labelVolumeMedium = QtWidgets.QLabel(self.Volume)
        self.labelVolumeMedium.setObjectName("labelVolumeMedium")
        self.gridLayout_3.addWidget(self.labelVolumeMedium, 1, 0, 1, 1)
        self.comboBoxVolumeMedium = QtWidgets.QComboBox(self.Volume)
        self.comboBoxVolumeMedium.setObjectName("comboBoxVolumeMedium")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.comboBoxVolumeMedium.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxVolumeMedium, 1, 1, 1, 1)
        # Button Autodetect       
        self.pushButtonVolumeMedium = QtWidgets.QPushButton(self.Volume)
        self.pushButtonVolumeMedium.setObjectName("pushButtonVolumeMedium")
        self.pushButtonVolumeMedium.clicked.connect(self.VolumeAutodetect)
        self.gridLayout_3.addWidget(self.pushButtonVolumeMedium, 1, 2, 1, 1)

        self.labelVolumeLabel = QtWidgets.QLabel(self.Volume)
        self.labelVolumeLabel.setObjectName("labelVolumeLabel")
        self.gridLayout_3.addWidget(self.labelVolumeLabel, 1, 3, 1, 1)
        self.lineEditVolumeLabel = QtWidgets.QLineEdit(self.Volume)
        self.lineEditVolumeLabel.setObjectName("lineEditVolumeLabel")
        self.gridLayout_3.addWidget(self.lineEditVolumeLabel, 1, 4, 1, 1)
        self.labelVolumeDescription = QtWidgets.QLabel(self.Volume)
        self.labelVolumeDescription.setObjectName("labelVolumeDescription")
        self.gridLayout_3.addWidget(self.labelVolumeDescription, 2, 0, 1, 1)
        self.plainTextEditVolumeDescription = QtWidgets.QPlainTextEdit(self.Volume)
        self.plainTextEditVolumeDescription.setObjectName("plainTextEditVolumeDescription")
        self.gridLayout_3.addWidget(self.plainTextEditVolumeDescription, 2, 1, 1, 4)
        self.labelVolumeRemarks = QtWidgets.QLabel(self.Volume)
        self.labelVolumeRemarks.setObjectName("labelVolumeRemarks")
        self.gridLayout_3.addWidget(self.labelVolumeRemarks, 3, 0, 1, 1)
        self.plainTextEditVolumeRemarks = QtWidgets.QPlainTextEdit(self.Volume)
        self.plainTextEditVolumeRemarks.setObjectName("plainTextEditVolumeRemarks")
        self.gridLayout_3.addWidget(self.plainTextEditVolumeRemarks, 3, 1, 1, 4)
        self.tabWidget.addTab(self.Volume, "")
        ## Settings Viewtab
        self.View = QtWidgets.QWidget()
        self.View.setObjectName("View")
        self.gridLayout = QtWidgets.QGridLayout(self.View)
        self.gridLayout.setObjectName("gridLayout")
        self.labelViewMetadata = QtWidgets.QLabel(self.View)
        self.labelViewMetadata.setObjectName("labelViewMetadata")
        self.gridLayout.addWidget(self.labelViewMetadata, 0, 0, 1, 1)
        ### Button Metadata
        self.pushButtonUpdateMetadata = QtWidgets.QPushButton(self.View)
        self.pushButtonUpdateMetadata.setObjectName("pushButtonUpdateMetadata")
        self.pushButtonUpdateMetadata.clicked.connect(self.showXML)

        self.gridLayout.addWidget(self.pushButtonUpdateMetadata, 0, 1, 1, 1)
        self.textEditViewMetadata = QtWidgets.QTextEdit(self.View)
        self.textEditViewMetadata.setObjectName("textEditViewMetadata")
        self.gridLayout.addWidget(self.textEditViewMetadata, 1, 0, 1, 2)
        self.tabWidget.addTab(self.View, "")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.labelErrorOut = QtWidgets.QLabel(self.centralwidget)
        self.labelErrorOut.setObjectName("labelErrorOut")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelErrorOut)
        # Settings Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Package = QtWidgets.QMenu(self.menubar)
        self.menu_Package.setObjectName("menu_Package")
        self.menuVolume = QtWidgets.QMenu(self.menubar)
        self.menuVolume.setObjectName("menuVolume")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ## Menu File/Quit
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.setStatusTip('Exit application')
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        ## Menu Package/New
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setStatusTip('Create a new package')
        self.actionNew.triggered.connect(self.newPackage)
        ## Menu Package/Save
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setStatusTip('Save a package')
        self.actionSave.triggered.connect(self.savePackage)
        ## Menu Package/Load
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setStatusTip('Load a package')
        self.actionLoad.triggered.connect(self.loadPackage)
        ##Menu Volume/New
        self.actionNew2 = QtWidgets.QAction(MainWindow)
        self.actionNew2.setObjectName("actionNew2")
        self.actionNew2.setShortcut('Ctrl+n')
        self.actionNew2.setStatusTip('Add a new volume')
        self.actionNew2.triggered.connect(self.newVolume)
        ## Menu Volume/Save
        self.actionSave2 = QtWidgets.QAction(MainWindow)
        self.actionSave2.setObjectName("actionSave2")
        self.actionSave2.setShortcut('Ctrl+s')
        self.actionSave2.setStatusTip('Save a volume')
        self.actionSave2.triggered.connect(self.saveVolume)
        ## Menu Settings/Source 
        self.actionSource = QtWidgets.QAction(MainWindow)
        self.actionSource.setObjectName("actionSource")
        self.actionSource.setStatusTip('Enter the source')
        self.actionSource.triggered.connect(self.dirSource)	
        ## Menu Settings/Target
        self.actionTarget = QtWidgets.QAction(MainWindow)
        self.actionTarget.setObjectName("actionTarget")
        self.actionTarget.setStatusTip('Enter the target')
        self.actionTarget.triggered.connect(self.dirTarget)
        ## Menu Settings/Standard Image
        self.actionStandard_Image = QtWidgets.QAction(MainWindow)
        self.actionStandard_Image.setObjectName("actionStandard_Image")
        self.actionStandard_Image.setStatusTip('Select Internal copy routine as Image-Tool')
        self.actionStandard_Image.triggered.connect(self.stdImage)
        ## Menu Settings/DD
        self.action_DD = QtWidgets.QAction(MainWindow)
        self.action_DD.setObjectName("action_DD")
        self.action_DD.setStatusTip('Select DD as Image-Tool')
        self.action_DD.triggered.connect(self.ddImage)
        ## Menu Settings/DD rescue
        self.actionDD_rescue = QtWidgets.QAction(MainWindow)
        self.actionDD_rescue.setObjectName("actionDD_rescue")
        self.actionDD_rescue.setStatusTip('Select DDrescue as Image-Tool')
        self.actionDD_rescue.triggered.connect(self.ddrescueImage)
        ## Menu Settings/Kryo Flux
        self.actionKryo_Flux = QtWidgets.QAction(MainWindow)
        self.actionKryo_Flux.setObjectName("actionKryo_Flux")
        self.actionKryo_Flux.setStatusTip('Select KryoFlux as Image-Tool')
        self.actionKryo_Flux.triggered.connect(self.kryoFluxImage)
        ## Menu Help/About
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_About.triggered.connect(self.aboutUs)
        # add Menu
        self.menu_File.addAction(self.actionQuit)
        self.menu_Package.addAction(self.actionNew)
        self.menu_Package.addAction(self.actionSave)
        self.menu_Package.addAction(self.actionLoad)
        self.menuVolume.addAction(self.actionNew2)
        self.menuVolume.addAction(self.actionSave2)
        self.menuSettings.addAction(self.actionSource)
        self.menuSettings.addAction(self.actionTarget)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionStandard_Image)
        self.menuSettings.addAction(self.action_DD)
        self.menuSettings.addAction(self.actionDD_rescue)
        self.menuSettings.addAction(self.actionKryo_Flux)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Package.menuAction())
        self.menubar.addAction(self.menuVolume.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlopPyImg   "))
        self.labelSourceIn.setText(_translate("MainWindow", "Source:"))
        self.labelSourceOut.setText(_translate("MainWindow", "Input source"))
        self.labelTargetIn.setText(_translate("MainWindow", "Target:"))
        self.labelTargetOut.setText(_translate("MainWindow", "Input target"))
        self.labelIngestToolIn.setText(_translate("MainWindow", "Ingest Tool:"))
        self.labelIngestToolOut.setText(_translate("MainWindow", "Select ingest-tool"))
        self.labelPackageId.setText(_translate("MainWindow", "Package ID"))
        self.labelPackageName.setText(_translate("MainWindow", "Package Name"))
        self.labelPackageVersion.setText(_translate("MainWindow", "Package Version"))
        self.labelPackageDate.setText(_translate("MainWindow", "Package Date"))
        self.labelPackageClass.setText(_translate("MainWindow", "Package Class"))
        self.comboBoxPackageClass.setItemText(0, _translate("MainWindow", "Unknown"))
        self.comboBoxPackageClass.setItemText(1, _translate("MainWindow", "0_Original-Disk"))
        self.comboBoxPackageClass.setItemText(2, _translate("MainWindow", "Data"))
        self.comboBoxPackageClass.setItemText(3, _translate("MainWindow", "OS"))
        self.comboBoxPackageClass.setItemText(4, _translate("MainWindow", "Games"))
        self.comboBoxPackageClass.setItemText(5, _translate("MainWindow", "Various"))
        self.labelPackageEnviroment.setText(_translate("MainWindow", "Package Enviroment"))
        self.comboBoxPackageEnviroment.setItemText(0, _translate("MainWindow", "Unknown"))
        self.comboBoxPackageEnviroment.setItemText(1, _translate("MainWindow", "CP-M"))
        self.comboBoxPackageEnviroment.setItemText(2, _translate("MainWindow", "MS-DOS"))
        self.comboBoxPackageEnviroment.setItemText(3, _translate("MainWindow", "OS-2"))
        self.comboBoxPackageEnviroment.setItemText(4, _translate("MainWindow", "Atari ST"))
        self.comboBoxPackageEnviroment.setItemText(5, _translate("MainWindow", "Macintosh"))
        self.comboBoxPackageEnviroment.setItemText(6, _translate("MainWindow", "MS-Windows 3.0"))
        self.comboBoxPackageEnviroment.setItemText(7, _translate("MainWindow", "MS-Windows 32 Bit (9x, NT, 2K, XP)"))
        self.comboBoxPackageEnviroment.setItemText(8, _translate("MainWindow", "MS-Windows 64 Bit (Vista, 7, 8x, 10)"))
        self.comboBoxPackageEnviroment.setItemText(9, _translate("MainWindow", "Various"))
        self.labelPackageVolumeCount.setText(_translate("MainWindow", "Volume Count"))
        self.lineEditPackageVolumeCount.setText(_translate("MainWindow", "0"))
        self.labelPackageReserved.setText(_translate("MainWindow", "Reserved"))
        self.labelPackageDescription.setText(_translate("MainWindow", "Package Description"))
        self.labelPackageRemarks.setText(_translate("MainWindow", "Remarks"))
        self.labelPackageIngestDate.setText(_translate("MainWindow", "Ingest Date"))
        self.labelPackageArchivist.setText(_translate("MainWindow", "Archivist"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Package), _translate("MainWindow", "Package"))
        self.labelVolumeId.setText(_translate("MainWindow", "Volume ID"))
        self.labelVolumeName.setText(_translate("MainWindow", "Volume Name"))
        self.labelVolumeMedium.setText(_translate("MainWindow", "Volume Medium"))
        self.comboBoxVolumeMedium.setItemText(0, _translate("MainWindow", "Unknown"))
        self.comboBoxVolumeMedium.setItemText(1, _translate("MainWindow", "PC 5.25in SS/DD 180kb"))
        self.comboBoxVolumeMedium.setItemText(2, _translate("MainWindow", "PC 5.25in DS/DD 360kb"))
        self.comboBoxVolumeMedium.setItemText(3, _translate("MainWindow", "PC 3.5in DS/DD 720kb"))
        self.comboBoxVolumeMedium.setItemText(4, _translate("MainWindow", "PC 5.25in DS/HD 1.2mb"))
        self.comboBoxVolumeMedium.setItemText(5, _translate("MainWindow", "PC 3.5in DS/HD 1.4mb"))
        self.comboBoxVolumeMedium.setItemText(6, _translate("MainWindow", "PC 5.25in"))
        self.comboBoxVolumeMedium.setItemText(7, _translate("MainWindow", "3.5in"))
        self.comboBoxVolumeMedium.setItemText(8, _translate("MainWindow", "PC 3.5in"))
        self.comboBoxVolumeMedium.setItemText(9, _translate("MainWindow", "Various"))
        self.pushButtonVolumeMedium.setText(_translate("MainWindow", "Read Volumesize"))
        self.labelVolumeLabel.setText(_translate("MainWindow", "Volume Label"))
        self.labelVolumeDescription.setText(_translate("MainWindow", "Volume Description"))
        self.labelVolumeRemarks.setText(_translate("MainWindow", "Remarks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Volume), _translate("MainWindow", "Volume"))
        self.labelViewMetadata.setText(_translate("MainWindow", "View metadata"))
        self.pushButtonUpdateMetadata.setText(_translate("MainWindow", "Update metadata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.View), _translate("MainWindow", "Metadata"))
        self.labelErrorOut.setText(_translate("MainWindow", ""))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Package.setTitle(_translate("MainWindow", "&Package"))
        self.menuVolume.setTitle(_translate("MainWindow", "&Volume"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.actionNew2.setText(_translate("MainWindow", "&New"))
        self.actionSave2.setText(_translate("MainWindow", "Sa&ve"))
        self.actionSource.setText(_translate("MainWindow", "&Source"))
        self.actionTarget.setText(_translate("MainWindow", "&Target"))
        self.actionStandard_Image.setText(_translate("MainWindow", "&Internal copy routine"))
        self.action_DD.setText(_translate("MainWindow", "&DD"))
        self.actionDD_rescue.setText(_translate("MainWindow", "DD&rescue "))
        self.actionKryo_Flux.setText(_translate("MainWindow", "Kryo&Flux"))
        self.action_About.setText(_translate("MainWindow", "&About"))

    # business logic

    global sourceName
    sourceName  = ''
    global linuxMountPath
    linuxMountPath = ''
    global thirdDirPath
    thirdDirPath = ''
    global checkOS
    checkOS = platform.platform()
    

    def dirSource(self):
        global sourceName
        global linuxMountPath
        sourceName = ''
        linuxMountPath = ''

        if checkOS[0:5] == 'Linux':
            linuxMountPath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open your mountpath', '/media')
            linuxRawDevice, ok = QtWidgets.QInputDialog.getText(None, 'Input the filesystem', 'Enter the path for raw device')
            if ok:
                sourceName = linuxRawDevice

        elif checkOS[0:7] == 'Windows':
            sourceName = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open source', os.getenv('HOME'))

        else:
            print('unkown os')

        self.labelSourceOut.setText(sourceName)
        if sourceName == '':
            self.labelSourceOut.setText('You have not selected a source')
        print(sourceName)
        return sourceName
        
    def dirTarget(self):
        global targetName
        targetName = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open traget', os.getenv('HOME'))
        self.labelTargetOut.setText(targetName)
        if targetName == '':
            self.labelTargetOut.setText('You have not selected a target (settings target)')
        print(targetName)
        return targetName

    def newPackage(self):
        standardImage = False
        ddrescue = False
        ddV = False
        kryoFluxV = False
        self.labelIngestToolOut.setText('Select ingest-tool')
        targetName = ''
        self.labelTargetOut.setText('Input target')
        sourceName = ''
        thirdDirPath = ''
        self.labelSourceOut.setText('Input source')
        self.lineEditPackageID.clear()
        self.lineEditPackageName.clear()
        self.lineEditPackageVersion.clear()
        self.lineEditPackageDate.clear()
        self.comboBoxPackageClass.setCurrentIndex(0)
        self.comboBoxPackageEnviroment.setCurrentIndex(0)
        self.lineEditPackageVolumeCount.setText('0')
        self.lineEditPackageReserved.clear()
        self.plainTextEditPackageDescription.clear()
        self.plainTextEditPackageRemarks.clear()
        self.lineEditPackageArchivist.clear()
        self.labelErrorOut.clear()

        
    def savePackage(self):
        # pruefe ob Packet/Nachlassname ausgefuellt ist
        if self.lineEditPackageName.text() != '':
            # erstelle Verzeichnisse
            firstDirPath = targetName + os.sep + self.lineEditPackageName.text()
            if not os.path.exists(firstDirPath):
                os.makedirs(firstDirPath)
        
            secondDirPath = firstDirPath + os.sep + self.comboBoxPackageClass.currentText()
            if not os.path.exists(secondDirPath):
                os.makedirs(secondDirPath)
            
            global thirdDirPath
            thirdDirPath = secondDirPath + os.sep + self.comboBoxPackageEnviroment.currentText()
            if not os.path.exists(thirdDirPath):
                os.makedirs(thirdDirPath)
         
            # erstelle Metadaten - info.xml
            id = '  <id>' + self.lineEditPackageID.text() + '</id>'
            name = '  <name>' + self.lineEditPackageName.text() + '</name>'
            version = '  <version>' + self.lineEditPackageVersion.text() + '</version>'
            date = '  <date>' + self.lineEditPackageDate.text() + '</date>'
            classe = '  <class>' + self.comboBoxPackageClass.currentText() + '</class>'
            enviroment = '  <enviroment>' + self.comboBoxPackageEnviroment.currentText() + '</enviroment>'
            count = '  <count>' + self.lineEditPackageVolumeCount.text() + '</count>'
            reserved = '  <reserved>' + self.lineEditPackageReserved.text() + '</reserved>'
            description = '  <description>' + self.plainTextEditPackageDescription.toPlainText() + '</description>'
            remarks = '  <remarks>' + self.plainTextEditPackageRemarks.toPlainText() + '</remarks>'
            ingestDate = self.dateEditPackageIngestDate.date()
            ingestDate = str(ingestDate)
            ingestDate = '  <ingestDate>' + ingestDate[-11:-1] + '</ingestDate>'
            archivist = '  <archivist>' + self.lineEditPackageArchivist.text() + '</archivist>'
            self.lineEditPackageArchivist
            xml = '<package>' + '\n' + id + '\n' + name + '\n' + version + '\n' + date + '\n' + classe + '\n' + enviroment + '\n' + count + '\n' + reserved + '\n' + description + '\n' + remarks + '\n' + ingestDate + '\n' + archivist + '\n' + '</package>'
            infoXmlFile = thirdDirPath + '/info.xml'
            # schreib Metadatendatei
            if not os.path.isfile(infoXmlFile):
                f = open(infoXmlFile, 'w')
                f.write(xml)
                f.close()
            print(xml)
            return thirdDirPath
            self.labelErrorOut.setText('')
        else:
            self.labelErrorOut.setText('Enter a packagename')
    

    def loadPackage(self):
        global thirdDirPath
        thirdDirPath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Load file', os.getenv('HOME'))
        self.labelTargetOut.setText(thirdDirPath)
        if thirdDirPath == '':
            self.labelTargetOut.setText('you have not select a target (package load)')
        return thirdDirPath

    def VolumeAutodetect(self):
        if sourceName != '' or linuxMountPath != '':
            if sourceName != '':
                volumeSourceSize = shutil.disk_usage(sourceName)
            if linuxMountPath != '':
                volumeSourceSize = shutil.disk_usage(linuxMountPath)
            volumeSourceTotalSize = volumeSourceSize.total / 1024
            if volumeSourceTotalSize < 180:
                self.comboBoxVolumeMedium.setCurrentIndex(1)
            elif volumeSourceTotalSize < 360:
                self.comboBoxVolumeMedium.setCurrentIndex(2)
            elif volumeSourceTotalSize < 720:
                self.comboBoxVolumeMedium.setCurrentIndex(3)
            elif volumeSourceTotalSize < 1200:
                self.comboBoxVolumeMedium.setCurrentIndex(4)
            elif volumeSourceTotalSize < 1440:
                self.comboBoxVolumeMedium.setCurrentIndex(5)
            else:
                self.comboBoxVolumeMedium.setCurrentIndex(0)
        else:
            self.labelErrorOut.setText('You have not selected a source')

    def newVolume(self):
        # suche volume ID
        pathXmlFile = thirdDirPath + os.sep + 'info.xml'
        if os.path.exists(pathXmlFile):
            f = open(pathXmlFile, 'r')
            xmlFileData = f.read()
            f.close()
            dom3 = xml.dom.minidom.parseString(xmlFileData)
            volumeIdPosition = dom3.getElementsByTagName('count')
            volumeId = str(int(volumeIdPosition[0].firstChild.nodeValue) + 1)
            self.lineEditVolumeId.setText(volumeId)
        else:
            self.lineEditVolumeId.setText('1')
        self.lineEditVolumeName.clear()
        self.lineEditVolumeLabel.clear()
        self.comboBoxVolumeMedium.setCurrentIndex(0)
        self.plainTextEditVolumeDescription.clear()
        self.plainTextEditVolumeRemarks.clear()

  
    def saveVolume(self):
        print(sourceName)
        if standardImage or ddV or ddrescue:
            self.labelErrorOut.setText('')
            if standardImage:
                fileName = funktionen.nameCount('.lst', thirdDirPath)
                imgFilePath = thirdDirPath + os.sep + funktionen.nameCount('.img', thirdDirPath)
                # erstelle Image
                funktionen.imageStandard(sourceName, thirdDirPath)
                time.sleep(0.3)
                if os.path.exists(imgFilePath):
                    if checkOS[0:5] == 'Linux':
                            funktionen.contentList(linuxMountPath, fileName, thirdDirPath)
                    else:
                        funktionen.contentList(sourceName, fileName, thirdDirPath)  # bekommt die globale variable nicht übergeben
                    # erstelle md5 checksumme
                    funktionen.checkSum(thirdDirPath)

            if ddV:
                if checkOS[0:5] == 'Linux':
               
                    print(ddCommand)
                    fileName = funktionen.nameCount('.lst', thirdDirPath)
                    if checkOS[0:5] == 'Linux':
                        funktionen.contentList(linuxMountPath, fileName, thirdDirPath)
                    else:
                        funktionen.contentList(sourceName, fileName, thirdDirPath)  # bekommt die globale variable nicht übergeben
                    imgName = funktionen.nameCount('.img', thirdDirPath)
                    # erstelle Image
                    command = 'dd ' + 'if=' + sourceName + ' of=' + thirdDirPath + os.sep + imgName + ' ' + ddCommand 
                    os.system(command)
                    time.sleep(0.3)
                    funktionen.checkSum(thirdDirPath)

            if ddrescue:
                if checkOS[0:5] == 'Linux':
               
                    print(ddrescueCommand)
                    fileName = funktionen.nameCount('.lst', thirdDirPath)
                    if checkOS[0:5] == 'Linux':
                        funktionen.contentList(linuxMountPath, fileName, thirdDirPath)
                    else:
                        funktionen.contentList(sourceName, fileName, thirdDirPath)  
                    imgName = funktionen.nameCount('.img', thirdDirPath)
                    command = 'ddrescue ' + ddrescueCommand + ' ' + sourceName + ' ' + thirdDirPath + os.sep + imgName   
                    os.system(command)
                    time.sleep(0.3)
                    funktionen.checkSum(thirdDirPath)


            # füge daten in info.xml hinzu
            id = self.lineEditVolumeId.text()
            name = self.lineEditVolumeName.text()
            label = self.lineEditVolumeLabel.text()
            media = self.comboBoxVolumeMedium.currentText()
            description = self.plainTextEditVolumeDescription.toPlainText()
            remarks = self.plainTextEditVolumeRemarks.toPlainText()
            funktionen.volumeMetadata(thirdDirPath, name, media, label, description, remarks)

        else:
            self.labelErrorOut.setText('Select a ingest-tool')




    def stdImage(self):
        global standardImage
        global ddrescue
        global ddV
        global kryoFluxV
        standardImage = True
        ddrescue = False
        ddV = False
        kryoFluxV = False
        self.labelIngestToolOut.setText('Internal copy routine')
        print('standardImage is: ', standardImage)

    def ddImage(self):
        global standardImage
        global ddV
        global ddrescue
        global ddCommand
        global kryoFluxV
        ddCommand, ok = QtWidgets.QInputDialog.getText(None, 'dd parameters', 'Enter additional parameters for dd')
        if ok:
            if ddCommand == '':
                ddCommandNone = 'None'
            ddCommandNone = ''
            ddOutput = 'dd Image-Tool is active with additional parameters: ' + ddCommand + ddCommandNone
            self.labelIngestToolOut.setText(ddOutput)
            ddV = True
            ddrescue = False
            standardImage = False
            kryoFluxV = False
            print('dd is: ', ddV)

    def ddrescueImage(self):
        global standardImage
        global ddV
        global ddrescue
        global ddrescueCommand
        global kryoFluxV
        ddrescueCommand, ok = QtWidgets.QInputDialog.getText(None, 'ddrescue parameters', 'Enter additional parameters for ddrescue')
        if ok:
            if ddrescueCommand == '':
                ddrescueCommandNone = 'None'
            ddrescueCommandNone = ''
            ddrescueOutput = 'ddrescue Image-Tool is active with additional parameters: ' + ddrescueCommand + ddrescueCommandNone
            self.labelIngestToolOut.setText(ddrescueOutput)
            ddrescue = True
            ddV = False
            standardImage = False
            kryoFluxV = False
            print('ddrescue is: ', ddrescue)

    def kryoFluxImage(self):
        global standardImage
        global ddV
        global ddrescue
        global kryoFluxCommand
        global kryoFluxV
        kryoFluxCommand, ok = QtWidgets.QInputDialog.getText(None, 'kryoFlux command', 'Enter the command for kryoFlux')
        if ok:
            kryoFluxOutput = 'KryoFlux Image-Tool is active with follow parameters: ' + kryoFluxCommand
            self.labelIngestToolOut.setText(kryoFluxOutput)
            ddrescue = False
            ddV = False
            standardImage = False
            kryoFluxV = True
            print('kryoFlux is: ', kryoFluxV)
    
    
        # show XML
    def showXML(self):
        if thirdDirPath != '':
            fname = thirdDirPath + os.sep + 'info.xml'
            if os.path.exists(fname):
                f = open(fname, 'r')
                daten = f.read()
                f.close()
                self.textEditViewMetadata.setText(daten)
            else:
                self.labelErrorOut.setText('Enter a existing path')
        else:
            self.labelErrorOut.setText('Enter a target or loadpath')

    def aboutUs(self):
        QtWidgets.QMessageBox.information(None, 'About FlopPyImg', 'FlopPyImg is a open source ingest-tool for floppy disks \nCopyright by Jens Steilen', QtWidgets.QMessageBox.Yes)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

