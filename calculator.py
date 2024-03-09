import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label_num1 = QLabel("First Number:")
        layout.addWidget(label_num1)

        self.num1_input = QLineEdit()
        self.num1_input.setPlaceholderText("Enter first number")
        layout.addWidget(self.num1_input)

        label_operation = QLabel("Operation (+, -, *, /):")
        layout.addWidget(label_operation)

        self.operation_input = QLineEdit()
        self.operation_input.setPlaceholderText("Enter operation")
        layout.addWidget(self.operation_input)

        label_num2 = QLabel("Second Number:")
        layout.addWidget(label_num2)

        self.num2_input = QLineEdit()
        self.num2_input.setPlaceholderText("Enter second number")
        layout.addWidget(self.num2_input)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        layout.addWidget(calculate_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        layout.addWidget(clear_button)

        self.setLayout(layout)

    def calculate(self):
        num1_text = self.num1_input.text()
        num2_text = self.num2_input.text()
        operation = self.operation_input.text()

        if not num1_text or not num2_text or not operation:
            self.result_label.setText("Please fill in all fields.")
            return

        try:
            num1 = float(num1_text)
            num2 = float(num2_text)

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    result = "Error: Division by zero!"
                else:
                    result = num1 / num2
            else:
                result = "Invalid operation"

            self.result_label.setText("Result: " + str(result))
        except ValueError:
            self.result_label.setText("Please enter valid numbers.")

    def clear(self):
        self.num1_input.clear()
        self.operation_input.clear()
        self.num2_input.clear()
        self.result_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
