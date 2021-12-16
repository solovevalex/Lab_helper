from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import re
import Function_Plotting_Graph as ann_func
import Indirect_measurements_error as sonya_func

# Здесь объявлю возможные имена для дополнительных графических окон
names_start = ['график 2', 'график 3', 'график 4', 'график 5', 'график 6', 'график 7', 'график 8', 'график 9',
               'график 10']
names_use = ['график 2', 'график 3', 'график 4', 'график 5', 'график 6', 'график 7', 'график 8', 'график 9',
             'график 10']
value_use = dict(graph_2=0, graph_3=0, graph_4=0, graph_5=0, graph_6=0, graph_7=0, graph_8=0, graph_9=0, graph_10=0)
value_names = ['graph_1', 'graph_2', 'graph_3', 'graph_4', 'graph_5', 'graph_6', 'graph_7', 'graph_8',
               'graph_9', 'graph_10']
str_exp = ""


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("спаравка")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)


class add_graph():
    def __init__(self, name):
        self.graph = QtWidgets.QWidget()
        self.graph.setObjectName("name")

        self.label_graph_high_1 = QtWidgets.QLabel(self.graph)
        self.label_graph_high_1.setGeometry(QtCore.QRect(320, 10, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_high_1.setFont(font)
        self.label_graph_high_1.setObjectName("label_graph_high_1")
        self.formula_graph_need = QtWidgets.QTextEdit(self.graph)
        self.formula_graph_need.setGeometry(QtCore.QRect(80, 40, 801, 87))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph_need.setFont(font)
        self.formula_graph_need.setObjectName("formula_graph_need")
        self.label_graphics_high_2 = QtWidgets.QLabel(self.graph)
        self.label_graphics_high_2.setGeometry(QtCore.QRect(310, 140, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_high_2.setFont(font)
        self.label_graphics_high_2.setObjectName("label_graphics_high_2")
        self.point_Y = QtWidgets.QTextEdit(self.graph)
        self.point_Y.setGeometry(QtCore.QRect(310, 230, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_Y.setFont(font)
        self.point_Y.setObjectName("point_Y")
        self.point_X = QtWidgets.QTextEdit(self.graph)
        self.point_X.setGeometry(QtCore.QRect(310, 180, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_X.setFont(font)
        self.point_X.setObjectName("point_X")
        self.label_graph_X = QtWidgets.QLabel(self.graph)
        self.label_graph_X.setGeometry(QtCore.QRect(580, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_X.setFont(font)
        self.label_graph_X.setObjectName("label_graph_X")
        self.label_graphics_Y = QtWidgets.QLabel(self.graph)
        self.label_graphics_Y.setGeometry(QtCore.QRect(580, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_Y.setFont(font)
        self.label_graphics_Y.setObjectName("label_graphics_Y")

        self.formula_graph = QtWidgets.QLabel(self.graph)
        self.formula_graph.setGeometry(QtCore.QRect(70, 350, 821, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.formula_graph.setFont(font)
        self.formula_graph.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.formula_graph.setObjectName("formula_graph")

        _translate = QtCore.QCoreApplication.translate
        self.label_graph_high_1.setText(_translate("MainWindow", "введите формулу для графика:"))
        self.label_graphics_high_2.setText(_translate("MainWindow", "введите данные(точки графика):"))
        self.label_graph_X.setText(_translate("MainWindow", "x"))
        self.label_graphics_Y.setText(_translate("MainWindow", "y"))

        self.formula_graph.setText(_translate("MainWindow", 'Для запуска вернитесь во вкладку "главный график".'))


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 719)
        """Создание всего..."""
        self.create_main()
        self.create_menu_Bar()
        # self.create_ecxel_fail()
        self.create_mis()
        self.create_graphics()

        """Выполняется занесение в главное окно"""
        self.retranslateUi(MainWindow)
        self.menu.setCurrentIndex(0)
        self.menu_graphics.setCurrentIndex(0)

        """устанавливается menubar, centralwidget"""
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menuBar)

        """Воссоединение всего!"""
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

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
        self.label_graph_X_1.setGeometry(QtCore.QRect(910, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_X_1.setFont(font)
        self.label_graph_X_1.setObjectName("label_graph_X_1")
        self.label_graphics_Y_1 = QtWidgets.QLabel(self.graphics_main)
        self.label_graphics_Y_1.setGeometry(QtCore.QRect(910, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_graphics_Y_1.setFont(font)
        self.label_graphics_Y_1.setObjectName("label_graphics_Y_1")
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
        self.btn_start_graph_1.setGeometry(QtCore.QRect(390, 460, 191, 51))
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
        self.point_X_1 = QtWidgets.QTextEdit(self.graphics_main)
        self.point_X_1.setGeometry(QtCore.QRect(100, 170, 801, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_X_1.setFont(font)
        self.point_X_1.setObjectName("point_X_1")
        self.point_Y_1 = QtWidgets.QTextEdit(self.graphics_main)
        self.point_Y_1.setGeometry(QtCore.QRect(100, 210, 801, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point_Y_1.setFont(font)
        self.point_Y_1.setObjectName("point_Y_1")

        self.btn_add_graph_1 = QtWidgets.QPushButton(self.graphics_main)
        self.btn_add_graph_1.setGeometry(QtCore.QRect(290, 400, 191, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_graph_1.setFont(font)
        self.btn_add_graph_1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_add_graph_1.setObjectName("btn_add_graph_1")

        self.btn_clear_graph = QtWidgets.QPushButton(self.graphics_main)
        self.btn_clear_graph.setGeometry(QtCore.QRect(390, 560, 191, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_graph.setFont(font)
        self.btn_clear_graph.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_clear_graph.setObjectName("btn_clear_graph")

        self.btn_new_graph_1 = QtWidgets.QPushButton(self.graphics_main)
        self.btn_new_graph_1.setGeometry(QtCore.QRect(500, 400, 191, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_new_graph_1.setFont(font)
        self.btn_new_graph_1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_new_graph_1.setObjectName("btn_new_graph_1")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.graphics_main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(290, 329, 401, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horisontalCorrect_lbl_gr = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horisontalCorrect_lbl_gr.setContentsMargins(0, 0, 0, 0)
        self.horisontalCorrect_lbl_gr.setObjectName("horisontalCorrect_lbl_gr")
        self.label_graph_paint_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_graph_paint_1.setFont(font)
        self.label_graph_paint_1.setStyleSheet("background-color: rgb(170, 85, 255);")
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
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(290, 360, 401, 31))
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

        self.number_mistake = QtWidgets.QTextEdit(self.mistakes)
        self.number_mistake.setGeometry(QtCore.QRect(260, 530, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.number_mistake.setFont(font)
        self.number_mistake.setObjectName("number_mistake")
        self.number_mistake.setStyleSheet("background-color: rgb(255, 255, 127);")

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
        self.text_mistake_const = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_mistake_const.setFont(font)
        self.text_mistake_const.setPlainText("")
        self.text_mistake_const.setObjectName("text_mistake_const")
        self.horisontalCorrect_mis.addWidget(self.text_mistake_const)
        self.text_mistake_var_middle = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text_mistake_var_middle.setFont(font)
        self.text_mistake_var_middle.setPlainText("")
        self.text_mistake_var_middle.setObjectName("text_mistake_var_middle")
        self.horisontalCorrect_mis.addWidget(self.text_mistake_var_middle)
        self.text_mistake_var_deviation = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
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
        self.formula_mistake = QtWidgets.QTextEdit(self.mistakes)
        self.formula_mistake.setGeometry(QtCore.QRect(180, 210, 691, 87))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.formula_mistake.setFont(font)
        self.formula_mistake.setObjectName("formula_mistake")
        self.formula_mistake.setStyleSheet("background-color: rgb(255, 170, 0);")

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
        self.menuBar.addMenu(self.menu_btn)
        self.menu_btn.addAction('Справка', self.action_clicked)

    def action_clicked(self):
        error = QMessageBox()
        error.setWindowTitle("Справка")
        error.setText("Приветствую вас в нашем приложении!!!")
        error.setIcon(QMessageBox.Information)
        error.setStandardButtons(QMessageBox.Ok)

        error.setDefaultButton(QMessageBox.Ok)
        error.setInformativeText("Нажмите на Show Details, чтобы узнать детали")
        error.setDetailedText('Часть "Погрешности"\nЗдесь вы получите формулу для расчета погрешности косвенных измерений, а так же сможете численно оценить эту погрешность. '
                              'Для того, чтобы все работало корректно нужно корректно вводить данные!\n\n'
                              '1) Формула вводится в формате y = k*x. Синтаксис для операторов как в питоне.\n\n'
                                '2) Поле с константами заполняется через пробел\n\n'
                            '3) Нельзя использовать индексацию к буквам, использовать композицию букв как переменную или константу. Отдельный символ - отдельная единица значения\n\n'
                            '4) Не стоит использовать заглавные буквы: не сможете посчитать значение погрешности\n\n'
                              '5) Коррекно заполняйте значениями. Можно использовать "," и "."\n\n\n'
                              'Часть "Графики"\n'
                              'Здесь вы сможете получить апроксимацию ваших точек тем графиком, которым вы захотите. Ее ввод происходит вами. '
                              'Так же вы сможете его красиво оформить, сделав соответствующие подписи к осям координат, '
                              'а если захотите сможете получить экстремумы и нули функции, а также погрешность коэффицентов.\n\n'
                              'Не пугайтесь, если в roots получится много непонятных значений. "Это связано с недостатками выбранного метода. Перед вами будет много близких друк к другу значений - это один нуль функции'
                              'выберете то его числовое значение, которое вам нравится больше всего. Погрешность вашего выбора пренебрежимо мала: сотые процента\n\n'
                              'А теперь немного о формализме:\n'
                              '1) Переменной здесь служит ТОЛЬКО x\n\n'
                                '2) Задавайте функцию, т.е. вводите только f(x). Пример: k*x+b (y = k*x+b не пойдет)\n\n'
                                 '3) Точки графика вводятся через пробел, разделителем десятичной части может выступать "," и "."\n\n'
                                '4) Проследите, что у вас кол-во точек по оси X и по оси Y совпадают'
                              )



        error.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab_helper"))
        self.btn_clear_graph.setText(_translate("MainWindow", "Обновить окно!!!"))
        # self.label_ex.setText(_translate("MainWindow", "Введите полный путь к Excel файлу,\n"
        #                                                "с которым вы собираетесь работать\n"
        #                                                "(из этого файла будут считываться данные\n"
        #                                                "указанные через индексы)"))
        # self.btn_ex.setText(_translate("MainWindow", "Работать с этим файлом!"))
        # self.menu.setTabText(self.menu.indexOf(self.ecxel_fail), _translate("MainWindow", "Выбор excel файла"))
        self.label_graph_high_1.setText(_translate("MainWindow", "введите формулу для графика:"))
        self.label_graphics_high_3.setText(_translate("MainWindow", "введите данные(точки графика):"))
        self.label_graph_X_1.setText(_translate("MainWindow", "x"))
        self.label_graphics_Y_1.setText(_translate("MainWindow", "y"))
        self.check_mistake_1.setText(_translate("MainWindow", "Хочу погрешность"))
        self.check_zero_1.setText(_translate("MainWindow", "Хочу нули ф-ии"))
        self.check_extremum_1.setText(_translate("MainWindow", "хочу экстремумы"))
        self.label_graph_high_4.setText(_translate("MainWindow", "добавьте галочки, если нужно"))
        self.btn_start_graph_1.setText(_translate("MainWindow", "Получить график!"))
        self.btn_add_graph_1.setText(_translate("MainWindow", "хочу добавить график\n"
                                                              "в те же координатные оси"))
        self.btn_new_graph_1.setText(_translate("MainWindow", "удалить\nпоследнее окно с графиком"))
        self.label_graph_paint_1.setText(_translate("MainWindow", "подпись к графику"))
        self.label_graph_paint_2.setText(_translate("MainWindow", "  подись к оси x"))
        self.label_graph_paint_3.setText(_translate("MainWindow", "  подпись к оси y"))
        self.menu_graphics.setTabText(self.menu_graphics.indexOf(self.graphics_main),
                                      _translate("MainWindow", "главный график"))

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
        self.menu_btn.setTitle(_translate("MainWindow", "О программе"))

    """Долгожданные функции)))"""

    def add_functions(self):

        # функции для погрешностей
        # Вместо ['q','w','e','r','t','y'] НАДО получить списки переменных и констант
        # Кроме того, эта вець должна вставлять формулу!!! Это ее первостепенная задача
        """"Это первая часть для погрешностей"""
        self.btn_mis_getFormula.clicked.connect(lambda: self.sonya_func_get_formula_mis())
        """"Это вторая часть для погрешностей"""
        self.btn_mis_getFigure.clicked.connect(lambda: self.sonya_func_get_figure())
        self.btn_mis_new.clicked.connect(lambda: self.clear_mis())
        # функции для графиков
        # создание и удаление дополнительных окон для графиков
        self.btn_add_graph_1.clicked.connect(lambda: self.create_window_graph_add())
        self.btn_new_graph_1.clicked.connect(lambda: self.delete_window_graph_add())
        # Непосредственно анина функция
        self.btn_start_graph_1.clicked.connect(lambda: print(self.set_params_graph()))
        self.btn_start_graph_1.clicked.connect(lambda: self.Ann_function_final())
        # Удаление из главного окна графиков данных
        self.btn_clear_graph.clicked.connect(lambda: self.clear_graphic())

    # Мое для создания окон в графиках
    def create_window_graph_add(self):
        for key in value_use:
            if value_use[key] == 0:
                value_use[key] = add_graph(key)
                self.menu_graphics.addTab(value_use[key].graph, "")
                _translate = QtCore.QCoreApplication.translate
                self.menu_graphics.setTabText(self.menu_graphics.indexOf(value_use[key].graph),
                                              _translate("MainWindow", names_use[0]))
                self.menu.setTabText(self.menu.indexOf(self.graphics), _translate("MainWindow", "графики"))
                names_use.pop(0)
                self.menu.setCurrentIndex(2)

                break

    def delete_window_graph_add(self):
        n = 9 - len(names_use)

        if n > 0 and n < 9:
            names_use.insert(0, names_start[n - 1])
            self.menu_graphics.removeTab(n)
            list_value = []
            for keys in value_use:
                list_value.append(value_use[keys])
            value_use[value_names[list_value.index(0)]] = 0
        elif n == 9:
            names_use.insert(0, names_start[n - 1])
            self.menu_graphics.removeTab(n)
            value_use[9] = 0

    # считывание текста напрямую
    def read_text(self, place):
        return place.toPlainText()

    # установление красивых стобликов в разделе погрешности
    def set_text_value(self, place, vars):
        for var in vars:
            place.append(f"{var} = ")

    # Функция устанавливает параметры для аниной функции
    def set_params_graph(self):
        """Индексация правильная, т.е. индекс о,о,о соответствует данным о первом графике"""
        list_X = []  # список строк переменных X
        list_Y = []  # список строк переменныx Y
        list_formuls = []  # список строк формул
        error = False
        roots = False
        extr = False

        # Проверка чекбоксов на зажантие
        if self.check_zero_1.isChecked():
            roots = True
        if self.check_mistake_1.isChecked():
            error = True
        if self.check_extremum_1.isChecked():
            extr = True

        # Занесение данных со страницы главного графика
        list_X.append(self.read_text(self.point_X_1))
        list_Y.append(self.read_text(self.point_Y_1))
        list_formuls.append(self.read_text(self.formula_graph_need_1))
        x_label = self.read_text(self.text_graph_label_x)
        y_label = self.read_text(self.text_graph_label_y)
        title = self.read_text(self.text_graph_label_g)

        # занесение данных с дополнительных графиков
        for key in value_use:
            if value_use[key] == 0:
                break
            else:
                list_X.append(value_use[key].point_X.toPlainText())
                list_Y.append(value_use[key].point_Y.toPlainText())
                list_formuls.append(value_use[key].formula_graph_need.toPlainText())

        return list_formuls, list_X, list_Y, title, x_label, y_label, error, roots, extr

    def clear_mis(self):
        _translate = QtCore.QCoreApplication.translate
        self.formula_mistake_need.clear()
        self.mistake_name_const.clear()
        self.formula_mistake.setText(_translate("MainWindow", "Здесь вы получите формулу погрешности"))
        self.number_mistake.setText(_translate("MainWindow", "Здесь вы получите числовое значение"))
        self.text_mistake_const.clear()
        self.text_mistake_var_middle.clear()
        self.text_mistake_var_deviation.clear()

    def clear_graphic(self):
        self.formula_graph_need_1.clear()
        self.point_X_1.clear()
        self.point_Y_1.clear()
        self.text_graph_label_x.clear()
        self.text_graph_label_g.clear()
        self.text_graph_label_y.clear()
        self.check_zero_1.setChecked(False)
        self.check_mistake_1.setChecked(False)
        self.check_extremum_1.setChecked(False)

    def error(self, text):
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Cейчас это действие выполнить нельзя")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)

        error.setDefaultButton(QMessageBox.Ok)
        error.setInformativeText("Где-то вы ввели некорректные данные")
        error.setDetailedText(text)

        # error.buttonClicked.connect(self.popup_action)
        error.exec_()




    def Ann_function_final(self):
        a = ann_func.plotting_graph(self.set_params_graph()[0],
                                    self.set_params_graph()[1],
                                    self.set_params_graph()[2],
                                    self.set_params_graph()[3],
                                    self.set_params_graph()[4],
                                    self.set_params_graph()[5],
                                    self.set_params_graph()[6],
                                    self.set_params_graph()[7],
                                    self.set_params_graph()[8])
        if not a:
            self.error(
                '1) Переменной здесь служит ТОЛЬКО x\n\n'
                '2) Задавайте функцию, т.е. вводите только f(x). Пример: k*x+b (y = k*x+b не пойдет)\n\n'
                '3) Точки графика вводятся через пробел, разделителем десятичной части может выступать "," и "."\n\n'
                '4) Проследите, что у вас кол-во точек по оси X и по оси Y совпадают')

    def list_making(self, place):
        place.split(' ')
        return place

    def sonya_func_get_formula_mis(self):
        try:
            list_const = (list(self.list_making(self.mistake_name_const.toPlainText())))
            try:
                str_formula = (self.formula_mistake_need.toPlainText())
                str_formula = sonya_func.get_f(str_formula)
                sonya_results = sonya_func.get_error_func(str_formula[1], list_const)
            except BaseException:
                sonya_results = sonya_func.get_error_func(self.formula_mistake_need.toPlainText(), list_const)
            str_formula = (self.formula_mistake_need.toPlainText())
            self.formula_mistake.setText(sonya_func.get_final_err_expr(sonya_func.get_f(str_formula)[0],
                                                                       sonya_func.get_error_func(
                                                                           sonya_func.get_f(str_formula)[1],
                                                                           list_const)[0]))
            self.text_mistake_const.clear()
            self.text_mistake_var_middle.clear()
            self.text_mistake_var_deviation.clear()
            self.set_text_value(self.text_mistake_const, list_const)
            self.set_text_value(self.text_mistake_var_middle, sonya_results[1])
            self.set_text_value(self.text_mistake_var_deviation, sonya_results[2])


        except BaseException:
            self.error('1) Формула вводится в формате y = k*x. Синтаксис для операторов как в питоне.\n\n'
                       '2) Поле с константами заполняется через пробел\n\n'
                       '3) Нельзя использовать индексацию к буквам, использовать композицию букв как переменную или константу. Отдельный символ - отдельная единица значения\n\n'
                       '4) Не стоит использовать заглавные буквы: не сможете посчитать значение погрешности')

    def create_dict_mis(self, text):
        text = text.replace(' ', '')
        text = text.split("\n")
        try:
            list_need = []
            for part in text:
                part = part.split('=')
                part[1] = part[1].replace(',', '.')
                part[1] = float(part[1])
                list_need.append(part)

            dictionary = dict(list_need)

            return dictionary
        except BaseException:
            if text == ['']:
                return {}

    def sonya_func_get_figure(self):
        try:
            str_formula = (self.formula_mistake_need.toPlainText())
            str_formula = sonya_func.get_f(str_formula)
            dict_start = self.create_dict_mis(self.text_mistake_const.toPlainText())
            dict_1 = self.create_dict_mis(self.text_mistake_var_deviation.toPlainText())
            dict_2 = self.create_dict_mis(self.text_mistake_var_middle.toPlainText())
            dict_res = {}
            for key_old in dict_1:
                key_res = key_old[1:].upper()
                dict_res[key_res] = dict_1[key_old]
            dict_res = dict_res | dict_start | dict_2
            """важно! надо будет поменять!"""
            text = self.formula_mistake.toPlainText()
            index_del = text.index('=')
            text = text[index_del + 1:]
            text = '(' + text + ")**0.5"
            pattern = re.compile('d\w')
            need_replace = pattern.findall(text)
            for part in need_replace:
                part_replace = part[1].upper()
                text = re.sub(f'{part}', part_replace, text)
            figure = sonya_func.exp_value(text, dict_res)
            middle = sonya_func.exp_value(str_formula[1], dict_res)
            sigma = figure * middle

            rang = self.rung_figure(sigma)
            if rang != 0 and rang != 1:
                sigma = round(sigma * 10 ** rang, 3)
                self.number_mistake.setText(
                    f'({round(middle * 10 ** rang)} ± {sigma})* 10**({rang})')
                self.number_mistake.append(f'ε={(round(figure, self.rung_figure(figure)+2))*100} %')
            elif rang == 0:
                sigma = round(sigma * 10 ** rang, 3)
                self.number_mistake.setText(
                    f'{round(middle * 10 ** rang)} ± {sigma}')
                self.number_mistake.append(f'ε={(round(figure, self.rung_figure(figure)+2))*100} %')
            elif rang == 1:
                sigma = round(sigma, 3)
                self.number_mistake.setText(
                    f'{round(middle)} ± {sigma}')
                self.number_mistake.append(f'ε={(round(figure, self.rung_figure(figure)+2))*100} %')
        except BaseException:
            self.error('1) Возвращение к изначальной формуле: нельзя использовать индексацию к буквам, использовать композицию букв как переменную или константу. Отдельный символ - отдельная единица значения.\n\n'
                       '2) Возвращение к изначальной формуле: нельзя использовать заглавные буквы!\n\n'
                       '3) Коррекно заполняйте значениями. Можно использовать "," и "."\n\n'
                       '4) Если возникла ошибка: обновляйте окно и начинайте заново.\n\n')

    def rung_figure(self, figure):
        n = 0
        figure_work = figure.__str__()
        try:
            flag = figure_work.index(',')
        except ValueError:
            flag = figure_work.index('.')
        if flag == 1:
            for i in range(len(figure_work)):
                if figure_work[i] == '0':
                    n += 1
                elif figure_work[i] == ',' or figure_work[i] == '.':
                    pass
                elif figure_work[i] != '0':
                    break
        else:
            n = -flag
        return n


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
