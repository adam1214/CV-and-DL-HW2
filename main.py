# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

def btn1_1_clicked(self):
    print("btn1_1")
    imgL = cv2.imread('imL.png',cv2.IMREAD_GRAYSCALE)
    imgR = cv2.imread('imR.png',cv2.IMREAD_GRAYSCALE)
    stereo = cv2.StereoBM.create(numDisparities=64, blockSize=9)
    disparity = stereo.compute(imgL,imgR)
    plt.imshow(disparity, 'gray')
    plt.show()


def btn2_1_clicked(self):
    print("btn2_1")

    backSub = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=200, detectShadows=True) #generate the foreground mask
    capture = cv2.VideoCapture(cv2.samples.findFileOrKeep('bgSub.mp4')) #read the input video
    if not capture.isOpened:
        print('Unable to open: bgSub.mp4')
        exit(0)

    while True:
        ret, frame = capture.read()

        if frame is None:
            break

        fgMask = backSub.apply(frame) #update the background model

        #get the frame number and write it on the current frame
        cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        #show the current frame and the fg masks
        cv2.imshow('Frame', frame) #original video
        cv2.imshow('FG Mask', fgMask)
        
        keyboard = cv2.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    
    capture.release()

click_cnt = 0
#capture video
cap = cv2.VideoCapture('featureTracking.mp4')
ret_gloabl, frame_global = cap.read()
pt1 = (0,0)
pt2 = (0,0)
pt3 = (0,0)
pt4 = (0,0)
pt5 = (0,0)
pt6 = (0,0)
pt7 = (0,0)

def draw_rectangle(event, x, y, flags, param): #mouse callback function
    global click_cnt, pt1, pt2, pt3, pt4, pt5, pt6, pt7, cap
    if event == cv2.EVENT_LBUTTONDOWN and click_cnt < 7: #draw square at the center point
        if click_cnt == 0:
            pt1 = (x,y)
        elif click_cnt == 1:
            pt2 = (x,y)
        elif click_cnt == 2:
            pt3 = (x,y)
        elif click_cnt == 3:
            pt4 = (x,y)
        elif click_cnt == 4:
            pt5 = (x,y)
        elif click_cnt == 5:
            pt6 = (x,y)
        elif click_cnt == 6:
            pt7 = (x,y)
        
        click_cnt = click_cnt + 1
        cv2.rectangle(frame_global, (x-5,y-5), (x+5,y+5), (0,0,255), 2)
        cv2.imshow('frame 1', frame_global)

    elif click_cnt == 7:
        cap.release()

        
def btn3_1_clicked(self):
    print("btn3_1")
    cv2.namedWindow(winname='frame 1')
    cv2.setMouseCallback('frame 1', draw_rectangle)
    cv2.imshow('frame 1', frame_global)
    print("Please click 7 center points of 7 blue circles of this image.")
        
def btn3_2_clicked(self):
    global pt1, pt2, pt3, pt4, pt5, pt6, pt7
    print("btn3_2")

    if pt1==(0,0) or pt2==(0,0) or pt3==(0,0) or pt4==(0,0) or pt5==(0,0) or pt6==(0,0) or pt7==(0,0):
        pt1=(118, 72)
        pt2=(111, 96)
        pt3=(119, 116)
        pt4=(137, 239)
        pt5=(128, 257)
        pt6=(173, 267)
        pt7=(194, 259)
        print('You have not tracked 7 points, and program have tracked the default 7 points for you.')

    capture = cv2.VideoCapture(cv2.samples.findFileOrKeep('featureTracking.mp4')) #read the input video
    if not capture.isOpened:
        print('Unable to open: featureTracking.mp4')
        exit(0)

    while True:
        ret, frame = capture.read()

        if frame is None:
            break

        #get the frame number and write it on the current frame
        cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

        cv2.imshow('Frame', frame)
        
        keyboard = cv2.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    
    capture.release()
    


def btn4_1_clicked(self):
    print("btn4_1")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn1_1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn1_1.setObjectName("btn1_1")
        self.verticalLayout_3.addWidget(self.btn1_1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn2_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn2_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn2_1.setObjectName("btn2_1")
        self.verticalLayout_4.addWidget(self.btn2_1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn3_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn3_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn3_1.setObjectName("btn3_1")
        self.verticalLayout_5.addWidget(self.btn3_1)
        self.btn3_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn3_2.setMinimumSize(QtCore.QSize(0, 50))
        self.btn3_2.setObjectName("btn3_2")
        self.verticalLayout_5.addWidget(self.btn3_2)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn4_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn4_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn4_1.setObjectName("btn4_1")
        self.verticalLayout_6.addWidget(self.btn4_1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "1. Stereo"))
        self.btn1_1.setText(_translate("MainWindow", "1.1 Display"))
        self.groupBox_2.setTitle(_translate("MainWindow", "2. Background Subtraction"))
        self.btn2_1.setText(_translate("MainWindow", "2.1 Background Subtraction"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. Feature Tracking"))
        self.btn3_1.setText(_translate("MainWindow", "3.1 Preprocessing"))
        self.btn3_2.setText(_translate("MainWindow", "3.2 Video Tracking"))
        self.groupBox_4.setTitle(_translate("MainWindow", "4. Augmented Reality"))
        self.btn4_1.setText(_translate("MainWindow", "4.1 Augmented Reality"))
        
        self.btn1_1.clicked.connect(btn1_1_clicked)
        self.btn2_1.clicked.connect(btn2_1_clicked)
        self.btn3_1.clicked.connect(btn3_1_clicked)
        self.btn3_2.clicked.connect(btn3_2_clicked)
        self.btn4_1.clicked.connect(btn4_1_clicked)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())