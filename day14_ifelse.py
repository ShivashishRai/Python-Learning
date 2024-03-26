
#Date and if else condition
#if else

import datetime

time_of_day = datetime.datetime.now()
current_time = time_of_day.hour
#print(time_of_day.date)
print(current_time)

if 4 < current_time <12:
    print("Good Morning")

elif 12 < current_time < 17:
    print("Good Afternoon ")

else:
    print("Good Night")


