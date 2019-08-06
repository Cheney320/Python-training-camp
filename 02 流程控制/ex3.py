"""
练习三：
写一个根据当日日期来说明是否上班的程序，请用户输入日期来获取
"""

import datetime

def get_week_day(date):
  week_day_dict = {
    0 : 'Monday',
    1 : 'Tuesday',
    2 : 'Wednesday',
    3 : 'Thursday',
    4 : 'Friday',
    5 : 'Saturday',
    6 : 'Sunday',
  }
  day = date.weekday()
  return week_day_dict[day]

date = input("input date(%Y-%m-%d)>>")
date = datetime.datetime.strptime(date, "%Y-%m-%d")
if get_week_day(date) in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
    print("上班")
if get_week_day(date) in ['Saturday','Sunday']:
    print("出去浪")

