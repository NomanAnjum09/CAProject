# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QFileDialog) 	
from PyQt5.QtGui import QPalette
from main import driver
from functools import partial
import pickle


qtCreatorFile = "base1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

globalobj = 0
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def get_input(self):
        cache_size = int(self.cache_size.currentText())
        block_size = int(self.block_size.currentText())
        associativity = int(self.associativity.value())
        memory_accesses = int(self.mem_access.text())
        output = driver(cache_size, associativity, block_size, memory_accesses)
        self.tableWidget.item(0,0).setText(str(output['miss_rate']))
        self.tableWidget.item(0,1).setText(str(output['hit_rate']))
        self.tableWidget.item(0,2).setText(str(output['miss_count']))
        self.tableWidget.item(0,3).setText(str(output['hit_count']))

    def plot(self):
        plt.style.use('dark_background')
        block_size = 4
        memory_accesses = 2000

        # Associtive Array with 0 index having x and y lists of associativity 1 outputs and so on.
        ass_xy = []
        
        
        use_db = False
        if(self.use_db.isChecked()):
            use_db = True
        if use_db:
            store_file = open('pickled_data_set1', 'rb')
            stored_data = pickle.load(store_file)
            print(stored_data)
            ass_xy, associativities = stored_data
            
            print(ass_xy)
            associativities = [2,4,8]

        else:    
            store_file = open('pickled_data_set1', 'wb')
            associativities = [2,4,8]
            for associativity in associativities:
                x_points=[]
                outputs_driver=[]
                cache_size = 1024 # start from  1 KB     
                while cache_size <= 131072: # 128 KB
                    output = driver(cache_size, associativity, block_size, memory_accesses) 
                    x_points.append(cache_size)
                    outputs_driver.append(output)
                    cache_size *= 2
                    # print(step)
                ass_xy.append([x_points, outputs_driver])

            pickle.dump((ass_xy, associativities), store_file)

        store_file.close()
        fig,ax = plt.subplots(figsize=(10, 10))

        

        legends = []
        for index,ass in enumerate(ass_xy):
            y_points = []
            for points in ass[1]:
                y_points.append(points['miss_rate'])
            
            lines, = plt.plot(ass[0], y_points, label = str(associativities[index]) + ' Way Associative')
            legends.append(lines)


        plt.legend(handles=legends)
        plt.xlabel('Cache Size (Bytes)')
        plt.ylabel('Miss Rate')
        # plt.xscale('log')
        plt.show()

        


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_calculate.clicked.connect(self.get_input)
        self.pushButton_plot.clicked.connect(self.plot)

        # self.pushButton_plot.hide()
        # self.pushButton_kruskal.hide()
        # self.pushButton_prims.hide()
        # self.pushButton_dijkstra.hide()
        # self.pushButton_bellman.hide()
        # self.pushButton_floyd.hide()
        # self.pushButton_local.hide()
        # self.pushButton_all.hide()
        # self.tableWidget.hide()

        # self.pushButton_plot.clicked.connect(lambda: PLOTTING())
        # self.pushButton_kruskal.clicked.connect(lambda: buttonpress(kruskal.kruskal,from_to_cost,no_of_nodes))
        # self.pushButton_prims.clicked.connect(lambda: buttonpress( prims.PRIMS,from_to_cost,no_of_nodes,source ))
        # self.pushButton_dijkstra.clicked.connect(lambda :buttonpress(dijkstra.DIJKSTRA,from_to_cost,no_of_nodes,source))
        # self.pushButton_bellman.clicked.connect(lambda: buttonpress(bellmanford.BELLMANFORD,from_to_cost,no_of_nodes,source))
        # self.pushButton_floyd.clicked.connect(lambda: buttonpress(FloydWarshall.FLOYDWARSHALL,from_to_cost,no_of_nodes,source,node_x_y))
        # self.pushButton_local.clicked.connect(lambda: LocalCluster.LocalCluster(result))
        # self.pushButton_all.clicked.connect(lambda: all_bulk.get_all_results(from_to_cost,no_of_nodes,source,node_x_y, result, self))
        # self.pushButton_get_input.clicked.connect(self.benchmark_input)


        
if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    