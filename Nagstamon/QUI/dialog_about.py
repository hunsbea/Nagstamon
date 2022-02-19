# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_about(object):
    def setupUi(self, dialog_about):
        dialog_about.setObjectName("dialog_about")
        dialog_about.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_about.sizePolicy().hasHeightForWidth())
        dialog_about.setSizePolicy(sizePolicy)
        dialog_about.setSizeGripEnabled(True)
        dialog_about.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(dialog_about)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(dialog_about)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setObjectName("tabs")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.vbox_about = QtWidgets.QVBoxLayout(self.tab_about)
        self.vbox_about.setObjectName("vbox_about")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox_about.addItem(spacerItem)
        self.label_nagstamon = QtWidgets.QLabel(self.tab_about)
        self.label_nagstamon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nagstamon.setObjectName("label_nagstamon")
        self.vbox_about.addWidget(self.label_nagstamon)
        self.label_nagstamon_long = QtWidgets.QLabel(self.tab_about)
        self.label_nagstamon_long.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nagstamon_long.setObjectName("label_nagstamon_long")
        self.vbox_about.addWidget(self.label_nagstamon_long)
        self.label_copyright = QtWidgets.QLabel(self.tab_about)
        self.label_copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copyright.setObjectName("label_copyright")
        self.vbox_about.addWidget(self.label_copyright)
        self.label_website = QtWidgets.QLabel(self.tab_about)
        self.label_website.setAlignment(QtCore.Qt.AlignCenter)
        self.label_website.setObjectName("label_website")
        self.vbox_about.addWidget(self.label_website)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox_about.addItem(spacerItem1)
        self.label_footnote = QtWidgets.QLabel(self.tab_about)
        self.label_footnote.setAlignment(QtCore.Qt.AlignCenter)
        self.label_footnote.setObjectName("label_footnote")
        self.vbox_about.addWidget(self.label_footnote)
        self.tabs.addTab(self.tab_about, "")
        self.tab_credits = QtWidgets.QWidget()
        self.tab_credits.setObjectName("tab_credits")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_credits)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textedit_credits = QtWidgets.QTextBrowser(self.tab_credits)
        self.textedit_credits.setObjectName("textedit_credits")
        self.verticalLayout.addWidget(self.textedit_credits)
        self.tabs.addTab(self.tab_credits, "")
        self.tab_license = QtWidgets.QWidget()
        self.tab_license.setObjectName("tab_license")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_license)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textedit_license = QtWidgets.QTextEdit(self.tab_license)
        self.textedit_license.setObjectName("textedit_license")
        self.verticalLayout_3.addWidget(self.textedit_license)
        self.tabs.addTab(self.tab_license, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_about)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(dialog_about)
        self.tabs.setCurrentIndex(0)
        self.buttonBox.accepted.connect(dialog_about.accept)
        self.buttonBox.rejected.connect(dialog_about.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_about)

    def retranslateUi(self, dialog_about):
        _translate = QtCore.QCoreApplication.translate
        dialog_about.setWindowTitle(_translate("dialog_about", "About Nagstamon"))
        self.label_nagstamon.setText(_translate("dialog_about", "Nagstamon x"))
        self.label_nagstamon_long.setText(_translate("dialog_about", "Nagios status monitor"))
        self.label_copyright.setText(_translate("dialog_about", "©2008-2022 Henri Wahl et al."))
        self.label_website.setText(_translate("dialog_about", "https://nagstamon.de"))
        self.label_footnote.setText(_translate("dialog_about", "Footnote"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_about), _translate("dialog_about", "About"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_credits), _translate("dialog_about", "Credits"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_license), _translate("dialog_about", "License"))

