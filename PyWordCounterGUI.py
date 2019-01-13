# -*- coding: utf-8 -*-
# Created: Thu Jan  3 17:24:13 2019
#      by: pyside2-uic  running on PySide2 5.11.4a1.dev1546291887

from PySide2 import QtCore, QtGui, QtWidgets
from pywcgui_modules.utils import *
from pywcgui_modules.operations import *

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        self.statDict = {}
        self.filteredStatDict = {}
        self.tableHeader = ["WORD", "TIMES", "SCORE(%)"]

        MainDialog.setObjectName("MainDialog")
        MainDialog.setFixedSize(800, 600)
        self.formLayoutWidget = QtWidgets.QWidget(MainDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 62))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.textFileRadio = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.textFileRadio.setChecked(True)
        self.textFileRadio.setObjectName("textFileRadio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textFileRadio)
        self.textFileInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.textFileInput.setObjectName("textFileInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textFileInput)
        self.URLInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.URLInput.setObjectName("URLInput")
        self.URLInput.setReadOnly(True)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.URLInput)
        self.URLRadio = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.URLRadio.setObjectName("URLRadio")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.URLRadio)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 10, 151, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.browseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout_3.addWidget(self.browseButton)
        self.checkButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.checkButton.setObjectName("checkButton")
        self.checkButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 611, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lengthLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lengthLabel.setObjectName("lengthLabel")
        self.horizontalLayout_4.addWidget(self.lengthLabel)
        self.lengthSpin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lengthSpin.setValue(2)
        self.lengthSpin.setMinimum(1)
        self.lengthSpin.setMaximum(1000)
        self.lengthSpin.setObjectName("lengthSpin")
        self.horizontalLayout_4.addWidget(self.lengthSpin)
        self.timesLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.timesLabel.setObjectName("timesLabel")
        self.horizontalLayout_4.addWidget(self.timesLabel)
        self.timesSpin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.timesSpin.setValue(2)
        self.timesSpin.setMinimum(1)
        self.timesSpin.setMaximum(1000000)
        self.timesSpin.setObjectName("timesSpin")
        self.horizontalLayout_4.addWidget(self.timesSpin)
        self.resultTableView = QtWidgets.QTableView(MainDialog)
        self.resultTableView.setGeometry(QtCore.QRect(10, 110, 781, 441))
        self.resultTableView.setObjectName("resultTableView")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(MainDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 560, 781, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.exportButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.exportButton.setObjectName("exportButton")
        self.exportButton.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.exportButton)
        self.analyseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.analyseButton.setObjectName("analyseButton")
        self.horizontalLayout_5.addWidget(self.analyseButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(MainDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 70, 151, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(155, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.errorDialogBox = QtWidgets.QErrorMessage(MainDialog)


        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

        """ All events """

        self.textFileRadio.toggled.connect(self.toggleInput)
        self.browseButton.released.connect(self.open)
        self.checkButton.released.connect(self.checkUrl)
        self.lengthSpin.valueChanged[int].connect(self.lengthSpinChanged)
        self.timesSpin.valueChanged[int].connect(self.timesSpinChanged)
        self.analyseButton.released.connect(self.analyse)
        self.exportButton.released.connect(self.export)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtWidgets.QApplication.translate("MainDialog", "PyWordCounter GUI", None, -1))
        self.textFileRadio.setText(QtWidgets.QApplication.translate("MainDialog", "Text File", None, -1))
        self.URLRadio.setText(QtWidgets.QApplication.translate("MainDialog", "URL", None, -1))
        self.browseButton.setText(QtWidgets.QApplication.translate("MainDialog", "Browse", None, -1))
        self.checkButton.setText(QtWidgets.QApplication.translate("MainDialog", "Check", None, -1))
        self.lengthLabel.setText(QtWidgets.QApplication.translate("MainDialog", "Length", None, -1))
        self.timesLabel.setText(QtWidgets.QApplication.translate("MainDialog", "Times", None, -1))
        self.exportButton.setText(QtWidgets.QApplication.translate("MainDialog", "Export", None, -1))
        self.analyseButton.setText(QtWidgets.QApplication.translate("MainDialog", "Analyse", None, -1))

    """ Events functions """

    def toggleInput(self, textFileRadioEnabled):
        """ Disable url input and check button when file radio is enabled, and vice-versa """

        if textFileRadioEnabled:
            self.URLInput.setReadOnly(True)
            self.checkButton.setEnabled(False)
            self.textFileInput.setReadOnly(False)
            self.browseButton.setEnabled(True)
        else:
            self.URLInput.setReadOnly(False)
            self.checkButton.setEnabled(True)
            self.textFileInput.setReadOnly(True)
            self.browseButton.setEnabled(False)

    def lengthSpinChanged(self, valueAsInt):
        """ Update data into table each time length spin value changed """

        if len(self.statDict) > 0:
            self.filteredStatDict = filterStatDict(self.statDict,
                                    int(self.lengthSpin.textFromValue(valueAsInt)),
                                    self.timesSpin.value())

            # Update data into table
            self.updateTable(toTableFormat(self.filteredStatDict))
            self.resultTableView.resizeColumnsToContents()

    def timesSpinChanged(self, valueAsInt):
        """ Update data into table each time times spin value changed """

        if len(self.statDict) > 0:
            self.filteredStatDict = filterStatDict(self.statDict,
                                    self.lengthSpin.value(),
                                    int(self.timesSpin.textFromValue(valueAsInt)))

            # Update data into table
            self.updateTable(toTableFormat(self.filteredStatDict))
            self.resultTableView.resizeColumnsToContents()

    def open(self):
        """ Open  a text file """

        filePath, type = QtWidgets.QFileDialog.getOpenFileName(
            parent=MainDialog, caption="Open Text File", filter="Txt Files (*.txt)")
        self.textFileInput.setText(filePath)

    def checkUrl(self):
        """ Check a given url """

        urlsite = self.URLInput.text()
        if len(urlsite) == 0:
            self.errorDialogBox.showMessage('URL field cannot be empty!!')
            return
        if urlReadable(urlsite):
            self.errorDialogBox.showMessage("URL: '" + urlsite +"' is OK! Click 'Analyse' to continue :)")
        else:
            self.errorDialogBox.showMessage("URL: '" + urlsite +"' cannot be analysed!")

    def analyse(self):
        """ Analyse an url or a text file """

        if self.textFileRadio.isChecked():
            filepath = self.textFileInput.text()
            if len(filepath) == 0:
                self.errorDialogBox.showMessage('Text File field cannot be empty!!')
                return
            if not fileReadable(filepath):
                self.errorDialogBox.showMessage("File: '" + filepath +"' cannot be analysed!")
            else:
                textData = readfile(filepath)
                self.statDict = analyseData(textData)
                self.filteredStatDict = filterStatDict(self.statDict, self.lengthSpin.value(), self.timesSpin.value())

                # Display data into table
                self.updateTable(toTableFormat(self.filteredStatDict))
                self.resultTableView.resizeColumnsToContents()

                # Enable export button
                self.exportButton.setEnabled(True)

        if self.URLRadio.isChecked():
            urlsite = self.URLInput.text()
            if len(urlsite) == 0:
                self.errorDialogBox.showMessage('URL field cannot be empty!!')
                return
            if urlReadable(urlsite):
                textData = readurl(urlsite)
                self.statDict = analyseData(textData)
                self.filteredStatDict = filterStatDict(self.statDict, self.lengthSpin.value(), self.timesSpin.value())

                # Display data into table
                self.updateTable(toTableFormat(self.filteredStatDict))
                self.resultTableView.resizeColumnsToContents()

                # Enable export button
                self.exportButton.setEnabled(True)

            else:
                self.errorDialogBox.showMessage("URL: '" + urlsite +"' cannot be analysed! Please 'Check' before 'Analyse.'")

    def updateTable(self, data):
        """ Update data into table """

        tablemodel = TableModel(data, self.tableHeader, MainDialog)
        self.resultTableView.setModel(tablemodel)

    def export(self):
        """ Export filtered result into CSV file """

        try:
            filePath, type = QtWidgets.QFileDialog.getSaveFileName(
                parent=MainDialog, caption="Save Into CSV File", filter="Csv Files (*.csv)")
            writeDataIntoCsvFile(filePath, self.filteredStatDict)
            self.errorDialogBox.showMessage(filePath +"' saved successfully :)")
        except:
            pass    # Cancel save


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDialog = QtWidgets.QDialog()
    ui = Ui_MainDialog()
    ui.setupUi(MainDialog)
    MainDialog.show()
    sys.exit(app.exec_())
