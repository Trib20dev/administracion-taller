# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_register.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 250)
        Dialog.setMinimumSize(QSize(400, 250))
        Dialog.setMaximumSize(QSize(400, 250))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(False)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_2 = QVBoxLayout(self.login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lab_login_nombre = QLabel(self.login)
        self.lab_login_nombre.setObjectName(u"lab_login_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_login_nombre)

        self.line_login_nombre = QLineEdit(self.login)
        self.line_login_nombre.setObjectName(u"line_login_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_login_nombre)

        self.lab_login_password = QLabel(self.login)
        self.lab_login_password.setObjectName(u"lab_login_password")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_login_password)

        self.line_login_password = QLineEdit(self.login)
        self.line_login_password.setObjectName(u"line_login_password")
        self.line_login_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_login_password)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.but_login_login = QPushButton(self.login)
        self.but_login_login.setObjectName(u"but_login_login")

        self.verticalLayout_2.addWidget(self.but_login_login)

        self.widget = QWidget(self.login)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lab_login_error = QLabel(self.widget)
        self.lab_login_error.setObjectName(u"lab_login_error")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_login_error.sizePolicy().hasHeightForWidth())
        self.lab_login_error.setSizePolicy(sizePolicy)
        self.lab_login_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_3.addWidget(self.lab_login_error)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.setStretch(0, 1)
        self.tabWidget.addTab(self.login, "")
        self.register = QWidget()
        self.register.setObjectName(u"register")
        self.verticalLayout_4 = QVBoxLayout(self.register)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lab_register_nombre = QLabel(self.register)
        self.lab_register_nombre.setObjectName(u"lab_register_nombre")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_register_nombre)

        self.line_register_nombre = QLineEdit(self.register)
        self.line_register_nombre.setObjectName(u"line_register_nombre")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_register_nombre)

        self.lab_register_password = QLabel(self.register)
        self.lab_register_password.setObjectName(u"lab_register_password")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_register_password)

        self.line_register_password = QLineEdit(self.register)
        self.line_register_password.setObjectName(u"line_register_password")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_register_password)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.but_register_register = QPushButton(self.register)
        self.but_register_register.setObjectName(u"but_register_register")
        self.but_register_register.setEnabled(False)

        self.verticalLayout_4.addWidget(self.but_register_register)

        self.widget_2 = QWidget(self.register)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lab_register_error = QLabel(self.widget_2)
        self.lab_register_error.setObjectName(u"lab_register_error")
        self.lab_register_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_5.addWidget(self.lab_register_error)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.tabWidget.addTab(self.register, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Form", None))
        self.lab_login_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.lab_login_password.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.but_login_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.lab_login_error.setText(QCoreApplication.translate("Dialog", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("Dialog", u"Inicio de sesion", None))
        self.lab_register_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.lab_register_password.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.but_register_register.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.lab_register_error.setText(QCoreApplication.translate("Dialog", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register), QCoreApplication.translate("Dialog", u"Registrate", None))
    # retranslateUi

