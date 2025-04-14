def add_daily_temp(temps_dic, day, temp):
    if day not in temps_dic:
        temps_dic[day] = temp
    return temps_dic

temps_dic = {}
add_daily_temp(temps_dic, day="Sunday", temp=10)
add_daily_temp(temps_dic, day="Sunday", temp=10)
add_daily_temp(temps_dic, day="Monday", temp=13)
add_daily_temp(temps_dic, day="Tuesday", temp=32)
add_daily_temp(temps_dic, day="Wednesday", temp=45)

print(temps_dic)