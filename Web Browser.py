import sys
from PySide.QtCore import *
from PySide.QtGui import *
from Pyside.QtWebKit import *

class Browser(QWidget):
	def __init__(self):
		super(Browser, self).__init__()

		# Set the Default Website for the Browser
		self.webview = QWebView(self)
		self.webview.load("http://www.google.co.za")

		#Set how Big the Browser's Window will be
		self.setGeometry(0, 0, 800, 600)

		#Set the Back Button
		self.back_btn = QPushButton("<", self)
		self.back_btn.clicked.connect(self.webview.back)
		self.back_btn.setMaximumSize(20, 20)

		#Set the Forward Button
		self.forward_btn = QPushButton(">", self)
		self.forward_btn.clicked.connect(self.webview.forward)
		self.forward_btn.setMaximumSize(20, 20)

		#That little Bar where you put in the URL
		self.url_entry= QLineEdit(self)
		self.url_entry.setMinimumSize(200, 20)
		self.url_entry.setMaximumSize(20, 20)

		#Start the Search
		self.go_btn = QPushButton("Go", self)
		self.go_btn.clicked.connect(self.go_btn_clicked)
		self.go_btn.setMaximumSize(20, 20)

		self.favourites = QComboBox(self)
		self.favourites.addItems(["http://www.google.co.za",
			"http://www.raspberrypi.org",
			"http://www.facebook.com",])
		self.favourites.activated.connect(self.favourite_selected)
		self.favourites.setMinimumSize(200, 20)
		self.favourites.setMaximumSize(300, 20)

		self.search_box = QLineEdit(self)
		self.search_box.setMinimumSize(200, 20)
		self.search_box.setMaximumSize(300, 20)

		self.search_btn = QPushPutton("Find It", self)
		self.search_btn.clicked.connect(self.search_btn_clicked)
		self.search_btn.setMaximumSize(50, 20)

		self.zoom_slider = QSlider(Qt.Orientation(1), self)
		self.zoom_slider.setRange(2, 50)
		self.zoom_slider.setValue(10)
		self.zoom_slider.valueChanged.connect(self.zoom_changed)

		self.zoom_label = QLabel("Zoom:")
		self.webView.loadStarted.connect(self.page_loading)

		#How does the Menu Bar Look Like
		self.menu_bar = QHBoxLayout()
		self.menu_bar.addWidget(self.back_btn)
		self.menu_bar.addWidget(self.forward_btn)
		self.menu_bar.addWidget(self.url_entry)
		self.menu_bar.addWidget(self.go_btn)
		self.menu_bar.addStretch()
                self.menu_bar.addWidget(self.favourites)

                #Set the Layout
		self.main_layout = QVBoxLayout()
		self.main_layout.addLayout(self.menu_bar)
		self.setLayout(self.main_layout)

	def go_btn_clicked(self):
		self.webview.load(self.url_entry.text())

	def favourite_selected(self):
		self.webview.load(self.favourites.currentText())

	def zoom_changed(self):
		self.webview.setZoomFactor(self.zoom_slider.value()/10)

	def search_btn_clicked(self):
		self.webview.load("https://www.google.co.za/search?q="
			+ self.search_box.text())

	def page_loading(self):
		self.url_entry.setText(self.webview.url().toString())




class BrowserWindow(QMainWindow):
	def __init__(self):
		super(BrowserWindow, self).init()

		self.widget = Browser()
		self.setCentralWidget(self.widget)

		self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
		self.exitAction.setShortcut('Ctrl+Q')
		self.exitAction.setStatusTip('Exit Application')
		self.exitAction.triggered.connect(self.close)

		self.openFile = QAction(QIcon('exit.png'), 'Open', self)
		self.openFile.setShortcut('Ctrl+O')
		self.openFile.setSattusTip('Open new File')
		self.openFile.triggered.connect(self.showDialog)

		self.menu = self.menuBar()
		self.fileMenu = self.menu.addMenu('&File')
		self.fileMenu.addAction(self.openFile)
		self.fileMenu.addAction(self.exitAction)

		def showDialog(self):
			fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
			self.widget.webview.load("file:///" + fname)

		#Create a Qt Application
		app = QApplication(sys.agrv)
		window = BrowserWindow()
		window.show()

		#Loop the Application
		app.exec_()
		sys.exit()
