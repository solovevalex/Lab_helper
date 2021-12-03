# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View_final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 719)

        """Создание всего..."""
        self.create_main()
        self.create_menu_Bar()
        self.create_ecxel_fail()
        self.create_mis()
        self.create_graphics()
        self.create_graphics_add()

        """Выполняется занесение в главное окно"""
        self.retranslateUi(MainWindow)
        self.menu.setCurrentIndex(1)
        self.menu_graphics.setCurrentIndex(1)

        """устанавливается menubar, centralwidget"""
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menuBar)

        """Воссоединение всего!"""
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_ecxel_fail(self):
        self.ecxel_fail = QtWidgets.QWidget()
        self.ecxel_fail.setObjectName("ecxel_fail")
        self.label_ex = QtWidgets.QLabel(self.ecxel_fail)
        self.label_ex.setGeometry(QtCore.QRect(330, 30, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ex.setFont(font)
        self.label_ex.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_ex.setObjectName("label_ex")
        self.text_ex = QtWidgets.QTextEdit(self.ecxel_fail)
        self.text_ex.setGeometry(QtCore.QRect(250, 130, 541, 51))
        self.text_ex.setObjectName("text_ex")
        self.btn_ex = QtWidgets.QPushButton(self.ecxel_fail)
        self.btn_ex.setGeometry(QtCore.QRect(390, 220, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ex.setFont(font)
        self.btn_ex.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_ex.setObjectName("btn_ex")
        self.menu.addTab(self.ecxel_fail, "")

    def create_graphics(self):
        self.graphics = QtWidgets.QWidget()
        self.graphics.setObjectName("graphics")
        self.menu_graphics = QtWidgets.QTabWidget(self.graphics)
        self.menu_graphics.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.menu_graphics.setObjectName("menu_graphics")
        self.graphics_main = QtWidgets.QWidget()
        self.graphics_main.setObjectName("graphics_main")
        self.label_graph_high_1 = QtWidgets.QLabel(self.graphics_main)
        self.label_graph_high_1.setGeometry(QtCore.QRect(350, 10, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_high_1.setFont(font)
        self.label_graph_high_1.setObjectName("label_graph_high_1")
        self.label_graphics_high_3 = QtWidgets.QLabel(self.graphics_main)
        self.label_graphics_high_3.setGeometry(QtCore.QRect(100, 140, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_high_3.setFont(font)
        self.label_graphics_high_3.setObjectName("label_graphics_high_3")
        self.label_graph_X_1 = QtWidgets.QLabel(self.graphics_main)
        self.label_graph_X_1.setGeometry(QtCore.QRect(380, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_X_1.setFont(font)
        self.label_graph_X_1.setObjectName("label_graph_X_1")
        self.label_graphics_Y_1 = QtWidgets.QLabel(self.graphics_main)
        self.label_graphics_Y_1.setGeometry(QtCore.QRect(380, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_Y_1.setFont(font)
        self.label_graphics_Y_1.setObjectName("label_graphics_Y_1")
        self.label_label_high_5 = QtWidgets.QLabel(self.graphics_main)
        self.label_label_high_5.setGeometry(QtCore.QRect(240, 410, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_label_high_5.setFont(font)
        self.label_label_high_5.setObjectName("label_label_high_5")
        self.formula_graph_1 = QtWidgets.QLabel(self.graphics_main)
        self.formula_graph_1.setGeometry(QtCore.QRect(90, 450, 821, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph_1.setFont(font)
        self.formula_graph_1.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.formula_graph_1.setObjectName("formula_graph_1")
        self.check_mistake_1 = QtWidgets.QCheckBox(self.graphics_main)
        self.check_mistake_1.setGeometry(QtCore.QRect(250, 300, 131, 20))
        self.check_mistake_1.setObjectName("check_mistake_1")
        self.check_zero_1 = QtWidgets.QCheckBox(self.graphics_main)
        self.check_zero_1.setGeometry(QtCore.QRect(430, 300, 131, 20))
        self.check_zero_1.setObjectName("check_zero_1")
        self.check_extremum_1 = QtWidgets.QCheckBox(self.graphics_main)
        self.check_extremum_1.setGeometry(QtCore.QRect(600, 300, 131, 20))
        self.check_extremum_1.setObjectName("check_extremum_1")
        self.label_graph_high_4 = QtWidgets.QLabel(self.graphics_main)
        self.label_graph_high_4.setGeometry(QtCore.QRect(340, 270, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_high_4.setFont(font)
        self.label_graph_high_4.setObjectName("label_graph_high_4")
        self.btn_start_graph_1 = QtWidgets.QPushButton(self.graphics_main)
        self.btn_start_graph_1.setGeometry(QtCore.QRect(390, 340, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start_graph_1.setFont(font)
        self.btn_start_graph_1.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.btn_start_graph_1.setObjectName("btn_start_graph_1")
        self.formula_graph_need_1 = QtWidgets.QTextEdit(self.graphics_main)
        self.formula_graph_need_1.setGeometry(QtCore.QRect(100, 40, 801, 87))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph_need_1.setFont(font)
        self.formula_graph_need_1.setObjectName("formula_graph_need_1")
        self.point_X_1 = QtWidgets.QPlainTextEdit(self.graphics_main)
        self.point_X_1.setGeometry(QtCore.QRect(100, 170, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_X_1.setFont(font)
        self.point_X_1.setObjectName("point_X_1")
        self.point_Y_1 = QtWidgets.QPlainTextEdit(self.graphics_main)
        self.point_Y_1.setGeometry(QtCore.QRect(100, 210, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_Y_1.setFont(font)
        self.point_Y_1.setObjectName("point_Y_1")
        self.btn_add_graph_1 = QtWidgets.QPushButton(self.graphics_main)
        self.btn_add_graph_1.setGeometry(QtCore.QRect(200, 560, 261, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_graph_1.setFont(font)
        self.btn_add_graph_1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_add_graph_1.setObjectName("btn_add_graph_1")
        self.btn_new_graph_1 = QtWidgets.QPushButton(self.graphics_main)
        self.btn_new_graph_1.setGeometry(QtCore.QRect(540, 560, 261, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_new_graph_1.setFont(font)
        self.btn_new_graph_1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_new_graph_1.setObjectName("btn_new_graph_1")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.graphics_main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(500, 140, 401, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horisontalCorrect_lbl_gr = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horisontalCorrect_lbl_gr.setContentsMargins(0, 0, 0, 0)
        self.horisontalCorrect_lbl_gr.setObjectName("horisontalCorrect_lbl_gr")
        self.label_graph_paint_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_paint_1.setFont(font)
        self.label_graph_paint_1.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.label_graph_paint_1.setObjectName("label_graph_paint_1")
        self.horisontalCorrect_lbl_gr.addWidget(self.label_graph_paint_1)
        self.label_graph_paint_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_paint_2.setFont(font)
        self.label_graph_paint_2.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.label_graph_paint_2.setObjectName("label_graph_paint_2")
        self.horisontalCorrect_lbl_gr.addWidget(self.label_graph_paint_2)
        self.label_graph_paint_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_paint_3.setFont(font)
        self.label_graph_paint_3.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.label_graph_paint_3.setObjectName("label_graph_paint_3")
        self.horisontalCorrect_lbl_gr.addWidget(self.label_graph_paint_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.graphics_main)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(500, 180, 401, 89))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_graph_label_g = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_graph_label_g.setFont(font)
        self.text_graph_label_g.setObjectName("text_graph_label_g")
        self.horizontalLayout_2.addWidget(self.text_graph_label_g)
        self.text_graph_label_x = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_graph_label_x.setFont(font)
        self.text_graph_label_x.setObjectName("text_graph_label_x")
        self.horizontalLayout_2.addWidget(self.text_graph_label_x)
        self.text_graph_label_y = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_graph_label_y.setFont(font)
        self.text_graph_label_y.setObjectName("text_graph_label_y")
        self.horizontalLayout_2.addWidget(self.text_graph_label_y)
        self.menu_graphics.addTab(self.graphics_main, "")

    def create_graphics_add(self):
        self.graph_2 = QtWidgets.QWidget()
        self.graph_2.setObjectName("graph_2")
        self.label_graph_high_7 = QtWidgets.QLabel(self.graph_2)
        self.label_graph_high_7.setGeometry(QtCore.QRect(320, 10, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_high_7.setFont(font)
        self.label_graph_high_7.setObjectName("label_graph_high_7")
        self.formula_graph_need_4 = QtWidgets.QTextEdit(self.graph_2)
        self.formula_graph_need_4.setGeometry(QtCore.QRect(80, 40, 801, 87))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph_need_4.setFont(font)
        self.formula_graph_need_4.setObjectName("formula_graph_need_4")
        self.label_graphics_high_6 = QtWidgets.QLabel(self.graph_2)
        self.label_graphics_high_6.setGeometry(QtCore.QRect(310, 140, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_high_6.setFont(font)
        self.label_graphics_high_6.setObjectName("label_graphics_high_6")
        self.point_X_4 = QtWidgets.QPlainTextEdit(self.graph_2)
        self.point_X_4.setGeometry(QtCore.QRect(310, 230, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_X_4.setFont(font)
        self.point_X_4.setObjectName("point_X_4")
        self.point_Y_4 = QtWidgets.QPlainTextEdit(self.graph_2)
        self.point_Y_4.setGeometry(QtCore.QRect(310, 180, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_Y_4.setFont(font)
        self.point_Y_4.setObjectName("point_Y_4")
        self.label_graph_X_4 = QtWidgets.QLabel(self.graph_2)
        self.label_graph_X_4.setGeometry(QtCore.QRect(580, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_X_4.setFont(font)
        self.label_graph_X_4.setObjectName("label_graph_X_4")
        self.label_graphics_Y_4 = QtWidgets.QLabel(self.graph_2)
        self.label_graphics_Y_4.setGeometry(QtCore.QRect(580, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_Y_4.setFont(font)
        self.label_graphics_Y_4.setObjectName("label_graphics_Y_4")
        self.label_label_high_8 = QtWidgets.QLabel(self.graph_2)
        self.label_label_high_8.setGeometry(QtCore.QRect(200, 290, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_label_high_8.setFont(font)
        self.label_label_high_8.setObjectName("label_label_high_8")
        self.formula_graph_4 = QtWidgets.QLabel(self.graph_2)
        self.formula_graph_4.setGeometry(QtCore.QRect(70, 350, 821, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph_4.setFont(font)
        self.formula_graph_4.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.formula_graph_4.setObjectName("formula_graph_4")
        self.menu_graphics.addTab(self.graph_2, "")
        self.menu.addTab(self.graphics, "")

    def create_mis(self):
        self.mistakes = QtWidgets.QWidget()
        self.mistakes.setObjectName("mistakes")
        self.label_mis_high_1 = QtWidgets.QLabel(self.mistakes)
        self.label_mis_high_1.setGeometry(QtCore.QRect(290, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mis_high_1.setFont(font)
        self.label_mis_high_1.setObjectName("label_mis_high_1")
        self.label_mis_high_2 = QtWidgets.QLabel(self.mistakes)
        self.label_mis_high_2.setGeometry(QtCore.QRect(180, 130, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mis_high_2.setFont(font)
        self.label_mis_high_2.setObjectName("label_mis_high_2")
        self.label_mis_high_5 = QtWidgets.QLabel(self.mistakes)
        self.label_mis_high_5.setGeometry(QtCore.QRect(310, 310, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mis_high_5.setFont(font)
        self.label_mis_high_5.setObjectName("label_mis_high_5")
        self.number_mistake = QtWidgets.QLabel(self.mistakes)
        self.number_mistake.setGeometry(QtCore.QRect(260, 530, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.number_mistake.setFont(font)
        self.number_mistake.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.number_mistake.setObjectName("number_mistake")
        self.mistake_name_const = QtWidgets.QTextEdit(self.mistakes)
        self.mistake_name_const.setGeometry(QtCore.QRect(240, 160, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mistake_name_const.setFont(font)
        self.mistake_name_const.setObjectName("mistake_name_const")
        self.formula_mistake_need = QtWidgets.QTextEdit(self.mistakes)
        self.formula_mistake_need.setGeometry(QtCore.QRect(240, 50, 501, 87))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_mistake_need.setFont(font)
        self.formula_mistake_need.setObjectName("formula_mistake_need")
        self.label_small_1 = QtWidgets.QLabel(self.mistakes)
        self.label_small_1.setGeometry(QtCore.QRect(150, 370, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_small_1.setFont(font)
        self.label_small_1.setObjectName("label_small_1")
        self.label_small_2 = QtWidgets.QLabel(self.mistakes)
        self.label_small_2.setGeometry(QtCore.QRect(410, 370, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_small_2.setFont(font)
        self.label_small_2.setObjectName("label_small_2")
        self.label_small_3 = QtWidgets.QLabel(self.mistakes)
        self.label_small_3.setGeometry(QtCore.QRect(690, 370, 161, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_small_3.setFont(font)
        self.label_small_3.setObjectName("label_small_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.mistakes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 390, 821, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horisontalCorrect_mis = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horisontalCorrect_mis.setContentsMargins(0, 0, 0, 0)
        self.horisontalCorrect_mis.setObjectName("horisontalCorrect_mis")
        self.text_mistake_const = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_mistake_const.setFont(font)
        self.text_mistake_const.setPlainText("")
        self.text_mistake_const.setObjectName("text_mistake_const")
        self.horisontalCorrect_mis.addWidget(self.text_mistake_const)
        self.text_mistake_var_middle = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_mistake_var_middle.setFont(font)
        self.text_mistake_var_middle.setPlainText("")
        self.text_mistake_var_middle.setObjectName("text_mistake_var_middle")
        self.horisontalCorrect_mis.addWidget(self.text_mistake_var_middle)
        self.text_mistake_var_deviation = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_mistake_var_deviation.setFont(font)
        self.text_mistake_var_deviation.setPlainText("")
        self.text_mistake_var_deviation.setObjectName("text_mistake_var_deviation")
        self.horisontalCorrect_mis.addWidget(self.text_mistake_var_deviation)
        self.btn_mis_getFormula = QtWidgets.QPushButton(self.mistakes)
        self.btn_mis_getFormula.setGeometry(QtCore.QRect(610, 160, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_mis_getFormula.setFont(font)
        self.btn_mis_getFormula.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.btn_mis_getFormula.setObjectName("btn_mis_getFormula")
        self.formula_mistake = QtWidgets.QLabel(self.mistakes)
        self.formula_mistake.setGeometry(QtCore.QRect(180, 210, 691, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.formula_mistake.setFont(font)
        self.formula_mistake.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.formula_mistake.setObjectName("formula_mistake")
        self.btn_mis_getFigure = QtWidgets.QPushButton(self.mistakes)
        self.btn_mis_getFigure.setGeometry(QtCore.QRect(370, 480, 251, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_mis_getFigure.setFont(font)
        self.btn_mis_getFigure.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_mis_getFigure.setObjectName("btn_mis_getFigure")
        self.btn_mis_new = QtWidgets.QPushButton(self.mistakes)
        self.btn_mis_new.setGeometry(QtCore.QRect(360, 610, 271, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_mis_new.setFont(font)
        self.btn_mis_new.setStyleSheet("\n"
"background-color: rgb(255, 85, 0);")
        self.btn_mis_new.setObjectName("btn_mis_new")
        self.menu.addTab(self.mistakes, "")

    def create_main(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.menu = QtWidgets.QTabWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.menu.setObjectName("menu")

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menuBar.setObjectName("menuBar")

    def create_menu_Bar(self):
        self.menu_btn = QtWidgets.QMenu(self.menuBar)
        self.menu_btn.setObjectName("menu_btn")
        self.menuBar.addAction(self.menu_btn.menuAction())


        # self.action_2 = QtWidgets.QAction(MainWindow)
        # self.action_2.setObjectName("action_2")
        # self.action_3 = QtWidgets.QAction(MainWindow)
        # self.action_3.setObjectName("action_3")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ex.setText(_translate("MainWindow", "Введите полный путь к Excel файлу,\n"
"с которым вы собираетесь работать\n"
"(из этого файла будут считываться данные\n"
"указанные через индексы)"))
        self.btn_ex.setText(_translate("MainWindow", "Работать с этим файлом!"))
        self.menu.setTabText(self.menu.indexOf(self.ecxel_fail), _translate("MainWindow", "Выбор excel файла"))
        self.label_graph_high_1.setText(_translate("MainWindow", "введите формулу для графика:"))
        self.label_graphics_high_3.setText(_translate("MainWindow", "введите данные(точки графика):"))
        self.label_graph_X_1.setText(_translate("MainWindow", "x"))
        self.label_graphics_Y_1.setText(_translate("MainWindow", "y"))
        self.label_label_high_5.setText(_translate("MainWindow", "здесь вы получите формулу приближенного графика"))
        self.formula_graph_1.setText(_translate("MainWindow", "формула для вашего графика:"))
        self.check_mistake_1.setText(_translate("MainWindow", "Хочу погрешность"))
        self.check_zero_1.setText(_translate("MainWindow", "Хочу нули ф-ии"))
        self.check_extremum_1.setText(_translate("MainWindow", "хочу экстремумы"))
        self.label_graph_high_4.setText(_translate("MainWindow", "добавьте галочки, если нужно"))
        self.btn_start_graph_1.setText(_translate("MainWindow", "Получить график!"))
        self.btn_add_graph_1.setText(_translate("MainWindow", "хочу добавить график\n"
"в те же координатные оси"))
        self.btn_new_graph_1.setText(_translate("MainWindow", "Хочу создавать новый график.\n"
"Соглашаюсь удалить\n"
"предыдущие мои графики"))
        self.label_graph_paint_1.setText(_translate("MainWindow", "подпись к графику"))
        self.label_graph_paint_2.setText(_translate("MainWindow", "  подись к оси x"))
        self.label_graph_paint_3.setText(_translate("MainWindow", "  подпись к оси y"))
        self.menu_graphics.setTabText(self.menu_graphics.indexOf(self.graphics_main), _translate("MainWindow", "главный график"))
        self.label_graph_high_7.setText(_translate("MainWindow", "введите формулу для графика:"))
        self.label_graphics_high_6.setText(_translate("MainWindow", "введите данные(точки графика):"))
        self.label_graph_X_4.setText(_translate("MainWindow", "x"))
        self.label_graphics_Y_4.setText(_translate("MainWindow", "y"))
        self.label_label_high_8.setText(_translate("MainWindow", "здесь вы получите формулу приближенного графика"))
        self.formula_graph_4.setText(_translate("MainWindow", "формула для вашего графика:"))
        self.menu_graphics.setTabText(self.menu_graphics.indexOf(self.graph_2), _translate("MainWindow", "график 2"))
        self.menu.setTabText(self.menu.indexOf(self.graphics), _translate("MainWindow", "графики"))
        self.label_mis_high_1.setText(_translate("MainWindow", "введите формулу для величины, \n"
"погрешность которой вы хотите посчитать"))
        self.label_mis_high_2.setText(_translate("MainWindow", "укажите, какие буквы являются константой"))
        self.label_mis_high_5.setText(_translate("MainWindow", "если хотите получить числовое значение,\n"
"введите числовые значения переменных и констант"))
        self.number_mistake.setText(_translate("MainWindow", "Здесь вы получите числовое значение:"))
        self.label_small_1.setText(_translate("MainWindow", "значение констант"))
        self.label_small_2.setText(_translate("MainWindow", "среднее переменной"))
        self.label_small_3.setText(_translate("MainWindow", "среднекв. отклонение"))
        self.btn_mis_getFormula.setText(_translate("MainWindow", "Получить формулу погрешности"))
        self.formula_mistake.setText(_translate("MainWindow", "Здесь вы получите формулу погрешности:"))
        self.btn_mis_getFigure.setText(_translate("MainWindow", "Получить числовое значение"))
        self.btn_mis_new.setText(_translate("MainWindow", "Обновить окно!"))
        self.menu.setTabText(self.menu.indexOf(self.mistakes), _translate("MainWindow", "Погрешности"))
        self.menu_btn.setTitle(_translate("MainWindow", "Справка"))
        # self.action_2.setText(_translate("MainWindow", "О программе"))
        # self.action_3.setText(_translate("MainWindow", "проапроап"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
