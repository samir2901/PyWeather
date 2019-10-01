from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 501)
        MainWindow.setMinimumSize(QtCore.QSize(393, 501))
        MainWindow.setMaximumSize(QtCore.QSize(393, 501))
        MainWindow.setStyleSheet("background-color: rgb(255, 188, 167);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cityName_lbl = QtWidgets.QLabel(self.centralwidget)
        self.cityName_lbl.setGeometry(QtCore.QRect(20, 20, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.cityName_lbl.setFont(font)
        self.cityName_lbl.setStyleSheet("background-color: rgb(255, 188, 167);")
        self.cityName_lbl.setObjectName("cityName_lbl")
        self.cityName = QtWidgets.QLineEdit(self.centralwidget)
        self.cityName.setGeometry(QtCore.QRect(20, 40, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cityName.setFont(font)
        self.cityName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cityName.setObjectName("cityName")
        self.weatherReport_lbl = QtWidgets.QLabel(self.centralwidget)
        self.weatherReport_lbl.setGeometry(QtCore.QRect(20, 160, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.weatherReport_lbl.setFont(font)
        self.weatherReport_lbl.setStyleSheet("background-color: rgb(255, 188, 167);")
        self.weatherReport_lbl.setObjectName("weatherReport_lbl")
        self.weatherReport = QtWidgets.QTextEdit(self.centralwidget)
        self.weatherReport.setGeometry(QtCore.QRect(20, 180, 351, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weatherReport.setFont(font)
        self.weatherReport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weatherReport.setObjectName("weatherReport")
        self.weatherReport.setReadOnly(True)
        self.GetReport = QtWidgets.QPushButton(self.centralwidget)
        self.GetReport.setGeometry(QtCore.QRect(70, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.GetReport.setFont(font)
        self.GetReport.setStyleSheet("background-color: rgb(244, 52, 4);")
        self.GetReport.setObjectName("GetReport")
        self.GetReport.clicked.connect(self.weather)

        self.New = QtWidgets.QPushButton(self.centralwidget)
        self.New.setGeometry(QtCore.QRect(230, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(11)
        self.New.setFont(font)
        self.New.setStyleSheet("background-color: rgb(244, 52, 4);")
        self.New.setObjectName("New")
        self.New.clicked.connect(self.new)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyWeather"))
        self.cityName_lbl.setText(_translate("MainWindow", "Enter the name of the city"))
        self.weatherReport_lbl.setText(_translate("MainWindow", "Weather Report"))
        self.GetReport.setText(_translate("MainWindow", "Get Report"))
        self.New.setText(_translate("MainWindow", "New"))

    def weather(self):
        city = self.cityName.text()
        url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22" .format(city)
        try:
            res = requests.get(url)
            output = res.json()
            weatherStatus = output["weather"][0]["description"]
            temperature = output["main"]["temp"]
            humidity = output["main"]["humidity"]
            txt = "Weather Status: " + str(weatherStatus) + "\nTemperature: " + str(temperature) + " degrees C" + "\nHumidity: " + str(humidity) + "%"
            self.weatherReport.setText(txt)
        except:
            txt = "Oops!! Sorry try again"
            self.weatherReport.setText(txt)

    def new(self):
        self.cityName.clear()
        self.weatherReport.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
