
import sys, os
from typing import MappingView
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QWidget, \
                            QPushButton, QLabel,  QStatusBar, \
                            QVBoxLayout, QAction, QFileDialog, QMessageBox,qApp, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSize                          
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtCore import (QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir)

import csv

# from pandas.io.parsers import read_csv


"""
App interface Qmenu, button, drawdown menu...
""" 

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowIcon(QIcon('./icon/logo.ico'))
        self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
        self.resize(self.screen_width * 2, self.screen_height * 2) 
        self.path=None
        self.check_change = True 
         

        """ 
        table for display csv
        """     
        self.table=QTableWidget()
        Layout = QVBoxLayout()
        # set Qtable as the layout
        self.table.setLayout(Layout)
        self.setCentralWidget(self.table)

        #self.table attrubute
        self.table.filterTypes = '(*.csv)'
        self.table.cellChanged.connect(self.check_current_activate)
        self.table.show()
        
        
        # stautsBar
        self.statusBar = self.statusBar()

        fileOption = self.menuBar().addMenu('&File')

        

        exitAct = QAction('Quit', self)   
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出应用')
        exitAct.triggered.connect(qApp.quit)

        """
       menu and its function. 
        """ 
        openAct=self.createAcation(self,'Open...','打开文件',self.file_open)
        openAct.setShortcut(QKeySequence.Open) 

        newAct=self.createAcation(self,'New','新建文件',lambda:print("new"))
        newAct.setShortcut(QKeySequence.New)

        saveAct=self.createAcation(self,'Save','保存',self.save)
        saveAct.setShortcut(QKeySequence.Save)

        saveasAct=self.createAcation(self,'Save as','另存为',self.save_as)
        saveasAct.setShortcut(QKeySequence('Ctrl+Shift+S'))

        cutAct=self.createAcation(self,'Cut','剪辑',self.cut)
        cutAct.setShortcut(QKeySequence.Cut)

        copyAct=self.createAcation(self,'Copy','复制',self.copy)
        copyAct.setShortcut(QKeySequence.Copy)

        pasteAct=self.createAcation(self,'Paste','粘贴',self.paste)
        pasteAct.setShortcut(QKeySequence.Paste)

        fileOption.addActions([newAct])
        #sub menu under the File/New Form
        newForm_menu=fileOption.addMenu('New Form')
        newForm_menu.addAction("Visble Rows")
        newForm_menu.addAction("Selected Rows")
        newForm_menu.addAction("Row List")
        newForm_menu.addAction("Pivoting")
        newForm_menu.addAction("Reverse Pivoting")
        newForm_menu.addAction("Transposition")

        fileOption.addActions([openAct,saveAct,saveasAct])

        
        
        editOption = self.menuBar().addMenu("&Edit ")
        editOption.addActions([cutAct,copyAct,pasteAct])

        dataOption = self.menuBar().addMenu("&Data ")
        dataOption.addAction("New")

        chemOption = self.menuBar().addMenu("&Chemistry ")
        chemOption.addAction("New")

        dabaseOption = self.menuBar().addMenu("&Database ")
        dabaseOption.addAction("New")

        listOption = self.menuBar().addMenu("&List ")
        listOption.addAction("New")

        macroOption = self.menuBar().addMenu("&Macro ")
        macroOption.addAction("New")

        helpOption = self.menuBar().addMenu("&Help ")
        helpOption.addAction("New")

        self.update_title()
        




        """
        check cell activity
        """ 
        
    
    def check_current_activate(self):
        if self.check_change:
            
            row = self.table.currentRow()
            col = self.table.currentColumn()
            value = self.table.item(row, col)
            value = value.text()

            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    
    def createAcation(self,parent,action_name,set_staus_tip,triggered_method):
        action=QAction(action_name,parent)
        action.setStatusTip(set_staus_tip)
        action.triggered.connect(triggered_method)

        return action

        

# menu function 
    def file_open(self):
        self.check_change = False
        self.path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), self.table.filterTypes)
        self.setWindowTitle('{0} - csv reader'.format(os.path.basename(self.path[0]) if self.path[0] else 'Unittled'))

        if self.path[0] != '':
            with open(self.path[0], newline='') as csv_file:
                self.table.setRowCount(0)
                self.table.setColumnCount(5)
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    row = self.table.rowCount()
                    self.table.insertRow(row)
                    if len(row_data) > 5:
                        self.table.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.table.setItem(row, column, item)
        self.check_change = True
    
        """
    Save file and Save as csv to another dir
    """ 
    def save_as(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), self.table.filterTypes)
        self.path=path
        if self.path[0] != '':
            with open(self.path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

    def save(self):

        if self.path[0] != '':
            
            with open(self.path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

    def cut(self):
        for item in self.table.selectionModel().selection().indexes():
            row = item.row()
            col = item.column()
            select_item = self.table.item(row,col)
            if select_item is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(select_item.text())
                select_item.setText("")

    def copy(self):
        for item in self.table.selectionModel().selection().indexes():
            row = item.row()
            col = item.column()
            select_item = self.table.item(row,col)
            if select_item is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(select_item.text())
                select_item.setText(select_item.text())
    
    def paste(self):
        for item in self.table.selectionModel().selection().indexes():
            row = item.row()
            col = item.column()
            select_item = self.table.item(row,col)
            clip = QtWidgets.QApplication.clipboard()
            select_item.setText(clip.text())
        



    def update_title(self):
        self.setWindowTitle('{0} - csv reader'.format(os.path.basename(self.path) if self.path else 'Unittled'))

        


            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    sdf_reader = AppDemo()
    

    sdf_reader.show()
    
    sys.exit(app.exec_())
    

