'''
A program to add day and temp of that day to a dictionary
The function will add the temp if only the temp for that day is not found
Example: 
If I have already added wednesday it won't add any other temp to wednesday in dictionary
'''

#Function to add temp to dictionary
def add_daily_temp(temps_dic, day, temp):
    #Checks if day is in dic if not it updates it else reutrns it
    if day not in temps_dic:
        temps_dic[day] = temp
    return temps_dic

#Initializing dic
temps_dic = {}
#Using function add to dic
add_daily_temp(temps_dic, day="Saturday", temp=10)
add_daily_temp(temps_dic, day="Sunday", temp=10)
add_daily_temp(temps_dic, day="Monday", temp=13)
add_daily_temp(temps_dic, day="Tuesday", temp=32)
#Checking if the program works as intended
add_daily_temp(temps_dic, day="Wednesday", temp=45)
add_daily_temp(temps_dic, day="Wednesday", temp=15)


print(temps_dic)