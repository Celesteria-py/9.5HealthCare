# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

from  Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 749)
        MainWindow.setMinimumSize(QSize(1150, 0))
        MainWindow.setStyleSheet(u"border-radius: 10px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #000026;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(300, 0))
        self.widget_6.setStyleSheet(u"background-color: #182733;")
        self.verticalLayout_9 = QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.topApp = QWidget(self.widget_6)
        self.topApp.setObjectName(u"topApp")
        self.topApp.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_9 = QHBoxLayout(self.topApp)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.topApp)
        self.header.setObjectName(u"header")

        self.horizontalLayout_9.addWidget(self.header)

        self.widget_4 = QWidget(self.topApp)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 25))
        self.widget_4.setMaximumSize(QSize(80, 40))
        font = QFont()
        font.setPointSize(11)
        self.widget_4.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.widget_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.widget_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.widget_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_9.addWidget(self.widget_4)


        self.verticalLayout_9.addWidget(self.topApp)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.leftMenu = QCustomSlideMenu(self.widget_7)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(170, 0))
        self.leftMenu.setFont(font)
        self.leftMenu.setStyleSheet(u"QWidget {\n"
"	background-color: #4C4C81;\n"
"	border-radius: 7px;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent; \n"
"	padding:6px;\n"
"	text-align: left;\n"
"	font-weight: normal; \n"
"	border-top: 2px solid transparent; \n"
"	border-left: 5px solid transparent;\n"
"	border-bottom: 6px solid transparent;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #191975;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #000066; \n"
"	border-left: 5px solid #000066;\n"
"	border-bottom: 6px solid #000066;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #191975;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #000066; \n"
"	border-left: 5px solid #000066;\n"
"	border-bottom: 6px solid #000066;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.headerLeftMenu = QWidget(self.leftMenu)
        self.headerLeftMenu.setObjectName(u"headerLeftMenu")
        self.headerLeftMenu.setMaximumSize(QSize(64, 64))
        self.headerLeftMenu.setFont(font)
        self.headerLeftMenu.setStyleSheet(u"min-width: 2em;\n"
"min-height: 2em;")
        self.horizontalLayout_2 = QHBoxLayout(self.headerLeftMenu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu = QPushButton(self.headerLeftMenu)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(49, 52))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.menu.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon3)
        self.menu.setFlat(False)

        self.horizontalLayout_2.addWidget(self.menu)


        self.verticalLayout.addWidget(self.headerLeftMenu, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.leftPages = QWidget(self.leftMenu)
        self.leftPages.setObjectName(u"leftPages")
        self.leftPages.setMinimumSize(QSize(144, 196))
        self.leftPages.setMaximumSize(QSize(144, 196))
        self.leftPages.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.leftPages)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.homePage = QPushButton(self.leftPages)
        self.homePage.setObjectName(u"homePage")
        self.homePage.setMinimumSize(QSize(130, 0))
        self.homePage.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homePage.setIcon(icon4)
        self.homePage.setCheckable(True)

        self.verticalLayout_3.addWidget(self.homePage)

        self.profilePage = QPushButton(self.leftPages)
        self.profilePage.setObjectName(u"profilePage")
        self.profilePage.setMinimumSize(QSize(130, 0))
        self.profilePage.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profilePage.setIcon(icon5)
        self.profilePage.setCheckable(True)

        self.verticalLayout_3.addWidget(self.profilePage)

        self.surveyPage = QPushButton(self.leftPages)
        self.surveyPage.setObjectName(u"surveyPage")
        self.surveyPage.setMinimumSize(QSize(130, 0))
        self.surveyPage.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_regular/icons/font_awesome/regular/newspaper.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.surveyPage.setIcon(icon6)
        self.surveyPage.setCheckable(True)

        self.verticalLayout_3.addWidget(self.surveyPage)

        self.analysisPage = QPushButton(self.leftPages)
        self.analysisPage.setObjectName(u"analysisPage")
        self.analysisPage.setMinimumSize(QSize(130, 0))
        self.analysisPage.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/list-ul.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analysisPage.setIcon(icon7)
        self.analysisPage.setCheckable(True)

        self.verticalLayout_3.addWidget(self.analysisPage)


        self.verticalLayout.addWidget(self.leftPages, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.moreDetails = QWidget(self.leftMenu)
        self.moreDetails.setObjectName(u"moreDetails")
        self.moreDetails.setMinimumSize(QSize(130, 150))
        self.moreDetails.setMaximumSize(QSize(16777215, 150))
        self.moreDetails.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.moreDetails)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.setting = QPushButton(self.moreDetails)
        self.setting.setObjectName(u"setting")
        self.setting.setMinimumSize(QSize(130, 0))
        self.setting.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting.setIcon(icon8)
        self.setting.setCheckable(True)
        self.setting.setChecked(False)

        self.verticalLayout_4.addWidget(self.setting)

        self.information = QPushButton(self.moreDetails)
        self.information.setObjectName(u"information")
        self.information.setMinimumSize(QSize(130, 0))
        self.information.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.information.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.information)

        self.help = QPushButton(self.moreDetails)
        self.help.setObjectName(u"help")
        self.help.setMinimumSize(QSize(130, 0))
        self.help.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help.setIcon(icon10)

        self.verticalLayout_4.addWidget(self.help)


        self.verticalLayout.addWidget(self.moreDetails, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_8.addWidget(self.leftMenu)

        self.inLeftMenu = QCustomSlideMenu(self.widget_7)
        self.inLeftMenu.setObjectName(u"inLeftMenu")
        self.inLeftMenu.setMinimumSize(QSize(0, 0))
        self.inLeftMenu.setMaximumSize(QSize(200, 16777215))
        self.inLeftMenu.setFont(font)
        self.inLeftMenu.setStyleSheet(u"QWidget {\n"
"	background-color: #4C4C81;\n"
"	border-radius: 7px;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 12px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.inLeftMenu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.inLeftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.widget.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.closeSetting = QPushButton(self.widget)
        self.closeSetting.setObjectName(u"closeSetting")
        self.closeSetting.setFont(font)
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeSetting.setIcon(icon11)

        self.horizontalLayout_3.addWidget(self.closeSetting)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.inLeftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(u"background-color: #33336F;")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.log = QPushButton(self.widget_2)
        self.log.setObjectName(u"log")

        self.verticalLayout_6.addWidget(self.log)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_6.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_6.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_6.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_6.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_6.addWidget(self.pushButton_14)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_8.addWidget(self.inLeftMenu)

        self.mainBody = QWidget(self.widget_7)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(400, 0))
        self.mainBody.setMaximumSize(QSize(16777215, 16777215))
        self.mainBody.setFont(font)
        self.mainBody.setStyleSheet(u"\n"
"QWidget {\n"
"	background-color: #4C4C81;\n"
"	border-radius: 7px;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #666693;\n"
"	placeholder-text-color: #7D7DA4;\n"
"	border-radius: 2px;\n"
"	border-style: outset;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"	background-color: #5b3f5b;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 2px;\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.mainBody)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 5)
        self.headMain = QWidget(self.mainBody)
        self.headMain.setObjectName(u"headMain")
        self.headMain.setFont(font)
        self.headMain.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.headMain)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.headMain)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.headMain)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"border: none;\n"
"placeholder-text-color: white;")
        self.lineEdit.setMaxLength(0)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.headMain)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: #666693;")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.headMain)

        self.stackedWidget = QCustomQStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(592, 559))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"background-color:  #33336F;\n"
"border: none;}\n"
"\n"
"QLineEdit {\n"
"	background-color: #666693;\n"
"	border-radius: 3px;\n"
"	border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #191975;\n"
"	border-radius: 4px;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #000066; \n"
"	border-left: 3px solid #000066;\n"
"	border-bottom: 4px solid #000066;\n"
"}\n"
"QDateEdit {\n"
"	min-width: 10em;\n"
"}")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.verticalLayout_38 = QVBoxLayout(self.HomePage)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.scrollArea = QScrollArea(self.HomePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 2613, 2064))
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_39.setSpacing(30)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_39.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 2000))
        self.verticalLayout_40 = QVBoxLayout(self.widget_8)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_27 = QLabel(self.widget_8)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_40.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_39.addWidget(self.widget_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_38.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.HomePage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_15 = QVBoxLayout(self.loginPage)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.loginPage)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 180))
        self.widget_19.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_9 = QSpacerItem(265, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.label_16 = QLabel(self.widget_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(150, 150))
        self.label_16.setPixmap(QPixmap(u":/font_awesome_regular/icons/font_awesome/regular/circle-user.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.horizontalSpacer_10 = QSpacerItem(264, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)


        self.verticalLayout_15.addWidget(self.widget_19)

        self.widget_14 = QWidget(self.loginPage)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_6 = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.widget_20 = QWidget(self.widget_14)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(342, 0))
        self.widget_20.setMaximumSize(QSize(320, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.widget_20)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_17 = QVBoxLayout(self.widget_21)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.LoginLabel = QLabel(self.widget_21)
        self.LoginLabel.setObjectName(u"LoginLabel")
        self.LoginLabel.setMinimumSize(QSize(50, 0))
        font2 = QFont()
        font2.setPointSize(18)
        self.LoginLabel.setFont(font2)
        self.LoginLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.LoginLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_17 = QLabel(self.widget_21)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_17.setFont(font3)

        self.verticalLayout_17.addWidget(self.label_17)


        self.verticalLayout_18.addWidget(self.widget_21)

        self.widget_15 = QWidget(self.widget_20)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(342, 0))
        self.widget_15.setMaximumSize(QSize(16777215, 16777215))
        self.widget_15.setStyleSheet(u"QPushButton {\n"
"	background-color: #2C0D59;\n"
"	border-style: outset;\n"
"	border-color: #6FB0E5;\n"
"	border-radius: 7px;\n"
"	padding-left: 5px;;\n"
"	height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#381170;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #270B4E;\n"
"	border-left: 3px solid #270B4E;\n"
"	border-bottom: 4px solid #270B4E;\n"
"}\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_13 = QVBoxLayout(self.widget_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 5, 0)
        self.label_13 = QLabel(self.widget_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))

        self.verticalLayout_13.addWidget(self.label_13)

        self.label_15 = QLabel(self.widget_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))

        self.verticalLayout_13.addWidget(self.label_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_15.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(280, 0))
        self.widget_17.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.widget_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.username = QLineEdit(self.widget_17)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))

        self.verticalLayout_16.addWidget(self.username)

        self.password = QLineEdit(self.widget_17)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.password)

        self.widget_23 = QWidget(self.widget_17)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.lgPSignIn = QPushButton(self.widget_23)
        self.lgPSignIn.setObjectName(u"lgPSignIn")
        self.lgPSignIn.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_19.addWidget(self.lgPSignIn)

        self.lgPSignUp = QPushButton(self.widget_23)
        self.lgPSignUp.setObjectName(u"lgPSignUp")
        self.lgPSignUp.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_19.addWidget(self.lgPSignUp)


        self.verticalLayout_16.addWidget(self.widget_23)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)


        self.horizontalLayout_15.addWidget(self.widget_17)


        self.verticalLayout_18.addWidget(self.widget_15)


        self.horizontalLayout_14.addWidget(self.widget_20)

        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_15.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.loginPage)
        self.regisPage = QWidget()
        self.regisPage.setObjectName(u"regisPage")
        self.verticalLayout_10 = QVBoxLayout(self.regisPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.regisPage)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 180))
        self.widget_22.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_11 = QSpacerItem(265, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)

        self.label_18 = QLabel(self.widget_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(150, 150))
        self.label_18.setPixmap(QPixmap(u":/font_awesome_regular/icons/font_awesome/regular/circle-user.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_18)

        self.horizontalSpacer_12 = QSpacerItem(264, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)


        self.verticalLayout_10.addWidget(self.widget_22)

        self.widget_18 = QWidget(self.regisPage)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_13 = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.widget_24 = QWidget(self.widget_18)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(342, 0))
        self.widget_24.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.widget_24)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_12.setSpacing(65)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_25)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignLeft)

        self.LoginLabel_2 = QLabel(self.widget_25)
        self.LoginLabel_2.setObjectName(u"LoginLabel_2")
        self.LoginLabel_2.setMinimumSize(QSize(50, 0))
        self.LoginLabel_2.setFont(font2)
        self.LoginLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.LoginLabel_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_19.addWidget(self.widget_25, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_58 = QWidget(self.widget_24)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMinimumSize(QSize(0, 30))

        self.verticalLayout_19.addWidget(self.widget_58)

        self.widget_26 = QWidget(self.widget_24)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(342, 0))
        self.widget_26.setMaximumSize(QSize(16777215, 16777215))
        self.widget_26.setStyleSheet(u"QPushButton {\n"
"	background-color: #2C0D59;\n"
"	border-style: outset;\n"
"	border-color: #6FB0E5;\n"
"	border-radius: 7px;\n"
"	padding-left: 5px;;\n"
"	height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#381170;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #270B4E;\n"
"	border-left: 3px solid #270B4E;\n"
"	border-bottom: 4px solid #270B4E;\n"
"}\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_14 = QVBoxLayout(self.widget_27)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 5, 0)
        self.label_20 = QLabel(self.widget_27)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.label_20)

        self.label_7 = QLabel(self.widget_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.label_7)

        self.label_14 = QLabel(self.widget_27)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.label_14)

        self.label_22 = QLabel(self.widget_27)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.label_22)

        self.label_21 = QLabel(self.widget_27)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.label_21)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)


        self.horizontalLayout_20.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(280, 0))
        self.widget_28.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.widget_28)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.regisname = QLineEdit(self.widget_28)
        self.regisname.setObjectName(u"regisname")
        self.regisname.setMinimumSize(QSize(0, 30))

        self.verticalLayout_21.addWidget(self.regisname)

        self.studentID = QLineEdit(self.widget_28)
        self.studentID.setObjectName(u"studentID")
        self.studentID.setMinimumSize(QSize(0, 30))

        self.verticalLayout_21.addWidget(self.studentID)

        self.email = QLineEdit(self.widget_28)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(0, 30))

        self.verticalLayout_21.addWidget(self.email)

        self.regispass = QLineEdit(self.widget_28)
        self.regispass.setObjectName(u"regispass")
        self.regispass.setMinimumSize(QSize(0, 30))
        self.regispass.setEchoMode(QLineEdit.EchoMode.Password)
        self.regispass.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.regispass)

        self.confrim = QLineEdit(self.widget_28)
        self.confrim.setObjectName(u"confrim")
        self.confrim.setMinimumSize(QSize(0, 30))

        self.verticalLayout_21.addWidget(self.confrim)

        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.rgPSignIn = QPushButton(self.widget_29)
        self.rgPSignIn.setObjectName(u"rgPSignIn")
        self.rgPSignIn.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.rgPSignIn)

        self.rgPSignUp = QPushButton(self.widget_29)
        self.rgPSignUp.setObjectName(u"rgPSignUp")
        self.rgPSignUp.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.rgPSignUp)


        self.verticalLayout_21.addWidget(self.widget_29)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_20.addWidget(self.widget_28)


        self.verticalLayout_19.addWidget(self.widget_26)


        self.horizontalLayout_16.addWidget(self.widget_24)

        self.horizontalSpacer_14 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_15 = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.verticalLayout_10.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.regisPage)
        self.SurveyPage = QWidget()
        self.SurveyPage.setObjectName(u"SurveyPage")
        self.verticalLayout_25 = QVBoxLayout(self.SurveyPage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_36 = QWidget(self.SurveyPage)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMaximumSize(QSize(1200, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.widget_36)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_38 = QWidget(self.widget_36)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_6 = QLabel(self.widget_38)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_27.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.presick = QLineEdit(self.widget_38)
        self.presick.setObjectName(u"presick")
        self.presick.setMinimumSize(QSize(538, 25))
        self.presick.setMaximumSize(QSize(16777215, 25))
        self.presick.setFont(font3)

        self.horizontalLayout_27.addWidget(self.presick)


        self.verticalLayout_26.addWidget(self.widget_38, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_39 = QWidget(self.widget_36)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_34 = QLabel(self.widget_39)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.horizontalLayout_28.addWidget(self.label_34, 0, Qt.AlignmentFlag.AlignLeft)

        self.nowProb = QLineEdit(self.widget_39)
        self.nowProb.setObjectName(u"nowProb")
        self.nowProb.setMinimumSize(QSize(484, 25))
        self.nowProb.setMaximumSize(QSize(16777215, 25))
        self.nowProb.setFont(font3)
        self.nowProb.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.nowProb)


        self.verticalLayout_26.addWidget(self.widget_39, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_25.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.SurveyPage)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_27 = QVBoxLayout(self.widget_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_40 = QWidget(self.widget_37)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_29 = QVBoxLayout(self.widget_40)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_35 = QLabel(self.widget_40)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.verticalLayout_29.addWidget(self.label_35)

        self.Affected = QLineEdit(self.widget_40)
        self.Affected.setObjectName(u"Affected")
        self.Affected.setMinimumSize(QSize(0, 25))
        self.Affected.setMaximumSize(QSize(1200, 25))
        self.Affected.setFont(font3)

        self.verticalLayout_29.addWidget(self.Affected)


        self.verticalLayout_27.addWidget(self.widget_40)

        self.widget_42 = QWidget(self.widget_37)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_28 = QVBoxLayout(self.widget_42)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_36 = QLabel(self.widget_42)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.verticalLayout_28.addWidget(self.label_36)

        self.Improved = QLineEdit(self.widget_42)
        self.Improved.setObjectName(u"Improved")
        self.Improved.setMinimumSize(QSize(0, 25))
        self.Improved.setMaximumSize(QSize(1200, 25))
        self.Improved.setFont(font3)

        self.verticalLayout_28.addWidget(self.Improved)


        self.verticalLayout_27.addWidget(self.widget_42)

        self.widget_41 = QWidget(self.widget_37)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_31 = QVBoxLayout(self.widget_41)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_37 = QLabel(self.widget_41)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.verticalLayout_31.addWidget(self.label_37)

        self.Others = QLineEdit(self.widget_41)
        self.Others.setObjectName(u"Others")
        self.Others.setMinimumSize(QSize(0, 25))
        self.Others.setMaximumSize(QSize(1200, 25))
        self.Others.setFont(font3)

        self.verticalLayout_31.addWidget(self.Others)


        self.verticalLayout_27.addWidget(self.widget_41)

        self.widget_43 = QWidget(self.widget_37)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_30 = QVBoxLayout(self.widget_43)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_38 = QLabel(self.widget_43)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.verticalLayout_30.addWidget(self.label_38)

        self.Brief = QLineEdit(self.widget_43)
        self.Brief.setObjectName(u"Brief")
        self.Brief.setMinimumSize(QSize(0, 25))
        self.Brief.setMaximumSize(QSize(1200, 25))
        self.Brief.setFont(font3)

        self.verticalLayout_30.addWidget(self.Brief)

        self.widget_44 = QWidget(self.widget_43)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_30.addWidget(self.widget_44, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_27.addWidget(self.widget_43)

        self.sendSurvey = QPushButton(self.widget_37)
        self.sendSurvey.setObjectName(u"sendSurvey")
        self.sendSurvey.setMinimumSize(QSize(80, 35))

        self.verticalLayout_27.addWidget(self.sendSurvey, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_3)


        self.verticalLayout_25.addWidget(self.widget_37)

        self.stackedWidget.addWidget(self.SurveyPage)
        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName(u"AnalysisPage")
        self.verticalLayout_37 = QVBoxLayout(self.AnalysisPage)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Analysis = QTextBrowser(self.AnalysisPage)
        self.Analysis.setObjectName(u"Analysis")
        self.Analysis.setFont(font3)

        self.verticalLayout_37.addWidget(self.Analysis)

        self.stackedWidget.addWidget(self.AnalysisPage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.verticalLayout_36 = QVBoxLayout(self.ProfilePage)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.headerProfile_2 = QWidget(self.ProfilePage)
        self.headerProfile_2.setObjectName(u"headerProfile_2")
        self.headerProfile_2.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_20 = QVBoxLayout(self.headerProfile_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_46 = QLabel(self.headerProfile_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_46)


        self.verticalLayout_36.addWidget(self.headerProfile_2)

        self.bodyProfile_2 = QWidget(self.ProfilePage)
        self.bodyProfile_2.setObjectName(u"bodyProfile_2")
        self.bodyProfile_2.setMinimumSize(QSize(0, 400))
        self.verticalLayout_32 = QVBoxLayout(self.bodyProfile_2)
        self.verticalLayout_32.setSpacing(1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(1, 1, 1, 1)
        self.widget_45 = QWidget(self.bodyProfile_2)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_33 = QVBoxLayout(self.widget_45)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_30 = QLabel(self.widget_45)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_30)


        self.verticalLayout_32.addWidget(self.widget_45)

        self.widget_46 = QWidget(self.bodyProfile_2)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_47 = QWidget(self.widget_46)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.widget_47)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(30, 16777215))
        self.label_31.setFont(font3)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.firstName = QLineEdit(self.widget_47)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setMinimumSize(QSize(175, 25))
        self.firstName.setMaximumSize(QSize(175, 25))
        self.firstName.setFont(font3)
        self.firstName.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.firstName.setMouseTracking(True)
        self.firstName.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.firstName.setMaxLength(50)
        self.firstName.setEchoMode(QLineEdit.EchoMode.Normal)
        self.firstName.setReadOnly(False)

        self.horizontalLayout_32.addWidget(self.firstName)

        self.label_32 = QLabel(self.widget_47)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(30, 16777215))
        self.label_32.setFont(font3)

        self.horizontalLayout_32.addWidget(self.label_32)

        self.lastName = QLineEdit(self.widget_47)
        self.lastName.setObjectName(u"lastName")
        self.lastName.setMinimumSize(QSize(80, 25))
        self.lastName.setMaximumSize(QSize(80, 25))
        self.lastName.setFont(font3)
        self.lastName.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lastName.setMouseTracking(True)
        self.lastName.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.lastName.setMaxLength(20)
        self.lastName.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lastName.setReadOnly(False)

        self.horizontalLayout_32.addWidget(self.lastName)


        self.horizontalLayout_31.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.widget_46)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(405, 0))
        self.widget_48.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.widget_48.setStyleSheet(u"QComboBox {\n"
"	background-color: ;\n"
"}")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.widget_48)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setFont(font3)

        self.horizontalLayout_33.addWidget(self.label_33)

        self.sexual = QComboBox(self.widget_48)
        self.sexual.addItem("")
        self.sexual.addItem("")
        self.sexual.addItem("")
        self.sexual.addItem("")
        self.sexual.setObjectName(u"sexual")
        self.sexual.setEnabled(True)
        self.sexual.setMinimumSize(QSize(75, 0))
        self.sexual.setFont(font3)
        self.sexual.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.sexual.setMouseTracking(False)
        self.sexual.setTabletTracking(True)
        self.sexual.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.sexual.setAcceptDrops(False)
        self.sexual.setEditable(False)
        self.sexual.setIconSize(QSize(0, 0))

        self.horizontalLayout_33.addWidget(self.sexual)

        self.label_39 = QLabel(self.widget_48)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.horizontalLayout_33.addWidget(self.label_39)

        self.dateOfBirth = QDateEdit(self.widget_48)
        self.dateOfBirth.setObjectName(u"dateOfBirth")
        self.dateOfBirth.setMinimumSize(QSize(160, 0))
        self.dateOfBirth.setFont(font3)
        self.dateOfBirth.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dateOfBirth.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateOfBirth.setCalendarPopup(True)
        self.dateOfBirth.setCurrentSectionIndex(0)
        self.dateOfBirth.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateOfBirth.setDate(QDate(2006, 1, 1))

        self.horizontalLayout_33.addWidget(self.dateOfBirth)


        self.horizontalLayout_31.addWidget(self.widget_48)


        self.verticalLayout_32.addWidget(self.widget_46, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_49 = QWidget(self.bodyProfile_2)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_50 = QWidget(self.widget_49)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_50)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.horizontalLayout_35.addWidget(self.label_40)

        self.address = QLineEdit(self.widget_50)
        self.address.setObjectName(u"address")
        self.address.setMinimumSize(QSize(500, 25))
        self.address.setMaximumSize(QSize(500, 25))
        self.address.setFont(font3)
        self.address.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.address.setMouseTracking(True)
        self.address.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.address.setMaxLength(500)
        self.address.setEchoMode(QLineEdit.EchoMode.Normal)
        self.address.setReadOnly(False)

        self.horizontalLayout_35.addWidget(self.address)


        self.horizontalLayout_34.addWidget(self.widget_50, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_51 = QWidget(self.widget_49)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_41 = QLabel(self.widget_51)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.horizontalLayout_36.addWidget(self.label_41)

        self.phoneNumber = QLineEdit(self.widget_51)
        self.phoneNumber.setObjectName(u"phoneNumber")
        self.phoneNumber.setMinimumSize(QSize(104, 25))
        self.phoneNumber.setMaximumSize(QSize(104, 25))
        self.phoneNumber.setFont(font3)
        self.phoneNumber.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.phoneNumber.setMouseTracking(True)
        self.phoneNumber.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.phoneNumber.setMaxLength(10)
        self.phoneNumber.setEchoMode(QLineEdit.EchoMode.Normal)
        self.phoneNumber.setReadOnly(False)

        self.horizontalLayout_36.addWidget(self.phoneNumber)


        self.horizontalLayout_34.addWidget(self.widget_51, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_32.addWidget(self.widget_49, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_52 = QWidget(self.bodyProfile_2)
        self.widget_52.setObjectName(u"widget_52")
        self.verticalLayout_34 = QVBoxLayout(self.widget_52)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.widget_52)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)

        self.verticalLayout_34.addWidget(self.label_42)


        self.verticalLayout_32.addWidget(self.widget_52)

        self.widget_53 = QWidget(self.bodyProfile_2)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_35 = QVBoxLayout(self.widget_53)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_43 = QLabel(self.widget_54)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.horizontalLayout_37.addWidget(self.label_43)

        self.height = QLineEdit(self.widget_54)
        self.height.setObjectName(u"height")
        self.height.setMinimumSize(QSize(123, 25))
        self.height.setMaximumSize(QSize(123, 25))
        self.height.setFont(font3)
        self.height.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.height.setMouseTracking(True)
        self.height.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.height.setMaxLength(3)
        self.height.setEchoMode(QLineEdit.EchoMode.Normal)
        self.height.setReadOnly(False)

        self.horizontalLayout_37.addWidget(self.height)

        self.label_44 = QLabel(self.widget_54)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.horizontalLayout_37.addWidget(self.label_44)

        self.weight = QLineEdit(self.widget_54)
        self.weight.setObjectName(u"weight")
        self.weight.setMinimumSize(QSize(123, 25))
        self.weight.setMaximumSize(QSize(123, 25))
        self.weight.setFont(font3)
        self.weight.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.weight.setMouseTracking(True)
        self.weight.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.weight.setMaxLength(3)
        self.weight.setEchoMode(QLineEdit.EchoMode.Normal)
        self.weight.setReadOnly(False)

        self.horizontalLayout_37.addWidget(self.weight)


        self.verticalLayout_35.addWidget(self.widget_54, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_55 = QWidget(self.widget_53)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_45 = QLabel(self.widget_55)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.horizontalLayout_38.addWidget(self.label_45)

        self.lineEdit_27 = QLineEdit(self.widget_55)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setEnabled(True)
        self.lineEdit_27.setMinimumSize(QSize(123, 25))
        self.lineEdit_27.setMaximumSize(QSize(123, 25))
        self.lineEdit_27.setFont(font3)
        self.lineEdit_27.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.lineEdit_27.setMouseTracking(True)
        self.lineEdit_27.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_27.setMaxLength(0)
        self.lineEdit_27.setFrame(True)
        self.lineEdit_27.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_27.setReadOnly(False)
        self.lineEdit_27.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.horizontalLayout_38.addWidget(self.lineEdit_27)


        self.verticalLayout_35.addWidget(self.widget_55, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_56 = QWidget(self.widget_53)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")

        self.verticalLayout_35.addWidget(self.widget_56)


        self.verticalLayout_32.addWidget(self.widget_53)


        self.verticalLayout_36.addWidget(self.bodyProfile_2)

        self.footerProffile_2 = QWidget(self.ProfilePage)
        self.footerProffile_2.setObjectName(u"footerProffile_2")
        self.footerProffile_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #191975;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #000066; \n"
"	border-left: 5px solid #000066;\n"
"	border-bottom: 6px solid #000066;\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.footerProffile_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.goToUpdate = QPushButton(self.footerProffile_2)
        self.goToUpdate.setObjectName(u"goToUpdate")
        self.goToUpdate.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_40.addWidget(self.goToUpdate, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_36.addWidget(self.footerProffile_2)

        self.stackedWidget.addWidget(self.ProfilePage)
        self.InputProfilePage = QWidget()
        self.InputProfilePage.setObjectName(u"InputProfilePage")
        self.verticalLayout_11 = QVBoxLayout(self.InputProfilePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.headerProfile = QWidget(self.InputProfilePage)
        self.headerProfile.setObjectName(u"headerProfile")
        self.headerProfile.setMaximumSize(QSize(16777215, 80))
        self.label_8 = QLabel(self.headerProfile)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 20, 231, 16))
        self.label_8.setFont(font3)

        self.verticalLayout_11.addWidget(self.headerProfile)

        self.bodyProfile = QWidget(self.InputProfilePage)
        self.bodyProfile.setObjectName(u"bodyProfile")
        self.bodyProfile.setMinimumSize(QSize(0, 400))
        self.verticalLayout_12 = QVBoxLayout(self.bodyProfile)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.widget_10 = QWidget(self.bodyProfile)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_22 = QVBoxLayout(self.widget_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_22.addWidget(self.label_9)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.bodyProfile)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 16777215))
        self.label_10.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.inpFirstName = QLineEdit(self.widget_11)
        self.inpFirstName.setObjectName(u"inpFirstName")
        self.inpFirstName.setMinimumSize(QSize(175, 25))
        self.inpFirstName.setMaximumSize(QSize(175, 16777215))
        self.inpFirstName.setFont(font3)

        self.horizontalLayout_11.addWidget(self.inpFirstName)

        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(30, 16777215))
        self.label_11.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.inpLastName = QLineEdit(self.widget_11)
        self.inpLastName.setObjectName(u"inpLastName")
        self.inpLastName.setMinimumSize(QSize(80, 25))
        self.inpLastName.setMaximumSize(QSize(80, 16777215))
        self.inpLastName.setFont(font3)

        self.horizontalLayout_11.addWidget(self.inpLastName)


        self.horizontalLayout_10.addWidget(self.widget_11, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_57 = QWidget(self.widget_9)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(441, 40))
        self.widget_57.setMaximumSize(QSize(16777215, 16777215))
        self.widget_57.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.widget_57.setStyleSheet(u"QComboBox {\n"
"	background-color: ;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_47 = QLabel(self.widget_57)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font3)

        self.horizontalLayout_41.addWidget(self.label_47)

        self.inpSexual = QComboBox(self.widget_57)
        self.inpSexual.addItem("")
        self.inpSexual.addItem("")
        self.inpSexual.addItem("")
        self.inpSexual.addItem("")
        self.inpSexual.setObjectName(u"inpSexual")
        self.inpSexual.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_41.addWidget(self.inpSexual)

        self.label_48 = QLabel(self.widget_57)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)

        self.horizontalLayout_41.addWidget(self.label_48)

        self.inpDateOfBirth = QDateEdit(self.widget_57)
        self.inpDateOfBirth.setObjectName(u"inpDateOfBirth")
        self.inpDateOfBirth.setMinimumSize(QSize(160, 22))
        self.inpDateOfBirth.setMaximumSize(QSize(200, 22))
        self.inpDateOfBirth.setFont(font3)
        self.inpDateOfBirth.setMouseTracking(False)
        self.inpDateOfBirth.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.inpDateOfBirth.setAcceptDrops(True)
        self.inpDateOfBirth.setAutoFillBackground(True)
        self.inpDateOfBirth.setCalendarPopup(True)
        self.inpDateOfBirth.setCurrentSectionIndex(0)
        self.inpDateOfBirth.setTimeSpec(Qt.TimeSpec.UTC)
        self.inpDateOfBirth.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_41.addWidget(self.inpDateOfBirth)


        self.horizontalLayout_10.addWidget(self.widget_57, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.widget_13 = QWidget(self.bodyProfile)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_13)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(579, 84))
        self.widget_12.setMaximumSize(QSize(579, 84))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.inpAddress = QLineEdit(self.widget_12)
        self.inpAddress.setObjectName(u"inpAddress")
        self.inpAddress.setMinimumSize(QSize(0, 25))
        self.inpAddress.setFont(font3)

        self.horizontalLayout_13.addWidget(self.inpAddress)


        self.horizontalLayout_23.addWidget(self.widget_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_30 = QWidget(self.widget_13)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(200, 84))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_23 = QLabel(self.widget_30)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.horizontalLayout_22.addWidget(self.label_23)

        self.inpPhoneNumber = QLineEdit(self.widget_30)
        self.inpPhoneNumber.setObjectName(u"inpPhoneNumber")
        self.inpPhoneNumber.setMinimumSize(QSize(104, 25))
        self.inpPhoneNumber.setFont(font3)

        self.horizontalLayout_22.addWidget(self.inpPhoneNumber)


        self.horizontalLayout_23.addWidget(self.widget_30, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_12.addWidget(self.widget_13)

        self.widget_32 = QWidget(self.bodyProfile)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_23 = QVBoxLayout(self.widget_32)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.widget_32)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_24)


        self.verticalLayout_12.addWidget(self.widget_32)

        self.widget_31 = QWidget(self.bodyProfile)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_24 = QVBoxLayout(self.widget_31)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_31)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_25 = QLabel(self.widget_33)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.horizontalLayout_24.addWidget(self.label_25)

        self.inpHeight = QLineEdit(self.widget_33)
        self.inpHeight.setObjectName(u"inpHeight")
        self.inpHeight.setMinimumSize(QSize(0, 25))
        self.inpHeight.setFont(font3)

        self.horizontalLayout_24.addWidget(self.inpHeight)

        self.label_26 = QLabel(self.widget_33)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.horizontalLayout_24.addWidget(self.label_26)

        self.inpWeight = QLineEdit(self.widget_33)
        self.inpWeight.setObjectName(u"inpWeight")
        self.inpWeight.setMinimumSize(QSize(0, 25))
        self.inpWeight.setFont(font3)

        self.horizontalLayout_24.addWidget(self.inpWeight)


        self.verticalLayout_24.addWidget(self.widget_33, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_34 = QWidget(self.widget_31)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_29 = QLabel(self.widget_34)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.horizontalLayout_25.addWidget(self.label_29)

        self.lineEdit_14 = QLineEdit(self.widget_34)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 25))
        self.lineEdit_14.setFont(font3)
        self.lineEdit_14.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.lineEdit_14.setMaxLength(3)
        self.lineEdit_14.setFrame(False)
        self.lineEdit_14.setEchoMode(QLineEdit.EchoMode.NoEcho)
        self.lineEdit_14.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.horizontalLayout_25.addWidget(self.lineEdit_14)


        self.verticalLayout_24.addWidget(self.widget_34, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_35 = QWidget(self.widget_31)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_24.addWidget(self.widget_35)


        self.verticalLayout_12.addWidget(self.widget_31)


        self.verticalLayout_11.addWidget(self.bodyProfile)

        self.footerProffile = QWidget(self.InputProfilePage)
        self.footerProffile.setObjectName(u"footerProffile")
        self.footerProffile.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #191975;\n"
"	font-weight: bold;\n"
"	border-top: 2px solid #000066; \n"
"	border-left: 5px solid #000066;\n"
"	border-bottom: 6px solid #000066;\n"
"}")
        self.horizontalLayout_30 = QHBoxLayout(self.footerProffile)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.update = QPushButton(self.footerProffile)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_30.addWidget(self.update, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_11.addWidget(self.footerProffile)

        self.stackedWidget.addWidget(self.InputProfilePage)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.widget_3 = QWidget(self.mainBody)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.widget_5)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(70, 60))
        self.logo.setPixmap(QPixmap(u"../Qss/icons/logo.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.logo)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.frame_2 = QFrame(self.widget_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_7.addWidget(self.progressBar)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.sizeGrip = QFrame(self.widget_3)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sizeGrip)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_15 = QPushButton(self.sizeGrip)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/window_grip.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon12)

        self.verticalLayout_7.addWidget(self.pushButton_15)


        self.horizontalLayout_6.addWidget(self.sizeGrip, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout_8.addWidget(self.mainBody)


        self.verticalLayout_9.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.widget_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.menu.setText("")
        self.homePage.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profilePage.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.surveyPage.setText(QCoreApplication.translate("MainWindow", u"Survey", None))
        self.analysisPage.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.information.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.closeSetting.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"References", None))
        self.log.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_9.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"9.5Health", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search . . . .  (not avaiable yet)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ctrl + K", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"M\u01b0a l\u0169 ph\u1ee9c t\u1ea1p cu\u1ed1i th\u00e1ng 10 \u1edf mi\u1ec1n Trung\n"
"\u00d4ng Ho\u00e0ng Ph\u00fac L\u00e2m, Ph\u00f3 Gi\u00e1m \u0111\u1ed1c Trung t\u00e2m D\u1ef1 b\u00e1o Kh\u00ed t\u01b0\u1ee3ng Th\u1ee7y v\u0103n Qu\u1ed1c gia cho bi\u1ebft hi\u1ec7n t\u01b0\u1ee3ng ENSO (ch\u1ec9 c\u1ea3 hai hi\u1ec7n t\u01b0\u1ee3ng El Nino v\u00e0 La Nina v\u00e0 c\u00f3 li\u00ean quan v\u1edbi dao \u0111\u1ed9ng c\u1ee7a kh\u00ed \u00e1p gi\u1eefa 2 b\u1edd ph\u00eda \u0110\u00f4ng Th\u00e1i B\u00ecnh D\u01b0\u01a1ng v\u1edbi ph\u00eda T\u00e2y Th\u00e1i B\u00ecnh D\u01b0\u01a1ng-\u0110\u00f4ng \u1ea4n \u0110\u1ed9 D\u01b0\u01a1ng) \u0111ang trong tr\u1ea1ng th\u00e1i trung t\u00ednh nh\u01b0ng nghi\u00eang d\u1ea7n v\u1ec1 pha l\u1ea1nh.\n"
"\n"
"V\u00ec v\u1eady, b\u00e3o, \u00e1p th\u1ea5p nhi\u1ec7t \u0111\u1edbi tr\u00ean khu v\u1ef1c Bi\u1ec3n \u0110\u00f4ng c\u00f3 kh\u1ea3 n\u0103ng xu\u1ea5t hi\u1ec7n \u1edf m\u1ee9c x\u1ea5p x\u1ec9 \u0111\u1ebfn cao h\u01a1n trung b\u00ecnh nhi\u1ec1u n\u0103"
                        "m (trung b\u00ecnh nhi\u1ec1u n\u0103m tr\u00ean Bi\u1ec3n \u0110\u00f4ng l\u00e0 2,8 c\u01a1n b\u00e3o, \u0111\u1ed5 b\u1ed9 v\u00e0o \u0111\u1ea5t li\u1ec1n 1,1 c\u01a1n b\u00e3o) v\u00e0 t\u1eadp trung nhi\u1ec1u \u1edf khu v\u1ef1c Trung B\u1ed9 v\u00e0 c\u00e1c t\u1ec9nh, th\u00e0nh ph\u1ed1 ph\u00eda Nam; \u0111\u1ec1 ph\u00f2ng kh\u1ea3 n\u0103ng b\u00e3o, \u00e1p th\u1ea5p nhi\u1ec7t \u0111\u1edbi h\u00ecnh th\u00e0nh ngay tr\u00ean khu v\u1ef1c Bi\u1ec3n \u0110\u00f4ng.\n"
"\n"
"Kho\u1ea3ng th\u1eddi gian n\u00e0y c\u0169ng l\u00e0 giai \u0111o\u1ea1n m\u00f9a m\u01b0a \u1edf khu v\u1ef1c mi\u1ec1n Trung v\u00e0 cao \u0111i\u1ec3m t\u1eadp trung v\u00e0o th\u00e1ng 10 - 11. C\u00e1c t\u1ec9nh t\u1eeb Qu\u1ea3ng B\u00ecnh \u0111\u1ebfn Qu\u1ea3ng Tr\u1ecb, t\u1ed5ng l\u01b0\u1ee3ng m\u01b0a ph\u1ed5 bi\u1ebfn t\u1eeb 100 - 200 mm cao h\u01a1n trung b\u00ecnh nhi\u1ec1u n\u0103m 10 - 15 mm, c\u00e1c t\u1ec9nh t\u1eeb Th\u1eeba Thi\u00ean-Hu\u1ebf \u0111\u1ebfn Kh\u00e1nh H\u00f2a t\u1ed5ng l\u01b0\u1ee3"
                        "ng m\u01b0a ph\u1ed5 bi\u1ebfn t\u1eeb 250 - 500 mm, cao h\u01a1n trung b\u00ecnh nhi\u1ec1u n\u0103m 30 - 60 mm.\n"
"\n"
"Di\u1ec5n bi\u1ebfn thi\u00ean tai m\u01b0a l\u0169 cu\u1ed1i th\u00e1ng 10 th\u1ebf n\u00e0o?- \u1ea2nh 2.\n"
"Cao \u0111i\u1ec3m m\u01b0a l\u0169 n\u0103m nay d\u1ef1 b\u00e1o s\u1ebd ph\u1ee9c t\u1ea1p.\n"
"\n"
"Kh\u00f4ng kh\u00ed l\u1ea1nh c\u00f3 kh\u1ea3 n\u0103ng ho\u1ea1t \u0111\u1ed9ng m\u1ea1nh trong th\u00e1ng 12/2024-1/2025 v\u00e0 g\u00e2y ra c\u00e1c \u0111\u1ee3t r\u00e9t \u0111\u1eadm, r\u00e9t h\u1ea1i; \u0111\u1ec1 ph\u00f2ng kh\u1ea3 n\u0103ng x\u1ea3y ra nh\u1eefng \u0111\u1ee3t r\u00e9t \u0111\u1eadm, r\u00e9t h\u1ea1i k\u00e9o d\u00e0i \u0111\u1eb7c bi\u1ec7t t\u1ea1i c\u00e1c khu v\u1ef1c v\u00f9ng n\u00fai ph\u00eda B\u1eafc, k\u00e8m theo hi\u1ec7n t\u01b0\u1ee3ng s\u01b0\u01a1ng mu\u1ed1i, b\u0103ng gi\u00e1 trong th\u1eddi gian n\u00e0y.\n"
"\n"
"Hi\u1ec7n t\u01b0\u1ee3ng r\u00e9t \u0111\u1eadm, r\u00e9t h\u1ea1i t\u1ea1i khu v\u1ef1c B\u1eafc B\u1ed9 c\u00f3 kh"
                        "\u1ea3 n\u0103ng xu\u1ea5t hi\u1ec7n tr\u00ean di\u1ec7n r\u1ed9ng t\u1eeb n\u1eeda cu\u1ed1i th\u00e1ng 12 - t\u01b0\u01a1ng \u0111\u01b0\u01a1ng so v\u1edbi trung b\u00ecnh nhi\u1ec1u n\u0103m. Tr\u00ean ph\u1ea1m vi c\u1ea3 n\u01b0\u1edbc ti\u1ebfp t\u1ee5c c\u00f3 kh\u1ea3 n\u0103ng x\u1ea3y ra c\u00e1c hi\u1ec7n t\u01b0\u1ee3ng th\u1eddi ti\u1ebft nguy hi\u1ec3m nh\u01b0 d\u00f4ng, l\u1ed1c, s\u00e9t v\u00e0 gi\u00f3 gi\u1eadt m\u1ea1nh.\n"
"\n"
"Theo \u00f4ng Ho\u00e0ng Ph\u00fac L\u00e2m, t\u1eeb th\u00e1ng 11/2024 \u0111\u1ebfn th\u00e1ng 1/2025, d\u00f2ng ch\u1ea3y tr\u00ean c\u00e1c s\u00f4ng khu v\u1ef1c B\u1eafc B\u1ed9 ph\u1ed5 bi\u1ebfn \u1edf m\u1ee9c x\u1ea5p x\u1ec9 ho\u1eb7c cao h\u01a1n so v\u1edbi trung b\u00ecnh nhi\u1ec1u n\u0103m t\u1eeb 10-20%, cao h\u01a1n nhi\u1ec1u t\u1ea1i h\u1ed3 Tuy\u00ean Quang (s\u00f4ng G\u00e2m) v\u00e0 Th\u00e1c B\u00e0 (s\u00f4ng Ch\u1ea3y) cao h\u01a1n trung b\u00ecnh nhi\u1ec1u n\u0103m t\u1eeb 30-50%, ri\u00eang d\u00f2ng ch\u1ea3y \u0111\u1ebfn c\u00e1c "
                        "h\u1ed3 ch\u1ee9a ch\u1ee9a l\u1edbn tr\u00ean s\u00f4ng \u0110\u00e0 thi\u1ebfu h\u1ee5t t\u1eeb 10-30% so v\u1edbi trung b\u00ecnh nhi\u1ec1u n\u0103m.\n"
"\n"
"Khu v\u1ef1c B\u1eafc Trung B\u1ed9 t\u1eeb n\u1eeda cu\u1ed1i th\u00e1ng 10 \u0111\u1ebfn th\u00e1ng 11/2024, c\u00e1c s\u00f4ng \u1edf Thanh H\u00f3a xu\u1ea5t hi\u1ec7n 1-2 \u0111\u1ee3t dao \u0111\u1ed9ng, c\u00e1c s\u00f4ng \u1edf Ngh\u1ec7 An, H\u00e0 T\u0129nh xu\u1ea5t hi\u1ec7n 1-3 \u0111\u1ee3t l\u0169; m\u1ef1c n\u01b0\u1edbc \u0111\u1ec9nh l\u0169 h\u1ea1 l\u01b0u s\u00f4ng C\u1ea3, s\u00f4ng La \u1edf m\u1ee9c b\u00e1o \u0111\u1ed9ng 1.\n"
"\n"
"V\u00f9ng ven bi\u1ec3n khu v\u1ef1c Trung B\u1ed9 v\u00e0 Nam B\u1ed9 \u0111\u1ec1 ph\u00f2ng s\u00f3ng l\u1edbn k\u1ebft h\u1ee3p v\u1edbi n\u01b0\u1edbc d\u00e2ng do \u1ea3nh h\u01b0\u1edfng c\u1ee7a b\u00e3o, \u00e1p th\u1ea5p nhi\u1ec7t \u0111\u1edbi trong th\u00e1ng 11-12, nguy c\u01a1 cao g\u00e2y s\u1ea1t l\u1edf b\u1edd s\u00f4ng, b\u1edd bi\u1ec3n. C\u00e1c t\u1ec9nh, th\u00e0nh ph\u1ed1"
                        " ven bi\u1ec3n \u0110\u00f4ng Nam B\u1ed9 c\u1ea7n \u0111\u1ec1 ph\u00f2ng c\u00e1c \u0111\u1ee3t tri\u1ec1u c\u01b0\u1eddng trong th\u1eddi gian n\u00e0y c\u00f3 kh\u1ea3 n\u0103ng g\u00e2y ng\u1eadp \u00fang c\u00e1c v\u00f9ng tr\u0169ng, th\u1ea5p, ven s\u00f4ng v\u00e0 v\u00f9ng ngo\u00e0i \u0111\u00ea bao khu v\u1ef1c n\u00e0y.\n"
"\n"
"Kh\u1ea3 n\u0103ng xu\u1ea5t hi\u1ec7n xo\u00e1y thu\u1eadn nhi\u1ec7t \u0111\u1edbi cu\u1ed1i th\u00e1ng 10\n"
"\u00d4ng Nguy\u1ec5n \u0110\u1ee9c H\u00f2a, Ph\u00f3 Tr\u01b0\u1edfng ph\u00f2ng D\u1ef1 b\u00e1o kh\u00ed h\u1eadu, Trung t\u00e2m D\u1ef1 b\u00e1o Kh\u00ed t\u01b0\u1ee3ng Th\u1ee7y v\u0103n Qu\u1ed1c gia cho bi\u1ebft, trong th\u00e1ng 10 n\u0103m 2024, b\u00e3o v\u00e0 \u00e1p th\u1ea5p nhi\u1ec7t \u0111\u1edbi tr\u00ean khu v\u1ef1c Bi\u1ec3n \u0110\u00f4ng v\u00e0 \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn \u0111\u1ea5t li\u1ec1n c\u1ee7a Vi\u1ec7t Nam c\u00f3 kh\u1ea3 n\u0103ng \u1edf m\u1ee9c x\u1ea5p x\u1ec9 \u0111\u1ebfn cao h\u01a1n so v\u1edbi trung b\u00ec"
                        "nh nhi\u1ec1u n\u0103m c\u00f9ng th\u1eddi k\u1ef3. Theo s\u1ed1 li\u1ec7u trung b\u00ecnh nhi\u1ec1u n\u0103m, trong th\u00e1ng 10 tr\u00ean Bi\u1ec3n \u0110\u00f4ng c\u00f3 2 c\u01a1n b\u00e3o, \u0111\u1ed5 b\u1ed9 v\u00e0o Vi\u1ec7t Nam 0,8 c\u01a1n.\n"
"\n"
"C\u00e1c hi\u1ec7n t\u01b0\u1ee3ng th\u1eddi ti\u1ebft nguy hi\u1ec3m nh\u01b0 b\u00e3o, kh\u00f4ng kh\u00ed l\u1ea1nh, d\u00f4ng, l\u1ed1c xo\u00e1y tr\u00ean bi\u1ec3n c\u00f3 kh\u1ea3 n\u0103ng g\u00e2y ra gi\u00f3 m\u1ea1nh, s\u00f3ng l\u1edbn \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn c\u00e1c ho\u1ea1t \u0111\u1ed9ng tr\u00ean khu v\u1ef1c Bi\u1ec3n \u0110\u00f4ng.\n"
"\n"
"Li\u00ean quan \u0111\u1ebfn d\u1ef1 b\u00e1o b\u00e3o \u1edf Bi\u1ec3n \u0110\u00f4ng, c\u00e1c m\u00f4 h\u00ecnh d\u1ef1 b\u00e1o th\u1eddi ti\u1ebft qu\u1ed1c t\u1ebf (GFS c\u1ee7a M\u1ef9, ECMWF AI c\u1ee7a ch\u00e2u \u00c2u) \u0111ang c\u00f3 nh\u1eefng d\u1ef1 b\u00e1o ph\u1ee9c t\u1ea1p v\u1ec1 c\u00e1c h\u00ecnh th\u00e1i th\u1eddi ti\u1ebft g\u00e2y m\u01b0a l\u1edbn v\u00e0"
                        " kh\u1ea3 n\u0103ng c\u00f3 b\u00e3o c\u00f9ng l\u00fac ho\u1ea1t \u0111\u1ed9ng.\n"
"\n"
"Khi n\u00e0o mi\u1ec1n B\u1eafc \u0111\u00f3n m\u01b0a d\u00f4ng, k\u1ebft th\u00fac n\u1eafng hanh?\n"
"Mi\u1ec1n B\u1eafc nhi\u1ec1u s\u01b0\u01a1ng m\u00f9, Nam B\u1ed9 ti\u1ebfp t\u1ee5c m\u01b0a d\u00f4ng\n"
"C\u1ee5c Qu\u1ea3n l\u00fd Thi\u00ean v\u0103n, \u0110\u1ecba v\u1eadt l\u00fd v\u00e0 Kh\u00ed quy\u1ec3n Philippines (PAGASA) cho hay, trong tu\u1ea7n t\u1eeb ng\u00e0y 16-22/10, d\u1ef1 ki\u1ebfn m\u1ed9t v\u00f9ng \u00e1p th\u1ea5p g\u1ea7n Bi\u1ec3n \u0110\u00f4ng s\u1ebd xu\u1ea5t hi\u1ec7n \u1edf ph\u00eda t\u00e2y khu v\u1ef1c d\u1ef1 b\u00e1o c\u1ee7a Philippines (PAR). \u00c1p th\u1ea5p \u00edt c\u00f3 kh\u1ea3 n\u0103ng m\u1ea1nh l\u00ean. Kho\u1ea3ng t\u1eeb ng\u00e0y 25-26/10 tr\u1edf \u0111i, khu v\u1ef1c ph\u00eda \u0111\u00f4ng Philippines v\u00e0 Bi\u1ec3n \u0110\u00f4ng c\u00f3 kh\u1ea3 n\u0103ng xu\u1ea5t hi\u1ec7n xo\u00e1y thu\u1eadn nhi\u1ec7t \u0111\u1edbi.\n"
"\n"
"Chuy\u00ean gia kh\u00ed"
                        " t\u01b0\u1ee3ng th\u1ee7y v\u0103n khuy\u1ebfn c\u00e1o, tr\u01b0\u1edbc c\u00e1c h\u00ecnh th\u00e1i th\u1eddi ti\u1ebft tr\u00ean, ng\u01b0\u1eddi d\u00e2n c\u1ea7n ph\u1ea3i th\u01b0\u1eddng xuy\u00ean theo d\u00f5i th\u00f4ng tin d\u1ef1 b\u00e1o, c\u1ea3nh b\u00e1o tr\u00ean website c\u1ee7a Trung t\u00e2m D\u1ef1 b\u00e1o Kh\u00ed t\u01b0\u1ee3ng Th\u1ee7y v\u0103n Qu\u1ed1c gia t\u1ea1i \u0111\u1ecba ch\u1ec9: nchmf.gov.vn, c\u00e1c \u0110\u00e0i Kh\u00ed t\u01b0\u1ee3ng Th\u1ee7y v\u0103n t\u1ec9nh, th\u00e0nh ph\u1ed1 v\u00e0 khu v\u1ef1c; \u0111\u1ed3ng th\u1eddi c\u1eadp nh\u1eadt th\u01b0\u1eddng xuy\u00ean th\u00f4ng tin d\u1ef1 b\u00e1o kh\u00ed t\u01b0\u1ee3ng th\u1ee7y v\u0103n m\u1edbi nh\u1ea5t tr\u00ean c\u00e1c ph\u01b0\u01a1ng ti\u1ec7n truy\u1ec1n th\u00f4ng \u0111\u1ea1i ch\u00fang ch\u00ednh th\u1ed1ng c\u1ee7a Trung \u01b0\u01a1ng v\u00e0 \u0111\u1ecba ph\u01b0\u01a1ng \u0111\u1ec3 ch\u1ee7 \u0111\u1ed9ng \u1ee9ng ph\u00f3.\n"
"\n"
"Ch\u00ednh quy\u1ec1n v\u00e0 c\u00e1c \u0111\u01a1n"
                        " v\u1ecb ch\u1ee9c n\u0103ng c\u1ea7n cung c\u1ea5p nhanh, k\u1ecbp th\u1eddi th\u00f4ng tin d\u1ef1 b\u00e1o thi\u00ean tai cho ng\u01b0\u1eddi d\u00e2n, v\u1eadn \u0111\u1ed9ng, tuy\u00ean truy\u1ec1n c\u0169ng nh\u01b0 th\u1ef1c hi\u1ec7n l\u1ec7nh c\u1ea5m tuy\u1ec7t \u0111\u1ed1i ng\u01b0\u1eddi d\u00e2n ho\u1ea1t \u0111\u1ed9ng t\u1ea1i c\u00e1c khu v\u1ef1c c\u00f3 nguy c\u01a1 r\u1ee7i ro cao d\u1ec5 x\u1ea3y ra d\u00f4ng, l\u1ed1c, s\u00e9t, m\u01b0a \u0111\u00e1... Ng\u01b0\u1eddi d\u00e2n c\u1ea7n tu\u00e2n th\u1ee7 ch\u1eb7t ch\u1ebd h\u01b0\u1edbng d\u1eabn c\u00f4ng t\u00e1c \u1ee9ng ph\u00f3, ph\u00f2ng tr\u00e1nh thi\u00ean tai c\u1ee7a ch\u00ednh quy\u1ec1n \u0111\u1ecba ph\u01b0\u01a1ng.\n"
"\n"
"C\u01a1 quan kh\u00ed t\u01b0\u1ee3ng l\u01b0u \u00fd c\u00e1c b\u1ea3n tin c\u1ea3nh b\u00e1o th\u1eddi h\u1ea1n xa th\u01b0\u1eddng mang t\u00ednh ch\u1ea5t d\u1ef1 b\u00e1o xu th\u1ebf. V\u00ec v\u1eady, \u0111\u1ec3 th\u00f4ng tin d\u1ef1 b\u00e1o th\u1eddi ti\u1ebft c\u00f3 c\u01a1 s\u1edf cao h"
                        "\u01a1n, ng\u01b0\u1eddi d\u00e2n n\u00ean \u0111\u00f3n \u0111\u1ee3i nh\u1eefng b\u1ea3n tin th\u1eddi h\u1ea1n ng\u1eafn \u0111\u01b0\u1ee3c ph\u00e1t h\u00e0nh h\u1eb1ng ng\u00e0y t\u1eeb Trung t\u00e2m D\u1ef1 b\u00e1o Kh\u00ed t\u01b0\u1ee3ng Th\u1ee7y v\u0103n Qu\u1ed1c gia.", None))
        self.label_16.setText("")
        self.LoginLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome back!", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lgPSignIn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lgPSignUp.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.LoginLabel_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to 9.5Health", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"StudentID", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.confrim.setText("")
        self.rgPSignIn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.rgPSignUp.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ti\u1ec1n s\u1eed b\u1ec7nh \u00e1n", None))
        self.presick.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: Vi\u00eam ph\u1ed5i, \u0111au tim... etc )", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"C\u00e1c tri\u1ec7u ch\u1ee9ng hi\u1ec7n t\u1ea1i", None))
        self.nowProb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: Ho, s\u1ed1t, bu\u1ed3n n\u00f4n, kh\u00f3 th\u1edf,... etc )", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"M\u1ee9c \u0111\u1ed9 \u1ea3nh h\u01b0\u1edfng c\u1ee7a c\u00e1c tri\u1ec7u ch\u1ee9ng \u0111\u1ebfn cu\u1ed9c s\u1ed1ng h\u1eb1ng ng\u00e0y c\u1ee7a b\u1ea1n nh\u01b0 th\u1ebf n\u00e0o?", None))
        self.Affected.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: Kh\u00f4ng th\u1ec3 t\u1eadp trung l\u00e0m vi\u1ec7c, kh\u00e1 \u1ea3nh h\u01b0\u1edfng,... etc )", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"B\u1ea1n \u0111\u00e3 th\u1ef1c hi\u1ec7n bi\u1ec7n ph\u00e1p n\u00e0o \u0111\u1ec3 c\u1ea3i thi\u1ec7n tri\u1ec7u tr\u1ee9ng ch\u01b0a?", None))
        self.Improved.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: T\u1eadp th\u1ec3 d\u1ee5c bu\u1ed5i s\u00e1ng, \u0103n th\u1ef1c ph\u1ea9m gi\u00e0u Vitamin C,... etc )", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ngo\u00e0i nh\u1eefng th\u00f4ng tin \u0111\u00e3 cung c\u1ea5p, b\u1ea1n c\u00f2n lo ng\u1ea1i v\u1ec1 v\u1ea5n \u0111\u1ec1 s\u1ee9c kh\u1ecfe n\u00e0o kh\u00e1c kh\u00f4ng?", None))
        self.Others.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: D\u1ecbch s\u1ed1t xu\u1ea5t huy\u1ebft, d\u1ecbch covid, thu\u1ed1c ch\u1eefa tr\u1ecb ung th\u01b0,... etc )", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"B\u1ea1n mong mu\u1ed1n nh\u1eadn \u0111\u01b0\u1ee3c s\u1ef1 h\u1ed7 tr\u1ee3 g\u00ec t\u1eeb ch\u00fang t\u00f4i li\u00ean quan \u0111\u1ebfn t\u00ecnh tr\u1ea1ng s\u1ee9c kh\u1ecfe hi\u1ec7n t\u1ea1i?", None))
        self.Brief.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng (.ex: Ch\u1ebf \u0111\u1ed9 \u0103n u\u1ed1ng, t\u00ecnh h\u00ecnh d\u1ecbch, c\u1ee5 th\u1ec3 m\u1ee9c Kcal c\u1ea7n n\u1ea1p m\u1ed7i ng\u00e0y,... etc )", None))
        self.sendSurvey.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_46.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Information ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd", None))
        self.firstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nguy\u1ec5n V\u0103n", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None))
        self.lastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None))
        self.sexual.setItemText(0, "")
        self.sexual.setItemText(1, QCoreApplication.translate("MainWindow", u"Nam", None))
        self.sexual.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.sexual.setItemText(3, QCoreApplication.translate("MainWindow", u"Kh\u00e1c", None))

        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None))
        self.dateOfBirth.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.address.setText("")
        self.address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vinhomes Grandpark, TP. Th\u1ee7 \u0110\u1ee9c, TP. HCM, Vi\u1ec7t Nam", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Phone No.", None))
        self.phoneNumber.setInputMask("")
        self.phoneNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0908152508", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Body ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.height.setPlaceholderText(QCoreApplication.translate("MainWindow", u".ex 160 cm", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u".ex 60kg", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Body Temperature (Update later)", None))
        self.goToUpdate.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<username> Infomation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Information  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None))
        self.inpSexual.setItemText(0, "")
        self.inpSexual.setItemText(1, QCoreApplication.translate("MainWindow", u"Nam", None))
        self.inpSexual.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.inpSexual.setItemText(3, QCoreApplication.translate("MainWindow", u"Kh\u00e1c", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None))
        self.inpDateOfBirth.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Phone No.", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Body  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Body Temperature (Update later)", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.logo.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Author by Syneras", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.pushButton_15.setText("")
    # retranslateUi

