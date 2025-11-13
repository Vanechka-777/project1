import io
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>650</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Калькулятор расхода топлива</string>
  </property>
  <property name="styleSheet">
   <string notr="true">
   QMainWindow {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #E3F2FD, stop: 1 #BBDEFB);
   }
   QGroupBox {
    font-weight: bold;
    border: 2px solid #1976D2;
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 10px;
    background-color: rgba(255, 255, 255, 200);
   }
   QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
    color: #1976D2;
   }
   QPushButton {
    background-color: #2196F3;
    border: none;
    color: white;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: bold;
   }
   QPushButton:hover {
    background-color: #1976D2;
   }
   QPushButton:pressed {
    background-color: #0D47A1;
   }
   QPushButton#calculate_btn {
    background-color: #4CAF50;
   }
   QPushButton#calculate_btn:hover {
    background-color: #45a049;
   }
   QPushButton#clear_btn {
    background-color: #f44336;
   }
   QPushButton#clear_btn:hover {
    background-color: #da190b;
   }
   QPushButton#save_btn {
    background-color: #FF9800;
   }
   QPushButton#save_btn:hover {
    background-color: #e68900;
   }
   QLineEdit {
    padding: 6px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: white;
   }
   QLabel {
    color: #333;
   }
   </string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>591</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>⛽ Калькулятор расхода топлива</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="image_label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>591</width>
      <height>101</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QGroupBox" name="groupBox">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>190</y>
      <width>591</width>
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
      <string>🧮 Рассчитать</string>
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
      <string>🗑️ Очистить</string>
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
      <string>📊 История расчетов</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="groupBox_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>370</y>
      <width>591</width>
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
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>0.00 л/100км</string>
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
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>0.00 руб</string>
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
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>0.00 руб/км</string>
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
      <string/>
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
      <string>💾 Сохранить расчет</string>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class DatabaseManager:
    def __init__(self):
        self.db_name = "fuel_calculator.db"
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fuel_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                distance REAL NOT NULL,
                fuel REAL NOT NULL,
                price REAL NOT NULL,
                consumption REAL NOT NULL,
                cost REAL NOT NULL,
                cost_per_km REAL NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def save_calculation(self, record):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO fuel_history 
            (date, distance, fuel, price, consumption, cost, cost_per_km)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            record['date'], record['distance'], record['fuel'],
            record['price'], record['consumption'], record['cost'],
            record['cost_per_km']
        ))

        conn.commit()
        conn.close()

    def get_all_history(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT date, distance, fuel, price, consumption, cost, cost_per_km
            FROM fuel_history 
            ORDER BY date DESC
        ''')

        records = cursor.fetchall()
        conn.close()

        return records

    def clear_history(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('DELETE FROM fuel_history')

        conn.commit()
        conn.close()


class HistoryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.db = DatabaseManager()

        ui_file = io.StringIO(history_template)
        uic.loadUi(ui_file, self)

        self.history_table.setHorizontalHeaderLabels([
            "Дата", "Расстояние (км)", "Топливо (л)", "Цена (руб/л)",
            "Расход (л/100км)", "Стоимость (руб)", "Цена 1 км (руб)"
        ])

        self.history_table.setAlternatingRowColors(True)
        self.history_table.setSortingEnabled(True)
        self.history_table.horizontalHeader().setStretchLastSection(True)

        self.clear_history_btn.clicked.connect(self.clear_history)
        self.close_btn.clicked.connect(self.close)
        self.export_btn.clicked.connect(self.export_to_file)

        self.load_history()

    def load_history(self):
        try:
            records = self.db.get_all_history()

            self.history_table.setRowCount(len(records))

            for row, record in enumerate(records):
                self.history_table.setItem(row, 0, QTableWidgetItem(record[0]))
                self.history_table.setItem(row, 1, QTableWidgetItem(str(record[1])))
                self.history_table.setItem(row, 2, QTableWidgetItem(str(record[2])))
                self.history_table.setItem(row, 3, QTableWidgetItem(str(record[3])))
                self.history_table.setItem(row, 4, QTableWidgetItem(f"{record[4]:.2f}"))
                self.history_table.setItem(row, 5, QTableWidgetItem(f"{record[5]:.2f}"))
                self.history_table.setItem(row, 6, QTableWidgetItem(f"{record[6]:.2f}"))

            if not records:
                QMessageBox.information(self, "Информация", "История расчетов пуста")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки истории: {str(e)}")

    def clear_history(self):
        reply = QMessageBox.question(self, "Подтверждение",
                                     "Вы уверены, что хотите очистить всю историю?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                self.db.clear_history()
                self.history_table.setRowCount(0)
                QMessageBox.information(self, "Успех", "История очищена")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка очистки истории: {str(e)}")

    def export_to_file(self):
        try:
            records = self.db.get_all_history()

            if not records:
                QMessageBox.information(self, "Информация", "Нет данных для экспорта")
                return

            with open('fuel_history_export.txt', 'w', encoding='utf-8') as f:
                f.write("История расчетов расхода топлива\n")
                f.write("=" * 60 + "\n\n")

                for record in records:
                    f.write(f"Дата: {record[0]}\n")
                    f.write(f"Расстояние: {record[1]} км\n")
                    f.write(f"Топливо: {record[2]} л\n")
                    f.write(f"Цена: {record[3]} руб/л\n")
                    f.write(f"Расход: {record[4]:.2f} л/100км\n")
                    f.write(f"Стоимость поездки: {record[5]:.2f} руб\n")
                    f.write(f"Стоимость 1 км: {record[6]:.2f} руб\n")
                    f.write("-" * 40 + "\n")

            QMessageBox.information(self, "Успех", "Данные экспортированы в файл fuel_history_export.txt")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка экспорта: {str(e)}")


class FuelCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)

        self.db = DatabaseManager()
        self.history_window = None

        self.calculate_btn.clicked.connect(self.calculate_consumption)
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.history_btn.clicked.connect(self.show_history)
        self.save_btn.clicked.connect(self.save_calculation)


        self.create_simple_image()

    def create_simple_image(self):
        from PyQt5.QtGui import QPainter
        from PyQt5.QtCore import QRect

        pixmap = QPixmap(591, 100)
        pixmap.fill(Qt.white)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(Qt.blue)
        painter.drawRect(200, 40, 200, 30)
        painter.drawRect(220, 20, 160, 20)

        painter.setBrush(Qt.black)
        painter.drawEllipse(220, 60, 30, 30)
        painter.drawEllipse(350, 60, 30, 30)

        painter.setPen(Qt.red)
        painter.setFont(painter.font())
        painter.drawText(QRect(0, 0, 591, 100), Qt.AlignCenter, "⛽ КАЛЬКУЛЯТОР РАСХОДА ТОПЛИВА 🚗")

        painter.end()
        self.image_label.setPixmap(pixmap)

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
            record = {
                'distance': self.current_calculation['distance'],
                'fuel': self.current_calculation['fuel'],
                'price': self.current_calculation['price'],
                'consumption': self.current_calculation['consumption'],
                'cost': self.current_calculation['cost'],
                'cost_per_km': self.current_calculation['cost_per_km']
            }

            self.db.save_calculation(record)
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
