# -*- coding: utf-8 -*-            
# @Author : ManTang
# @Time : 2023/9/28
# @Status : developing
# @Context : 输入打卡时间和工作时间直接输出可以下班的时间点

from datetime import datetime, timedelta


class WorkTime(object):
    def __init__(self, start_time, work_hours):
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.work_hours = float(work_hours)

    def calculate_end_time(self):
        end_time = self.start_time + timedelta(hours=self.work_hours)

        return end_time.strftime("%H:%M")


if __name__ == "__main__":
    start_time = input("输入今天的打卡时间：")
    work_hours = input("今天需要工作的时长：")

    work_time = WorkTime(start_time, work_hours)

    # 计算下班时间
    end_time = work_time.calculate_end_time()

    # 输出下班时间
    print(f"下班时间为：{end_time}")
