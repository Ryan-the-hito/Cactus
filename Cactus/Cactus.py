#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
							 QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
							 QSystemTrayIcon, QMenu, QDialog, QMenuBar,
							 QPlainTextEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QColor
import PyQt6.QtGui
import webbrowser
import os
import sys
import subprocess
import time
import pyautogui


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("/Applications/Cactus.app/Contents/Resources/cactus-tray.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🌵 Get text from links!")
menu.addAction(action3)

menu.addSeparator()

action7 = QAction("⚙️ Settings")
menu.addAction(action7)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
btna4 = QAction("&Get text from links!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(btna4)


class window_about(QWidget):  # 增加说明页面(About)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		self.setUpMainWindow()
		self.resize(400, 380)
		self.center()
		self.setWindowTitle('About')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widg1 = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/cactus.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumWidth(100)
		l1.setMaximumHeight(100)
		l1.setScaledContents(True)
		blay1 = QHBoxLayout()
		blay1.setContentsMargins(0, 0, 0, 0)
		blay1.addStretch()
		blay1.addWidget(l1)
		blay1.addStretch()
		widg1.setLayout(blay1)

		widg2 = QWidget()
		lbl0 = QLabel('Cactus', self)
		font = PyQt6.QtGui.QFont()
		font.setFamily("Arial")
		font.setBold(True)
		font.setPointSize(20)
		lbl0.setFont(font)
		blay2 = QHBoxLayout()
		blay2.setContentsMargins(0, 0, 0, 0)
		blay2.addStretch()
		blay2.addWidget(lbl0)
		blay2.addStretch()
		widg2.setLayout(blay2)

		widg3 = QWidget()
		lbl1 = QLabel('Version 0.0.2', self)
		blay3 = QHBoxLayout()
		blay3.setContentsMargins(0, 0, 0, 0)
		blay3.addStretch()
		blay3.addWidget(lbl1)
		blay3.addStretch()
		widg3.setLayout(blay3)

		widg4 = QWidget()
		lbl2 = QLabel('Thanks for your love🤟.', self)
		blay4 = QHBoxLayout()
		blay4.setContentsMargins(0, 0, 0, 0)
		blay4.addStretch()
		blay4.addWidget(lbl2)
		blay4.addStretch()
		widg4.setLayout(blay4)

		widg5 = QWidget()
		lbl3 = QLabel('感谢您的喜爱！', self)
		blay5 = QHBoxLayout()
		blay5.setContentsMargins(0, 0, 0, 0)
		blay5.addStretch()
		blay5.addWidget(lbl3)
		blay5.addStretch()
		widg5.setLayout(blay5)

		widg6 = QWidget()
		lbl4 = QLabel('♥‿♥', self)
		blay6 = QHBoxLayout()
		blay6.setContentsMargins(0, 0, 0, 0)
		blay6.addStretch()
		blay6.addWidget(lbl4)
		blay6.addStretch()
		widg6.setLayout(blay6)

		widg7 = QWidget()
		lbl5 = QLabel('※\(^o^)/※', self)
		blay7 = QHBoxLayout()
		blay7.setContentsMargins(0, 0, 0, 0)
		blay7.addStretch()
		blay7.addWidget(lbl5)
		blay7.addStretch()
		widg7.setLayout(blay7)

		widg8 = QWidget()
		bt1 = QPushButton('The Author', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.intro)
		bt2 = QPushButton('Github Page', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.homepage)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg8.setLayout(blay8)

		widg9 = QWidget()
		bt3 = QPushButton('🍪\n¥5', self)
		bt3.setMaximumHeight(50)
		bt3.setMinimumHeight(50)
		bt3.setMinimumWidth(50)
		bt3.clicked.connect(self.donate)
		bt4 = QPushButton('🥪\n¥10', self)
		bt4.setMaximumHeight(50)
		bt4.setMinimumHeight(50)
		bt4.setMinimumWidth(50)
		bt4.clicked.connect(self.donate2)
		bt5 = QPushButton('🍜\n¥20', self)
		bt5.setMaximumHeight(50)
		bt5.setMinimumHeight(50)
		bt5.setMinimumWidth(50)
		bt5.clicked.connect(self.donate3)
		bt6 = QPushButton('🍕\n¥50', self)
		bt6.setMaximumHeight(50)
		bt6.setMinimumHeight(50)
		bt6.setMinimumWidth(50)
		bt6.clicked.connect(self.donate4)
		blay9 = QHBoxLayout()
		blay9.setContentsMargins(0, 0, 0, 0)
		blay9.addStretch()
		blay9.addWidget(bt3)
		blay9.addWidget(bt4)
		blay9.addWidget(bt5)
		blay9.addWidget(bt6)
		blay9.addStretch()
		widg9.setLayout(blay9)

		widg10 = QWidget()
		lbl6 = QLabel('© 2023 Ryan-the-hito. All rights reserved.', self)
		blay10 = QHBoxLayout()
		blay10.setContentsMargins(0, 0, 0, 0)
		blay10.addStretch()
		blay10.addWidget(lbl6)
		blay10.addStretch()
		widg10.setLayout(blay10)

		main_h_box = QVBoxLayout()
		main_h_box.addWidget(widg1)
		main_h_box.addWidget(widg2)
		main_h_box.addWidget(widg3)
		main_h_box.addWidget(widg4)
		main_h_box.addWidget(widg5)
		main_h_box.addWidget(widg6)
		main_h_box.addWidget(widg7)
		main_h_box.addWidget(widg8)
		main_h_box.addWidget(widg9)
		main_h_box.addWidget(widg10)
		main_h_box.addStretch()
		self.setLayout(main_h_box)

	def intro(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

	def homepage(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Cactus')

	def donate(self):
		dlg = CustomDialog()
		dlg.exec()

	def donate2(self):
		dlg = CustomDialog2()
		dlg.exec()

	def donate3(self):
		dlg = CustomDialog3()
		dlg.exec()

	def donate4(self):
		dlg = CustomDialog4()
		dlg.exec()

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()


class CustomDialog(QDialog):  # (About1)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/wechat5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/alipay5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Donate later~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.cancel)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog2(QDialog):  # (About2)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/wechat10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/alipay10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Donate later~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.cancel)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog3(QDialog):  # (About3)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/wechat20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/alipay20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Donate later~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.cancel)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog4(QDialog):  # (About4)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/wechat50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap('/Applications/Cactus.app/Contents/Resources/alipay50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Donate later~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.cancel)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def cancel(self):  # 设置取消键的功能
		self.close()


class window_update(QWidget):  # 增加更新页面（Check for Updates）
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		lbl = QLabel('Current Version: 0.0.2', self)
		lbl.move(110, 75)

		lbl0 = QLabel('Check Now:', self)
		lbl0.move(30, 20)

		bt1 = QPushButton('Check Github', self)
		bt1.clicked.connect(self.upd)
		bt1.move(110, 15)

		bt2 = QPushButton('Check Baidu Net Disk', self)
		bt2.clicked.connect(self.upd2)
		bt2.move(110, 45)

		self.resize(300, 110)
		self.center()
		self.setWindowTitle('Check for Updates')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def upd(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Cactus/releases')

	def upd2(self):
		webbrowser.open('https://pan.baidu.com/s/1LvzcoTGl0B2wB5W3nlRLsw?pwd=jsyn')

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()

class window3(QWidget):  # 主窗口
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setUpMainWindow()
		self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
		self.setFixedSize(500, 309)
		self.WEIGHT = int(self.screen().availableGeometry().width())
		self.HEIGHT = int(self.screen().availableGeometry().height())
	
	def setUpMainWindow(self):
		self.text1 = QPlainTextEdit(self)
		self.text1.setReadOnly(False)
		self.text1.setObjectName('edit')

		self.btn_0 = QPushButton('Copy all', self)
		self.btn_0.clicked.connect(self.CopyAll)
		
		self.btn_1 = QPushButton('Copy selected', self)
		self.btn_1.clicked.connect(self.CopyTwo)

		self.btn_2 = QPushButton('Cancel', self)
		self.btn_2.clicked.connect(self.cancel)

		qw1 = QWidget()
		vbox1 = QHBoxLayout()
		vbox1.setContentsMargins(0, 0, 0, 0)
		vbox1.addWidget(self.btn_0)
		vbox1.addWidget(self.btn_1)
		vbox1.addWidget(self.btn_2)
		qw1.setLayout(vbox1)

		qw2 = QWidget()
		vbox2 = QVBoxLayout()
		vbox2.setContentsMargins(20, 20, 20, 20)
		vbox2.addWidget(self.text1)
		vbox2.addWidget(qw1)
		qw2.setLayout(vbox2)
		qw2.setObjectName("Main")

		vbox3 = QHBoxLayout()
		vbox3.setContentsMargins(0, 0, 0, 0)
		vbox3.addWidget(qw2)
		self.setLayout(vbox3)

	def CopyAll(self):
		ResultEnd = self.text1.toPlainText()
		ResultEnd = ResultEnd.encode('utf-8').decode('utf-8', 'ignore')
		uid = os.getuid()
		env = os.environ.copy()
		env['__CF_USER_TEXT_ENCODING'] = f'{uid}:0x8000100:0x8000100'
		p = subprocess.Popen(['pbcopy', 'w'], stdin=subprocess.PIPE, env=env)
		p.communicate(input=ResultEnd.encode('utf-8'))
		self.cancel()
	
	def CopyTwo(self):
		ResultEnd = self.text1.textCursor().selectedText()
		ResultEnd = ResultEnd.encode('utf-8').decode('utf-8', 'ignore')
		uid = os.getuid()
		env = os.environ.copy()
		env['__CF_USER_TEXT_ENCODING'] = f'{uid}:0x8000100:0x8000100'
		p = subprocess.Popen(['pbcopy', 'w'], stdin=subprocess.PIPE, env=env)
		p.communicate(input=ResultEnd.encode('utf-8'))
		self.cancel()
	
	def activate(self):  # 设置窗口显示
		# Pause for a few seconds to give you time to position the mouse where you want to click
		text = codecs.open('/Applications/Cactus.app/Contents/Resources/SetTime.txt', 'r', encoding='utf-8').read()
		if text == '' or text == '0':
			n = 0
		else:
			n = int(text)
		time.sleep(n)
		
		# Right click at the current mouse position
		pyautogui.mouseDown(button='right')
		pyautogui.mouseUp(button='right')
		
		# Simulate Command+C shortcut
		pyautogui.hotkey('command', 'c')
		
		# Copy to plaintext
		a = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
		self.text1.setPlainText(a)

		x, y = pyautogui.position()
		if x + 500 > self.WEIGHT:
			x = self.WEIGHT - 510
		if y + 309 > self.HEIGHT:
			y = self.HEIGHT - 319
		self.move(x,y)
		
		self.show()
		self.setFocus()
		self.raise_()
		self.activateWindow()
	
	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
	
	def cancel(self):  # 设置取消键的功能
		self.close()


class window4(QWidget):  # Customization settings
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):  # 设置窗口内布局
		self.setUpMainWindow()
		self.setFixedSize(500, 120)
		self.center()
		self.setWindowTitle('Customization settings')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
	
	def setUpMainWindow(self):
		self.lbl1 = QLabel('Seconds before detection after being triggered: ', self)
		
		self.le1 = QLineEdit(self)
		self.le1.setPlaceholderText('Numbers only, no decimal. Default=0')
		text = codecs.open('/Applications/Cactus.app/Contents/Resources/SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)
		
		self.btn_1 = QPushButton('Save', self)
		self.btn_1.clicked.connect(self.SetTime)
		self.btn_1.setFixedSize(150, 20)
		
		qw1 = QWidget()
		vbox1 = QHBoxLayout()
		vbox1.setContentsMargins(0, 0, 0, 0)
		vbox1.addStretch()
		vbox1.addWidget(self.btn_1)
		vbox1.addStretch()
		qw1.setLayout(vbox1)

		vbox2 = QVBoxLayout()
		vbox2.setContentsMargins(20, 20, 20, 20)
		vbox2.addWidget(self.lbl1)
		vbox2.addWidget(self.le1)
		vbox2.addWidget(qw1)
		self.setLayout(vbox2)
	
	def SetTime(self):
		if self.le1.text() != '':
			SetTime = str(int(self.le1.text()))
			with open("/Applications/Cactus.app/Contents/Resources/SetTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(SetTime)
			self.close()
	
	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
	
	def activate(self):  # 设置窗口显示
		self.show()
		self.setFocus()
		self.raise_()
		self.activateWindow()
	
	def cancel(self):  # 设置取消键的功能
		self.close()

style_sheet_ori = '''
	QTabWidget::pane {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QTableWidget{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #FFFFFF;
		color: #000000;
		font: 14pt Helvetica;
}
	QWidget#Main {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QPushButton{
		border: 1px outset grey;
		background-color: #FFFFFF;
		border-radius: 4px;
		padding: 1px;
		color: #000000
}
	QPushButton:pressed{
		border: 1px outset grey;
		background-color: #0085FF;
		border-radius: 4px;
		padding: 1px;
		color: #FFFFFF
}
	QPlainTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QPlainTextEdit#edit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #FFFFFF;
		color: rgb(113, 113, 113);
		font: 14pt Helvetica;
}
	QTableWidget#small{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QLineEdit{
		border-radius:4px;
		border: 1px solid gray;
		background-color: #FFFFFF;
}
	QTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QListWidget{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
	w1 = window_about()  # about
	w2 = window_update()  # update
	w3 = window3()  # main1
	w3.setAutoFillBackground(True)
	p = w3.palette()
	p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
	w3.setPalette(p)
	w4 = window4()  # CUSTOMIZING
	action1.triggered.connect(w1.activate)
	action2.triggered.connect(w2.activate)
	action3.triggered.connect(w3.activate)
	action7.triggered.connect(w4.activate)
	btna4.triggered.connect(w3.activate)
	app.setStyleSheet(style_sheet_ori)
	app.exec()
