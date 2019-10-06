# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LinkedIn_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 643)
        self.person_info = QtWidgets.QTextEdit(Dialog)
        self.person_info.setGeometry(QtCore.QRect(20, 280, 331, 81))
        self.person_info.setObjectName("person_info")
        self.found = QtWidgets.QPushButton(Dialog)
        self.found.setGeometry(QtCore.QRect(20, 560, 131, 61))
        self.found.setObjectName("found")
        self.notfound = QtWidgets.QPushButton(Dialog)
        self.notfound.setGeometry(QtCore.QRect(170, 560, 131, 61))
        self.notfound.setObjectName("notfound")
        self.next_person = QtWidgets.QPushButton(Dialog)
        self.next_person.setGeometry(QtCore.QRect(320, 560, 131, 61))
        self.next_person.setObjectName("next_person")
        self.person_msg = QtWidgets.QTextEdit(Dialog)
        self.person_msg.setGeometry(QtCore.QRect(20, 380, 331, 161))
        self.person_msg.setObjectName("person_msg")
        self.copy_info = QtWidgets.QToolButton(Dialog)
        self.copy_info.setGeometry(QtCore.QRect(360, 300, 91, 51))
        self.copy_info.setObjectName("copy_info")
        self.copy_msg = QtWidgets.QToolButton(Dialog)
        self.copy_msg.setGeometry(QtCore.QRect(360, 410, 91, 51))
        self.copy_msg.setObjectName("copy_msg")
        self.row_box = QtWidgets.QTextEdit(Dialog)
        self.row_box.setGeometry(QtCore.QRect(20, 230, 141, 31))
        self.row_box.setObjectName("row_box")
        self.row_enter = QtWidgets.QToolButton(Dialog)
        self.row_enter.setGeometry(QtCore.QRect(170, 230, 61, 31))
        self.row_enter.setObjectName("row_enter")
        self.person_counter = QtWidgets.QLabel(Dialog)
        self.person_counter.setGeometry(QtCore.QRect(260, 230, 131, 31))
        self.person_counter.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.person_counter.setObjectName("person_counter")
        self.person_combo = QtWidgets.QComboBox(Dialog)
        self.person_combo.setGeometry(QtCore.QRect(360, 490, 91, 31))
        self.person_combo.setObjectName("person_combo")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.person_combo.addItem("")
        self.GCMLogo = QtWidgets.QLabel(Dialog)
        self.GCMLogo.setGeometry(QtCore.QRect(10, 20, 341, 101))
        self.GCMLogo.setMinimumSize(QtCore.QSize(0, 0))
        self.GCMLogo.setObjectName("GCMLogo")
        self.linkedinLogo = QtWidgets.QLabel(Dialog)
        self.linkedinLogo.setGeometry(QtCore.QRect(360, 30, 91, 101))
        self.linkedinLogo.setObjectName("linkedinLogo")
        self.filename_box = QtWidgets.QTextEdit(Dialog)
        self.filename_box.setGeometry(QtCore.QRect(20, 170, 141, 41))
        self.filename_box.setObjectName("filename_box")
        self.file_enter = QtWidgets.QToolButton(Dialog)
        self.file_enter.setGeometry(QtCore.QRect(170, 170, 61, 41))
        self.file_enter.setObjectName("file_enter")
        self.template_combo = QtWidgets.QComboBox(Dialog)
        self.template_combo.setGeometry(QtCore.QRect(360, 200, 91, 31))
        self.template_combo.setObjectName("template_combo")
        self.template_combo.addItem("")
        self.template_combo.addItem("")
        self.sig_label = QtWidgets.QLabel(Dialog)
        self.sig_label.setGeometry(QtCore.QRect(380, 470, 47, 13))
        self.sig_label.setObjectName("sig_label")
        self.templ_label = QtWidgets.QLabel(Dialog)
        self.templ_label.setGeometry(QtCore.QRect(380, 180, 47, 13))
        self.templ_label.setObjectName("templ_label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 220, 47, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.person_info.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the info about each person</p></body></html>"))
        self.found.setText(_translate("Dialog", "Found"))
        self.notfound.setText(_translate("Dialog", "Not Found"))
        self.next_person.setText(_translate("Dialog", "Next"))
        self.person_msg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the message to send when connecting</p></body></html>"))
        self.copy_info.setText(_translate("Dialog", "Copy"))
        self.copy_msg.setText(_translate("Dialog", "Copy"))
        self.row_box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter row number</p></body></html>"))
        self.row_enter.setText(_translate("Dialog", "Enter"))
        self.person_counter.setText(_translate("Dialog", "1 / "))
        self.person_combo.setItemText(0, _translate("Dialog", "Mark W"))
        self.person_combo.setItemText(1, _translate("Dialog", "Hector S"))
        self.person_combo.setItemText(2, _translate("Dialog", "Steve H"))
        self.person_combo.setItemText(3, _translate("Dialog", "George L"))
        self.person_combo.setItemText(4, _translate("Dialog", "Chris C"))
        self.person_combo.setItemText(5, _translate("Dialog", "Kimberly V"))
        self.person_combo.setItemText(6, _translate("Dialog", "Gunnar L"))
        self.person_combo.setItemText(7, _translate("Dialog", "Jarrett L"))
        self.GCMLogo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/LOGO/logo_trans_resized.png\"/></p></body></html>"))
        self.linkedinLogo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/LOGO/linkedinlogo.png\"/></p></body></html>"))
        self.filename_box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter CSV file name               (eg, contacts.csv)</p></body></html>"))
        self.file_enter.setText(_translate("Dialog", "Enter"))
        self.template_combo.setItemText(0, _translate("Dialog", "Default"))
        self.template_combo.setItemText(1, _translate("Dialog", "Law Firms"))
        self.sig_label.setText(_translate("Dialog", "Signature"))
        self.templ_label.setText(_translate("Dialog", "Template"))
        self.label_3.setText(_translate("Dialog", "Row"))

import src_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

