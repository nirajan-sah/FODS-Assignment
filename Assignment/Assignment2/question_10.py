def add_daily_temp(temps_dic, day, temp):
    if day in temps_dic:
        temps_dic[day] = temp
    return temps_dic

temps_dic = {
    "Sunday": " ",
    "Monday": " ",
    "Tuesday": " ",
    "Wednesday": " ",
    "Thursday": " ",
    "Friday": " ",
    "Saturday": " "
}
for keys in temps_dic:
    temp = float(input(f"Enter the temperature for day {keys}: "))
    add_daily_temp(temps_dic, keys,  temp)

print(temps_dic)