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
        self.ui.p10.pressed.connect(self.addFreq)
        self.ui.p100.pressed.connect(self.addFreq)
        self.ui.p1000.pressed.connect(self.addFreq)

    def toPlay(self):
        f = int(self.ui.freq_le.text()) #Hz
        fs = 44100 #Hz
        length = 2 #s
        x = np.arange(fs*length)
        # y = np.zeros(fs*length)
        # for i in range(8):
        #     y = y + 10**(-i) * np.sin(2 * np.pi * (i + 1) * f / fs * x)
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
        if sender_name == 'p10':
            f = f + 10
        elif sender_name == 'p100':
            f = f + 100
        else:
            f = f + 1000
        self.ui.freq_le.setText(str(f))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormWidget()
    main.show()
    sys.exit(app.exec_())