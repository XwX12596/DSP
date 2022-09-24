from PyQt5.QtWidgets import QApplication, QWidget
import sys
import sounddevice as sd
import numpy as np
from form import Ui_Form

class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.Ui_connect()
        self.ui.freq_le.setText('0')
    
    def Ui_connect(self):
        self.ui.start.pressed.connect(self.toPlay)
        self.ui.m1.pressed.connect(self.addFreq)
        self.ui.m10.pressed.connect(self.addFreq)
        self.ui.m100.pressed.connect(self.addFreq)
        self.ui.p1.pressed.connect(self.addFreq)
        self.ui.p10.pressed.connect(self.addFreq)
        self.ui.p100.pressed.connect(self.addFreq)
        self.ui.p1000.pressed.connect(self.addFreq)
        self.ui.p10000.pressed.connect(self.addFreq)

    def toPlay(self):
        f = int(self.ui.freq_le.text()) #Hz
        fs = 96000 #Hz
        length = 10 #s
        x = np.arange(fs*length)
        y0 = np.zeros(fs*length)
        y = np.sin(2 * np.pi * f / fs * x)
        sd.play(y,fs,blocking=False)
        
    def addFreq(self):
        sender = self.sender()
        sender_name = sender.objectName()
        try:
            f = int(self.ui.freq_le.text())
        except:
            self.ui.freq_le.setText('0')
            f = 1
        if sender_name == 'm1':
            f = f - 1
        elif sender_name == 'm10':
            f = f - 10
        elif sender_name == 'm100':
            f = f - 100
        elif sender_name == 'p1':
            f = f + 1
        elif sender_name == 'p10':
            f = f + 10
        elif sender_name == 'p100':
            f = f + 100
        elif sender_name == 'p1000':
            f = f + 1000
        else:
            f = f + 10000
        self.ui.freq_le.setText(str(f))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormWidget()
    main.show()
    sys.exit(app.exec_())