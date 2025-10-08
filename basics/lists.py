calendar_month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"]

for month in calendar_month_list:
    print(month)

calendar_month_list.append("November")
calendar_month_list.sort()
calendar_month_list.remove("June")
calendar_month_list.append("December")

print("After sort \n")
print(calendar_month_list)
