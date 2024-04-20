import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from PyQt6.QtGui import QIcon



class NewApp(QWidget) : # NewApp 은 QWidget을 상속 받는다
  # 생성자 
  def __init__(self):
    super().__init__() #상속받은 부모의 메서드 호출 -> __init__은 생성자
    # 즉 super를 통해 QWidget을 메모리에 올림
    self.initUI() #UI 초기화

  def initUI(self) : 
    layout = QVBoxLayout()
    self.setWindowTitle("APP")
    self.resize(300,300)
    self.setLayout(layout)
    self.show()
    self.setWindowIcon(QIcon("StatusBarButtonImage@2x.png"))

if __name__ == "__main__" :
  app = QApplication(sys.argv)
  widget = NewApp()
  widget.show()
  sys.exit(app.exec())
    
  
    