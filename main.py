import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>FuelCalculator</class>
 <widget class="QMainWindow" name="FuelCalculator">
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
      <widget class="QWidget" name="tab_calculator">
       <attribute name="title">
        <string>Расчет расхода</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QGroupBox" name="groupBox">
          <property name="title">
           <string>Параметры поездки</string>
          </property>
          <layout class="QGridLayout" name="gridLayout">
           <item row="0" column="0">
            <widget class="QLabel" name="label">
             <property name="text">
              <string>Расстояние (км):</string>
             </property>
            </widget>
           </item>
           <item row="0" column="1">
            <widget class="QLineEdit" name="distance_input">
             <property name="text">
              <string>100</string>
             </property>
            </widget>
           </item>
           <item row="1" column="0">
            <widget class="QLabel" name="label_2">
             <property name="text">
              <string>Расход топлива (л/100км):</string>
             </property>
            </widget>
           </item>
           <item row="1" column="1">
            <widget class="QLineEdit" name="consumption_input">
             <property name="text">
              <string>8.5</string>
             </property>
            </widget>
           </item>
           <item row="2" column="0">
            <widget class="QLabel" name="label_3">
             <property name="text">
              <string>Цена топлива (руб/л):</string>
             </property>
            </widget>
           </item>
           <item row="2" column="1">
            <widget class="QLineEdit" name="price_input">
             <property name="text">
              <string>50</string>
             </property>
            </widget>
           </item>
           <item row="3" column="0">
            <widget class="QLabel" name="label_4">
             <property name="text">
              <string>Дата поездки:</string>
             </property>
            </widget>
           </item>
           <item row="3" column="1">
            <widget class="QDateEdit" name="date_input"/>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <widget class="QGroupBox" name="groupBox_2">
          <property name="title">
           <string>Результаты расчета</string>
          </property>
          <layout class="QGridLayout" name="gridLayout_2">
           <item row="0" column="0">
            <widget class="QLabel" name="label_5">
             <property name="text">
              <string>Топливо всего (л):</string>
             </property>
            </widget>
           </item>
           <item row="0" column="1">
            <widget class="QLabel" name="fuel_total_label">
             <property name="text">
              <string>0.0</string>
             </property>
            </widget>
           </item>
           <item row="1" column="0">
            <widget class="QLabel" name="label_7">
             <property name="text">
              <string>Стоимость (руб):</string>
             </property>
            </widget>
           </item>
           <item row="1" column="1">
            <widget class="QLabel" name="cost_label">
             <property name="text">
              <string>0.0</string>
             </property>
            </widget>
           </item>
           <item row="2" column="0">
            <widget class="QLabel" name="label_9">
             <property name="text">
              <string>На 1 км (руб):</string>
             </property>
            </widget>
           </item>
           <item row="2" column="1">
            <widget class="QLabel" name="cost_per_km_label">
             <property name="text">
              <string>0.0</string>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout">
          <item>
           <widget class="QPushButton" name="calculate_btn">
            <property name="text">
             <string>Рассчитать</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="save_btn">
            <property name="text">
             <string>Сохранить запись</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="clear_btn">
            <property name="text">
             <string>Очистить</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="tab_history">
       <attribute name="title">
        <string>История расчетов</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_3">
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
            <string>Расход</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Цена</string>
           </property>
          </column>
          <column>
           <property name="text">
            <string>Стоимость</string>
           </property>
          </column>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <widget class="QPushButton" name="delete_btn">
            <property name="text">
             <string>Удалить запись</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="clear_history_btn">
            <property name="text">
             <string>Очистить историю</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="stats_btn">
            <property name="text">
             <string>Статистика</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="tab_statistics">
       <attribute name="title">
        <string>Статистика</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_4">
        <item>
         <widget class="QLabel" name="stats_label">
          <property name="text">
           <string>Статистика будет отображена здесь после расчетов</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QTextEdit" name="stats_text" readonly="true"/>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>28</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Файл</string>
    </property>
    <addaction name="action_export"/>
    <addaction name="separator"/>
    <addaction name="action_exit"/>
   </widget>
   <widget class="QMenu" name="menu_2">
    <property name="title">
     <string>Справка</string>
    </property>
    <addaction name="action_about"/>
   </widget>
   <addaction name="menu"/>
   <addaction name="menu_2"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action_exit">
   <property name="text">
    <string>Выход</string>
   </property>
  </action>
  <action name="action_about">
   <property name="text">
    <string>О программе</string>
   </property>
  </action>
  <action name="action_export">
   <property name="text">
    <string>Экспорт данных</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FuelCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.history_data = []

        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)

        self.setup_validators()
        self.setup_connections()
        self.setup_initial_state()

    def setup_validators(self):
        double_validator = QDoubleValidator(0.01, 10000.0, 2)
        double_validator.setNotation(QDoubleValidator.Notation.StandardNotation)

        price_validator = QDoubleValidator(0.01, 1000.0, 2)
        price_validator.setNotation(QDoubleValidator.Notation.StandardNotation)

        self.distance_input.setValidator(double_validator)
        self.consumption_input.setValidator(double_validator)
        self.price_input.setValidator(price_validator)

    def setup_connections(self):
        self.calculate_btn.clicked.connect(self.calculate_fuel)
        self.save_btn.clicked.connect(self.save_calculation)
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.delete_btn.clicked.connect(self.delete_history_entry)
        self.clear_history_btn.clicked.connect(self.clear_history)
        self.stats_btn.clicked.connect(self.show_statistics)
