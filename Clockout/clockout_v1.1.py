# -*- coding: utf-8 -*-            
# @Author : ManTang
# @Time : 2023/9/28
# @Status : developing
# @Context : 在实现计算出下班点的基础上加上UI界面

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta


class WorkTimeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("下班时间计算器")
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # 上班时间输入框
        start_label = QLabel("今日上班打卡时间：")
        self.start_time_edit = QLineEdit()
        self.start_time_edit.setAlignment(Qt.AlignCenter)
        layout.addWidget(start_label)
        layout.addWidget(self.start_time_edit)

        # 工作时长输入框
        work_label = QLabel("今日工作时长(h)：")
        self.work_hour_edit = QLineEdit("8.5")
        self.work_hour_edit.setAlignment(Qt.AlignCenter)
        layout.addWidget(work_label)
        layout.addWidget(self.work_hour_edit)

        # 加班时长输入框
        overtime_label = QLabel("今日准备加班时长(h)：")
        self.overtime_edit = QComboBox()
        self.overtime_edit.addItem("0")
        self.overtime_edit.addItem("1")
        self.overtime_edit.addItem("1.5")
        self.overtime_edit.addItem("2")
        self.overtime_edit.addItem("2.5")
        self.overtime_edit.addItem("3")
        self.overtime_edit.addItem("3.5")
        self.overtime_edit.setCurrentIndex(0)
        self.overtime_edit.setEditable(True)  # 将 QComboBox 设置为可编辑模式
        self.overtime_edit.lineEdit().setAlignment(Qt.AlignCenter)  # 设置 QLineEdit 内容居中显示
        layout.addWidget(overtime_label)
        layout.addWidget(self.overtime_edit)

        # 计算按钮
        clockout_label = QLabel("今日下班打卡时间为：")
        self.clockout_edit = QLineEdit()
        self.clockout_edit.setAlignment(Qt.AlignCenter)
        self.calculate_button = QPushButton("计算下班时间")
        self.calculate_button.clicked.connect(self.calculateEndTime)
        layout.addWidget(clockout_label)
        layout.addWidget(self.clockout_edit)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    # 计算下班时间
    def calculateEndTime(self):
        start_time = self.start_time_edit.text()
        if not start_time:
            if not self.show_warning():
                return  # 如果上班打卡时间未填写且用户选择不继续，则不进行下一步计算

        work_hours = float(self.work_hour_edit.text())
        overtime_hours = float(self.overtime_edit.currentText())
        start_time = datetime.strptime(start_time, "%H:%M")

        if overtime_hours > 0:
            work_hours += 1.5
            end_time = start_time + timedelta(hours=work_hours) + timedelta(hours=overtime_hours)
        else:
            end_time = start_time + timedelta(hours=work_hours)
        end_time = end_time.strftime("%H:%M")

        self.clockout_edit.setText(end_time)

        # print(f"下班时间为：{end_time}")

    def show_warning(self):
        reply = QMessageBox.warning(self, "警告", "请输入上班打卡时间", QMessageBox.Ok | QMessageBox.Cancel)  # 弹出警告框
        if reply == QMessageBox.Cancel:  # 如果用户选择继续，则返回 True
            return True
        else:
            self.start_time_edit.setFocus()
            return False


if __name__ == "__main__":
    app = QApplication([])
    window = WorkTimeApp()
    window.show()
    app.exec()
