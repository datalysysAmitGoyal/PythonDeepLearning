import threading
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from my_modules.AddTwoNums import *
import time

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_addition.clicked.connect(self.dispSum)
        self.show()

    def dispSum(self):
        numb1 = self.ui.lineEdit_firstNum.text()
        numb2 = self.ui.lineEdit_secondNum.text()
        x = int(numb1) if str(numb1).strip() != "" else 0
        y = int(numb2) if str(numb2).strip() != "" else 0
        z = x+y
        self.ui.label_result.setText("Sum is "+str(z))


def mdc_UI_StartView():
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

def regularFunction():
    while True:
        print("AMIT_Goyal")
        time.sleep(10)
def main():
    t1 = threading.Thread(target=regularFunction, args=(),)
    t1.start()
    print("Start")
    mdc_UI_StartView()
    print("ENds")
    
if __name__ == "__main__":
    main()
