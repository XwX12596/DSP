from PyQt5.QtWidgets import QApplication, QWidget
import sys
import sounddevice as sd
import numpy as np
from form import Ui_Form #a form auto-generated from a ui file which was made in help of Qt Creator

class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self) #initialize the ui
        self.Ui_connect() #connect buttons with functions
        self.ui.freq_le.setText('0') #initial value of frequency
    
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
        '''
        Generate and play the sound wave according to the text of lineEdit.
        '''
        f = int(self.ui.freq_le.text()) # frequency of the sine wave
        fs = 96000 # sampling 
        length = 10 # seconds it lasts
        x = np.arange(fs*length)
        y = np.sin(2 * np.pi * f / fs * x) # generate a sine wave
        sd.play(y,fs,blocking=False) # play the sine wave as a sound wave
        
    def addFreq(self):
        '''
        Increase or decrease the value in LineEdit which stands for the frequency of sound wave
        '''
        sender = self.sender()
        sender_name = sender.objectName()
        try:
            f = int(self.ui.freq_le.text()) # get the value of LineEdit
        except:
            self.ui.freq_le.setText('0') # default frequency (be 0 for protecting ears)
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
        self.ui.freq_le.setText(str(f)) # show the changed frequency
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormWidget()
    main.show() #initialize and show the window
    sys.exit(app.exec_())