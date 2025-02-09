"""
Author: Shaffaq Hai
Assignment 1
"""

#B
gym_member = "Alex Alliton" #string
preferred_weight = 20.5 #float
highest_reps = 20 #integer
membership_active = True #bool

#c
#dictonary with string key and values of tuples of ints
workout_stats = {"Alex": (30,45,29), "Jamie":(10,14,20), "Taylor":(40,50,30)}

#d
workout_total = {}
for member,value in workout_stats.items():
    sum_tuples = sum(value)
    workout_total[member+"_Total"] = sum_tuples

workout_stats.update(workout_total)
print(workout_stats)

workout_stats = {"alex": (30,45,29), "jamie":(10,14,20), "taylor":(40,50,30)}


#E
#converting my tuple into a list and then adding it to my list

workout_list = []
for value in workout_stats.values():
        value = list(value)
        workout_list.append(value)

print(workout_list)

#F
print("Name: Yoga, Running")
for member,value in workout_stats.items():
    print(member, value[0:2])

print("Weightlifting:")
for member,value in list(workout_stats.items())[1:]:
    print(member, value[-1])


#G
for key, value in workout_stats.items():
    if sum(value) >= 120:
        print(f"Great Job staying active {key}! ")


#H
print("Please Enter a Friends Name")
name = input().lower()
print(name)

check = True
for names,value in workout_stats.items():
    if(name == names):
        print(name + " is in the system")
        check = False
        sum_tuple = sum(value)
        print(f" Yoga   {workout_stats[name][0]}")
        print(f" Running   {workout_stats[name][1]}")
        print(f" Weightlifting  {workout_stats[name][2]}")
        print(f"{name}, worked out for  {sum_tuple} minutes total")

if check:
    print(f"Friend {name} not found in the records")


#i

newDict = {}
for names,values in workout_stats.items():
        sum_tuples = sum(values)
        newDict[names] = sum_tuples


print(newDict)
max_key = max(newDict.values())
min_key = min(newDict.values())
for key in newDict:
    if newDict[key] == max_key:
        print(  f"Highest total workout minutes " + key, newDict[key])

for key in newDict:
    if newDict[key] == min_key:
        print(f"Lowest total workout minutes " + key, newDict[key])




