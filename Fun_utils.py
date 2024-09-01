import os
import datetime

#command = "df -h"
#command = "uptime"
#command = "free -h"
#command = "date"

def fun(command):
    return os.system(command)

def show_date():
    return datetime.datetime.today()

fun("date")     
fun("free")
fun("uptime")
fun("df -h")

today_date = show_date()
print(today_date)

