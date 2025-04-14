'''
The same program as question 9 but prompts user for the data
'''

#Function add to dic
def add_daily_temp(temps_dic, day, temp):
    if day in temps_dic:
        temps_dic[day] = temp
    return temps_dic

#Initialize the dic with all the key vairables
temps_dic = {
    "Sunday": " ",
    "Monday": " ",
    "Tuesday": " ",
    "Wednesday": " ",
    "Thursday": " ",
    "Friday": " ",
    "Saturday": " "
}

#Using loop to get temp for all days
for keys in temps_dic:
    #Another loop to ensure user has inputed correct data
    while True:
        try:
            temp = float(input(f"Enter the temperature for day {keys}: "))
            add_daily_temp(temps_dic, keys,  temp)
            break
        except ValueError:
            print("Enter number for temperature")
            
    

print("Temperatur data: \n",temps_dic)