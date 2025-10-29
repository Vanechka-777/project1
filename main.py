import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Калькулятор расхода топлива</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QTabWidget" name="tabWidget">
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="calc_tab">
       <attribute name="title">
        <string>Расчет расхода</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QLabel" name="label">
          <property name="text">
           <string>Расчет расхода топлива (л/100км)</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout">
          <item>
           <widget class="QLabel" name="label_2">
            <property name="text">
             <string>Пройденное расстояние (км):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="distance_input"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <widget class="QLabel" name="label_3">
            <property name="text">
             <string>Потрачено топлива (л):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="fuel_input"/>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QPushButton" name="calculate_btn">
          <property name="text">
           <string>Рассчитать расход</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="result_label">
          <property name="text">
           <string>Результат:</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="cost_tab">
       <attribute name="title">
        <string>Стоимость поездки</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <item>
         <widget class="QLabel" name="label_4">
          <property name="text">
           <string>Расчет стоимости поездки</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_3">
          <item>
           <widget class="QLabel" name="label_5">
            <property name="text">
             <string>Расстояние (км):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="cost_distance_input"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_4">
          <item>
           <widget class="QLabel" name="label_6">
            <property name="text">
             <string>Расход (л/100км):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="consumption_input"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_5">
          <item>
           <widget class="QLabel" name="label_7">
            <property name="text">
             <string>Цена топлива (руб/л):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="price_input"/>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QPushButton" name="calculate_cost_btn">
          <property name="text">
           <string>Рассчитать стоимость</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="cost_result_label">
          <property name="text">
           <string>Результат:</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="refuel_tab">
       <attribute name="title">
        <string>Добавить заправку</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_4">
        <item>
         <widget class="QLabel" name="label_8">
          <property name="text">
           <string>Добавление данных о заправке</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_6">
          <item>
           <widget class="QLabel" name="label_9">
            <property name="text">
             <string>Пройденное расстояние (км):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="refuel_distance_input"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_7">
          <item>
           <widget class="QLabel" name="label_10">
            <property name="text">
             <string>Количество топлива (л):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="refuel_fuel_input"/>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_8">
          <item>
           <widget class="QLabel" name="label_11">
            <property name="text">
             <string>Цена за литр (руб):</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="refuel_price_input"/>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QPushButton" name="add_refuel_btn">
          <property name="text">
           <string>Добавить заправку</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="history_tab">
       <attribute name="title">
        <string>История</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_5">
        <item>
         <widget class="QLabel" name="label_12">
          <property name="text">
           <string>Последние 10 заправок</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QTableWidget" name="history_table">
          <column>
           <property name="text">
            <string>Дата</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Расстояние</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Топливо</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Цена</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Расход</string>
           </property>
          </column>
         </widget>
        </item>
        <item>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.bunon()


    def buton(self):
        self.setWindowTitle("Калькулятор расхода топлива")
        self.calculate_btn.clicked.connect(self.calculate_consumption)
        self.calculate_cost_btn.clicked.connect(self.calculate_cost)
        self.add_refuel_btn.clicked.connect(self.add_refueling)
        self.history_btn.clicked.connect(self.show_history_window)
        self.stats_btn.clicked.connect(self.show_stats_window)
        self.clear_history_btn.clicked.connect(self.clear_history)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow
    ex.show()
    sys.exit(app.exec())