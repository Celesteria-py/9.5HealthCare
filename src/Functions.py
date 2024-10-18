from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6 import QtCore
from PySide6.QtCore import QSettings, QTimer, QDate
from PySide6.QtGui import QColor, QFont, QFontDatabase, QIntValidator
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from src.proc import getRes
import markdown2

from Custom_Widgets.QCustomQDialog import QCustomQDialog
# import pyodbc as odbc
import time
import sys

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'Syneras'
DATABASE_NAME = 'HealthCare'

# connection_string = f"""
#     DRIVER={{{DRIVER_NAME}}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABASE_NAME};
#     charset=utf8mb4;
#     Trust_Connection=yes;
# """
#
# maxTries = 3
# retryDelay = 5
# for attempt in range(maxTries):
#     try:
#         conn = odbc.connect(connection_string, ansi=True, autocommit=True)
#         conn.setdecoding(odbc.SQL_CHAR, encoding='utf8')
#         conn.setdecoding(odbc.SQL_WCHAR, encoding='utf8')
#         conn.setencoding(encoding='utf8')
#         break
#     except Exception as e:
#         print(f'Error during connect to data base Attempt: {attempt + 1} - {e}')
#         if attempt < maxTries - 1:
#             print(f"retrying in {retryDelay} seconds . . .")
#             time.sleep(retryDelay)
#         else:
#             print("error occurred during connect to database")
#

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        self.isLogin = False
        # self.ui.stackedWidget.setCurrentIndex(1)

        self.switchToHomePage()


        # setting menu
        self.settingMenuIsExpanded = False
        self.checkedSettingBtn = False
        self.ui.setting.clicked.connect(self.settingMenu)
        self.ui.closeSetting.clicked.connect(self.settingMenu)

        self.ui.sendSurvey.clicked.connect(self.analyzing)

        self.ui.homePage.clicked.connect(self.switchToHomePage)
        self.ui.analysisPage.clicked.connect(self.switchToAnalysisPage)
        self.ui.surveyPage.clicked.connect(self.switchToSurveyPage)
        self.ui.profilePage.clicked.connect(self.switchToProfilePage)

        # self.ui.lgPSignUp.clicked.connect(self.SignUpPage)
        # self.ui.rgPSignIn.clicked.connect(self.SignInPage)
        #
        # self.ui.lgPSignIn.clicked.connect(self.Login)
        # self.ui.rgPSignUp.clicked.connect(self.Register)

        self.ui.log.clicked.connect(self.log)

        # self.ui.goToUpdate.clicked.connect(self.inpProfilePage)
        # self.ui.update.clicked.connect(self.updateData)

        # The default value is False
        self.ui.stackedWidget.setFadeTransition(True)
        # Set the fade animation duration
        self.ui.stackedWidget.setFadeSpeed(200)
        # Set the fade easing curve
        self.ui.stackedWidget.setFadeCurve(QtCore.QEasingCurve.Linear)

        # set validator
        self.ui.weight.setValidator(QIntValidator(0, 999, self.main))
        self.ui.height.setValidator(QIntValidator(0, 999, self.main))
        self.ui.phoneNumber.setValidator(QIntValidator(0, 999999999, self.main))


    def updateData(self):
        username = self.ui.username.text()
        firstname = self.ui.inpFirstName.text()
        lastname = self.ui.inpLastName.text()
        address = self.ui.inpAddress.text()
        sexual = self.ui.inpSexual.currentText()
        phonenumber = self.ui.inpPhoneNumber.text()
        weight = self.ui.inpWeight.text()
        height = self.ui.inpHeight.text()

        print(address)

        cursor = conn.cursor()
        sql = f"""update info set 
        firstname = N'{firstname}',
        lastname = N'{lastname}',
        sexual = N'{sexual}',
        phoneNumber = N'{phonenumber}',
        weigh = N'{weight}',
        heigh = N'{height}',
        useraddress = N'{address}'
        where username = N'{username}'
"""

        cursor.execute(sql)
        self.switchToProfilePage()
        cursor.close()


    def inpProfilePage(self):
        self.ui.inpHeight.setText(self.ui.height.text())
        self.ui.inpWeight.setText(self.ui.weight.text())
        self.ui.inpSexual.setCurrentText(self.ui.sexual.currentText())
        self.ui.inpAddress.setText(self.ui.address.text())
        self.ui.inpLastName.setText(self.ui.lastName.text())
        self.ui.inpFirstName.setText(self.ui.firstName.text())
        self.ui.inpPhoneNumber.setText(self.ui.phoneNumber.text())

        self.ui.stackedWidget.setCurrentIndex(6)

    def log(self):
        if self.isLogin:
            self.isLogin = False
            self.ui.log.setText("")
            self.settingMenu()
            # self.ui.username.setText("")
            # self.ui.password.setText("")
            self.switchToHomePage()
            self.ui.firstName.setText("")
            self.ui.lastName.setText("")
            self.ui.dateOfBirth.setDate(QDate(2006, 1, 1))
            self.ui.sexual.setCurrentText("")
            self.ui.address.setText("")
            self.ui.phoneNumber.setText("")
            self.ui.weight.setText("")
            self.ui.height.setText("")
            self.ui.presick.setText("")
            self.ui.nowProb.setText("")
            self.ui.Affected.setText("")
            self.ui.Improved.setText("")
            self.ui.Others.setText("")
            self.ui.Brief.setText("")
            self.ui.Analysis.setText("")

    def showDialog(self, type, des=None):
        description = des
        if type == "Invalid enter":
            description = "Your username or password can't be empty"
        elif type == "Account exist":
            description = "Username has been used or account already existed"
        elif type == "Successfully":
            description = "You've created an account"
        elif type == "wrong account":
            description = "Your password or username is incorrect"


        dialog = QCustomQDialog(
            parent=self.main,
            title="Error",
            description=description,
            yesButtonText="Confirm",
            showYesButton=True,
            showCancelButton=False,
            setModal=True,
            frameless=True,
            windowMovable=True,
            animationDuration=500,
        )
        dialog.show()

        # events
        dialog.accepted.connect(lambda: print("Accepted!"))


    # def Register(self):
    #     regisname = self.ui.regisname.text()
    #     regispwd = self.ui.regispass.text()
    #     cursor = conn.cursor()
    #     users = cursor.execute('select username, pwd from account')
    #     rows = users.fetchall()
    #     userGetID = len(cursor.execute('select userID from info').fetchall())
    #     userID = "2024" + f"{userGetID:05d}"
    #     print(rows)
    #     rej = False
    #     if (regisname == "") or (regispwd == ""):
    #         self.showDialog(type="Invalid enter")
    #     else:
    #         for row in rows:
    #             print(row.username)
    #             if regisname == row.username:
    #                 self.showDialog(type="Account exist")
    #                 rej = True
    #
    #         if not rej:
    #             self.showDialog(type="Successfully")
    #             try:
    #                 inpAcc = cursor.execute("insert into account (username, pwd) values (?, ?)", (regisname, regispwd))
    #                 inpInfo = cursor.execute("insert into info(username, userID) values (?, ?)", (regisname, userID))
    #             except odbc.DataError as err:
    #                 conn.rollback()
    #             else:
    #                 conn.commit()
    #             cursor.close()



    # def Login(self):
    #     username = self.ui.username.text()
    #     password = self.ui.password.text()
    #     cursor = conn.cursor()
    #     users = cursor.execute("select username, pwd from account")
    #     rows = users.fetchall()
    #     print(rows[0])
    #
    #     if (username == "") or (password == ""):
    #         self.showDialog(type="Invalid enter")
    #     else:
    #         for row in rows:
    #             if username == row.username and password == row.pwd:
    #                 self.isLogin = True
    #                 self.ui.log.setText("Logout")
    #                 self.ui.stackedWidget.setCurrentIndex(0)
    #                 print("Login")
    #
    #         if not self.isLogin:
    #             self.showDialog(type="wrong account")
    #
    #     cursor.close()
    # def SignUpPage(self):
    #     self.ui.stackedWidget.setCurrentIndex(2)
    #     self.ui.regisname.setText("")
    #     self.ui.regispass.setText("")
    #     self.ui.username.setText("")
    #     self.ui.password.setText("")
    #
    # def SignInPage(self):
    #     self.ui.stackedWidget.setCurrentIndex(1)
    #     self.ui.regisname.setText("")
    #     self.ui.regispass.setText("")
    #     self.ui.username.setText("")
    #     self.ui.password.setText("")
    def switchToHomePage(self):
        # self.checkLogin()
        # if self.isLogin:
        #     self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.analysisPage.setChecked(False)
        self.ui.homePage.setChecked(True)
        self.ui.surveyPage.setChecked(False)
        self.ui.profilePage.setChecked(False)


    def switchToAnalysisPage(self):
        # self.checkLogin()
        # if self.isLogin:
        #     self.ui.stackedWidget.setCurrentIndex(4)

        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.analysisPage.setChecked(True)
        self.ui.homePage.setChecked(False)
        self.ui.surveyPage.setChecked(False)
        self.ui.profilePage.setChecked(False)

    def switchToSurveyPage(self):
        # self.checkLogin()
        # if self.isLogin:
        #     self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.analysisPage.setChecked(False)
        self.ui.homePage.setChecked(False)
        self.ui.surveyPage.setChecked(True)
        self.ui.profilePage.setChecked(False)


    def switchToProfilePage(self):
        # username = self.ui.username.text()
        #
        # cursor = conn.cursor()
        # cursor.execute("select * from info where username = ?", username)
        # rows = cursor.fetchall()
        # self.checkLogin()
        # for row in rows:
        #     self.ui.firstName.setText(row.firstname)
        #     self.ui.lastName.setText(row.lastname)
        #     self.ui.sexual.setCurrentText(row.sexual)
        #     self.ui.height.setText(str(row.heigh))
        #     self.ui.weight.setText(str(row.weigh))
        #     self.ui.address.setText(row.useraddress)
        #     self.ui.phoneNumber.setText(row.phoneNumber)
        #
        #
        # if self.isLogin:
        #     self.ui.stackedWidget.setCurrentIndex(5)
        #
        # cursor.close()

        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.analysisPage.setChecked(False)
        self.ui.homePage.setChecked(False)
        self.ui.surveyPage.setChecked(False)
        self.ui.profilePage.setChecked(True)



    # def checkLogin(self):
    #     print(self.isLogin)
    #     if not self.isLogin:
    #         self.ui.stackedWidget.setCurrentIndex(1)

    def analyzing(self):
        try:
            weight = str(self.ui.weight.text())
            height = str(self.ui.height.text())
            presick = str(self.ui.presick.text())
            nowProb = str(self.ui.nowProb.text())
            affected = str(self.ui.Affected.text())
            improved = str(self.ui.Improved.text())
            others = str(self.ui.Others.text())
            brief = str(self.ui.Brief.text())

            res = getRes(text=[weight, height, presick, nowProb, affected, improved, others, brief], type="analysis")

            html = markdown2.markdown(f"{res}")
            self.ui.Analysis.setHtml(html)
            self.isLogin = True
            self.switchToAnalysisPage()
        except Exception as e:
            self.showDialog(type='ShowError', des=e)
            print("Error", e)


    def settingMenu(self):

        if self.settingMenuIsExpanded:
            self.ui.inLeftMenu.collapseMenu()
            self.settingMenuIsExpanded = False
        else:
            self.ui.inLeftMenu.expandMenu()
            self.settingMenuIsExpanded = True

        if not self.checkedSettingBtn:
            self.ui.setting.setChecked(True)
            self.checkedSettingBtn = True
        else:
            self.ui.setting.setChecked(False)
            self.checkedSettingBtn = False

        if not self.isLogin:
            self.ui.log.setText("")
        else:
            self.ui.log.setText("Reset")
