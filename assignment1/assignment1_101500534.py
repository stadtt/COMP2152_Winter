"""
Author: Shaffaq Hai
Assignment 1
"""

gym_member = "Alex Alliton" #string
preferred_weight = 20.5 #float
highest_reps = 20 #integer
membership_active = True

#dictonary with string key and values of tuples of ints
workout_stats = {"Alex": (30,45,29), "Jamie":(10,14,20), "Taylor":(40,50,30)}
workout_total = {}

for member,value in workout_stats.items():
    sum_tuples = sum(value)
    workout_total[member+"_Total"] = sum_tuples

workout_stats.update(workout_total)
print(workout_stats)

workout_stats = {"Alex": (30,45,29), "Jamie":(10,14,20), "Taylor":(40,50,30)}



#converting my tuple into a list and then adding it to my list
workout_list = []
for value in workout_stats.values():
        value = list(value)
        workout_list.append(value)

print(workout_list)
'''
for i in range(3):
    for j in range(1):
        print(workout_list[i][j])

for i in range(1,3):
    print(workout_list[i][2])
'''

print(f"Alex's Yoga time:  {workout_list[0][0]}")
print(f"Jamie's Yoga time:   {workout_list[1][0]}")
print(f"Taylor's Yoga time:   {workout_list[2][0]}")

print(f"Jamie's Yoga time:   {workout_list[1][2]}")
print(f"Taylor's Yoga time:   {workout_list[2][2]}")

for key, value in workout_stats.items():
    if sum(value) >= 120:
        print(f"Great Job staying active {key}! ")

print("Please Enter a friends Name")
name = input().lower()
print(name)

for names,value in workout_stats.items():
    if names == name.lower():
        print("Is in the system")
        sum = sum(value)
        print(f"{name}, worked out for  {sum} minutes total, {value} ")

