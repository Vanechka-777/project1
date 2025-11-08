import io
import sys
import json
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Калькулятор расхода топлива</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>541</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Калькулятор расхода топлива</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QGroupBox" name="groupBox">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>70</y>
      <width>541</width>
      <height>171</height>
     </rect>
    </property>
    <property name="title">
     <string>Ввод данных</string>
    </property>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>40</y>
       <width>151</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Пройденное расстояние (км):</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="distance_input">
     <property name="geometry">
      <rect>
       <x>180</x>
       <y>40</y>
       <width>113</width>
       <height>22</height>
      </rect>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>70</y>
       <width>151</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Израсходовано топлива (л):</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="fuel_input">
     <property name="geometry">
      <rect>
       <x>180</x>
       <y>70</y>
       <width>113</width>
       <height>22</height>
      </rect>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>151</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Цена топлива (руб/л):</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="price_input">
     <property name="geometry">
      <rect>
       <x>180</x>
       <y>100</y>
       <width>113</width>
       <height>22</height>
      </rect>
     </property>
    </widget>
    <widget class="QPushButton" name="calculate_btn">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>40</y>
       <width>191</width>
       <height>28</height>
      </rect>
     </property>
     <property name="text">
      <string>Рассчитать</string>
     </property>
    </widget>
    <widget class="QPushButton" name="clear_btn">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>80</y>
       <width>191</width>
       <height>28</height>
      </rect>
     </property>
     <property name="text">
      <string>Очистить</string>
     </property>
    </widget>
    <widget class="QPushButton" name="history_btn">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>120</y>
       <width>191</width>
       <height>28</height>
      </rect>
     </property>
     <property name="text">
      <string>История расчетов</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="groupBox_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>250</y>
      <width>541</width>
      <height>191</height>
     </rect>
    </property>
    <property name="title">
     <string>Результаты расчета</string>
    </property>
    <widget class="QLabel" name="label_5">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>40</y>
       <width>191</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Расход топлива на 100 км:</string>
     </property>
    </widget>
    <widget class="QLabel" name="consumption_result">
     <property name="geometry">
      <rect>
       <x>220</x>
       <y>40</y>
       <width>121</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>0.00 л/100км</string>
     </property>
     <property name="font">
      <font>
       <bold>true</bold>
      </font>
     </property>
    </widget>
    <widget class="QLabel" name="label_7">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>70</y>
       <width>191</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Стоимость поездки:</string>
     </property>
    </widget>
    <widget class="QLabel" name="cost_result">
     <property name="geometry">
      <rect>
       <x>220</x>
       <y>70</y>
       <width>121</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>0.00 руб</string>
     </property>
     <property name="font">
      <font>
       <bold>true</bold>
      </font>
     </property>
    </widget>
    <widget class="QLabel" name="label_9">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>191</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Стоимость 1 км:</string>
     </property>
    </widget>
    <widget class="QLabel" name="cost_per_km_result">
     <property name="geometry">
      <rect>
       <x>220</x>
       <y>100</y>
       <width>121</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>0.00 руб/км</string>
     </property>
     <property name="font">
      <font>
       <bold>true</bold>
      </font>
     </property>
    </widget>
    <widget class="QLabel" name="label_11">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>130</y>
       <width>191</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Дата расчета:</string>
     </property>
    </widget>
    <widget class="QLabel" name="date_result">
     <property name="geometry">
      <rect>
       <x>220</x>
       <y>130</y>
       <width>191</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>-</string>
     </property>
    </widget>
    <widget class="QPushButton" name="save_btn">
     <property name="geometry">
      <rect>
       <x>350</x>
       <y>40</y>
       <width>171</width>
       <height>28</height>
      </rect>
     </property>
     <property name="text">
      <string>Сохранить расчет</string>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

history_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>HistoryWindow</class>
 <widget class="QMainWindow" name="HistoryWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>История расчетов</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>661</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>История расчетов расхода топлива</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QTableWidget" name="history_table">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>661</width>
      <height>351</height>
     </rect>
    </property>
    <property name="columnCount">
     <number>6</number>
    </property>
    <property name="rowCount">
     <number>0</number>
    </property>
   </widget>
   <widget class="QPushButton" name="clear_history_btn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>410</y>
      <width>191</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Очистить историю</string>
    </property>
   </widget>
   <widget class="QPushButton" name="close_btn">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>410</y>
      <width>191</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Закрыть</string>
    </property>
   </widget>
   <widget class="QPushButton" name="export_btn">
    <property name="geometry">
     <rect>
      <x>255</x>
      <y>410</y>
      <width>191</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Экспорт в файл</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class HistoryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        ui_file = io.StringIO(history_template)
        uic.loadUi(ui_file, self)

        self.history_table.setHorizontalHeaderLabels([
            "Дата", "Расстояние (км)", "Топливо (л)", "Цена (руб/л)",
            "Расход (л/100км)", "Стоимость (руб)"
        ])

        self.clear_history_btn.clicked.connect(self.clear_history)
        self.close_btn.clicked.connect(self.close)
        self.export_btn.clicked.connect(self.export_to_file)

        self.load_history()

    def load_history(self):
        try:
            with open('.venv/fuel_history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)

            self.history_table.setRowCount(len(history))

            for row, record in enumerate(history):
                self.history_table.setItem(row, 0, QTableWidgetItem(record['date']))
                self.history_table.setItem(row, 1, QTableWidgetItem(str(record['distance'])))
                self.history_table.setItem(row, 2, QTableWidgetItem(str(record['fuel'])))
                self.history_table.setItem(row, 3, QTableWidgetItem(str(record['price'])))
                self.history_table.setItem(row, 4, QTableWidgetItem(f"{record['consumption']:.2f}"))
                self.history_table.setItem(row, 5, QTableWidgetItem(f"{record['cost']:.2f}"))

        except FileNotFoundError:
            QMessageBox.information(self, "Информация", "История расчетов пуста")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки истории: {str(e)}")

    def clear_history(self):
        reply = QMessageBox.question(self, "Подтверждение",
                                     "Вы уверены, что хотите очистить всю историю?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                with open('.venv/fuel_history.json', 'w', encoding='utf-8') as f:
                    json.dump([], f)
                self.history_table.setRowCount(0)
                QMessageBox.information(self, "Успех", "История очищена")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка очистки истории: {str(e)}")

    def export_to_file(self):
        try:
            with open('fuel_history_export.txt', 'w', encoding='utf-8') as f:
                f.write("История расчетов расхода топлива\n")
                f.write("=" * 50 + "\n")

                with open('.venv/fuel_history.json', 'r', encoding='utf-8') as history_file:
                    history = json.load(history_file)

                for record in history:
                    f.write(f"Дата: {record['date']}\n")
                    f.write(f"Расстояние: {record['distance']} км\n")
                    f.write(f"Топливо: {record['fuel']} л\n")
                    f.write(f"Цена: {record['price']} руб/л\n")
                    f.write(f"Расход: {record['consumption']:.2f} л/100км\n")
                    f.write(f"Стоимость: {record['cost']:.2f} руб\n")
                    f.write("-" * 30 + "\n")

            QMessageBox.information(self, "Успех", "Данные экспортированы в файл fuel_history_export.txt")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка экспорта: {str(e)}")


class FuelCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)

        self.history_window = None

        self.calculate_btn.clicked.connect(self.calculate_consumption)
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.history_btn.clicked.connect(self.show_history)
        self.save_btn.clicked.connect(self.save_calculation)

        self.current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        self.date_result.setText(self.current_date)

    def validate_inputs(self):
        try:
            distance = float(self.distance_input.text().replace(',', '.'))
            fuel = float(self.fuel_input.text().replace(',', '.'))
            price = float(self.price_input.text().replace(',', '.'))

            if distance <= 0 or fuel <= 0 or price <= 0:
                raise ValueError("Значения должны быть положительными")

            return distance, fuel, price

        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода",
                                "Пожалуйста, введите корректные числовые значения во все поля")
            return None, None, None

    def calculate_consumption(self):
        distance, fuel, price = self.validate_inputs()

        if distance is None:
            return

        consumption_per_100km = (fuel / distance) * 100
        total_cost = fuel * price
        cost_per_km = total_cost / distance

        self.consumption_result.setText(f"{consumption_per_100km:.2f} л/100км")
        self.cost_result.setText(f"{total_cost:.2f} руб")
        self.cost_per_km_result.setText(f"{cost_per_km:.2f} руб/км")

        self.current_calculation = {
            'distance': distance,
            'fuel': fuel,
            'price': price,
            'consumption': consumption_per_100km,
            'cost': total_cost,
            'cost_per_km': cost_per_km
        }

    def clear_inputs(self):
        self.distance_input.clear()
        self.fuel_input.clear()
        self.price_input.clear()
        self.consumption_result.setText("0.00 л/100км")
        self.cost_result.setText("0.00 руб")
        self.cost_per_km_result.setText("0.00 руб/км")
        self.date_result.setText("-")

    def save_calculation(self):
        if not hasattr(self, 'current_calculation'):
            QMessageBox.warning(self, "Предупреждение", "Сначала выполните расчет")
            return

        try:
            try:
                with open('.venv/fuel_history.json', 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except FileNotFoundError:
                history = []

            record = {
                'date': datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                'distance': self.current_calculation['distance'],
                'fuel': self.current_calculation['fuel'],
                'price': self.current_calculation['price'],
                'consumption': self.current_calculation['consumption'],
                'cost': self.current_calculation['cost'],
                'cost_per_km': self.current_calculation['cost_per_km']
            }

            history.append(record)

            with open('.venv/fuel_history.json', 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)

            QMessageBox.information(self, "Успех", "Расчет сохранен в историю")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {str(e)}")

    def show_history(self):
        if self.history_window is None:
            self.history_window = HistoryWindow(self)
        self.history_window.show()
        self.history_window.load_history()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = FuelCalculator()
    calculator.show()

    sys.exit(app.exec_())

