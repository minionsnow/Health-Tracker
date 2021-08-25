# -*- coding: utf-8 -*-
class USER:
  def __init__(self,name,sex,age,weight,height):
    self.name = name
    self.sex = sex
    self.age = age
    self.weight = weight
    self.height = height
    self.BMI()

  def BMI(self):
    self.bmi = round(float(self.weight)/(float(self.height)/100)**2,1)
    if self.bmi>25 :
      self.bmi_com = ". Lose some weight!!"
    elif self.bmi>18.5 :
      self.bmi_com = ". Keep up the good work!!"
    else:
      self.bmi_com = ". Try to put on some weight!!"



class WEEKLY_WORKOUT:
  def __init__(self,workout_list):
    self.workout_list = workout_list
    self.Stats()

  def Stats(self):
    self.distance = [round(int(x[1]) * 0.000713,2) for x in self.workout_list]
    self.time = [round(float(y[0]) + float(y[1])/60 + float(y[2])/3600,2) for y in [x[2].split(":") for x in self.workout_list]]
    self.speed = [round(self.distance[i]/self.time[i],2) for i in range(len(self.distance)) if self.time[i]!=0]
    if 0.0 not in self.time: self.award = 1
    else : self.award = 0
    self.longest_dis = max(self.distance)
    self.fastest_speed = max(self.speed)
    self.shortest_dis = min([x for x in self.distance if x!=0])
    self.slowest_speed = min(self.speed)
    if sum(self.time)>0:self.average_speed = round(sum(self.distance)/sum(self.time),2)
    else: self.average_speed = 0.0
    self.average_dis = round(sum(self.distance),2)

class MONTHLY_WORKOUT:
  def __init__(self,workout_list):
    self.workout_list = workout_list
    self.Stats()

  def Stats(self):
    self.award = sum([x.award for x in self.workout_list])
    self.longest_dis = max([x.longest_dis for x in self.workout_list])
    self.fastest_speed = max([x.fastest_speed for x in self.workout_list])
    self.shortest_dis = min([x.shortest_dis for x in self.workout_list])
    self.slowest_speed = min([x.slowest_speed for x in self.workout_list])
    self.average_speed = round(sum([x.average_speed for x in self.workout_list])/len(self.workout_list),2)
    self.average_dis = round(sum([x.average_dis for x in self.workout_list])/len(self.workout_list),2)

class OVERALL_WORKOUT:
  def __init__(self,workout_list):
    self.workout_list = workout_list
    self.Stats()

  def Stats(self):
    self.award = sum([1 for x in self.workout_list if x.award==4])
    self.longest_dis = max([x.longest_dis for x in self.workout_list])
    self.fastest_speed = max([x.fastest_speed for x in self.workout_list])
    self.shortest_dis = min([x.shortest_dis for x in self.workout_list])
    self.slowest_speed = min([x.slowest_speed for x in self.workout_list])
    self.average_speed = round(sum([x.average_speed for x in self.workout_list])/len(self.workout_list),2)
    self.average_dis = round(sum([x.average_dis for x in self.workout_list])/len(self.workout_list),2)

def display(user,flag,workout):
  if user.sex=='Male':print("Hi Mr." + user.name)
  else : print("Hi Miss." + user.name)
  print("Your BMI is: "+ str(user.bmi) + user.bmi_com)
  if flag == 1:
    print("Your Weekly achievement is as follows:")
    if workout.award>0 : print("No breakout in Sessions: You get a 7/7 award")
  elif flag == 2:
    print("Your Monthly achievement is as follows:")
    if workout.award>0 : print("Congrats! You have got a {} 7/7 award for this month".format(workout.award))
  elif flag == 3:
    print("Your Overall achievement is as follows:")
    if workout.award>0 : print("Congrats! You have got a {} M/M award for this month".format(workout.award))
  print("Your Fastest Speed is: "+  str(workout.fastest_speed) + " km/hr")
  print("Your Longest Distance is: "+ str(workout.longest_dis) + " km")
  print("Your Slowest Speed is: "+ str(workout.slowest_speed) + " km/hr")
  print("Your Shortest Distance is: "+ str(workout.shortest_dis) + " km")
  if flag==1:
      print("Your Weekly Average Speed is: "+ str(workout.average_speed) + " km/hr")
      print("Your Weekly Average Distance is: "+ str(workout.average_dis) + " km")
  elif flag==2:
      print("Your Monthly Average Speed is: "+ str(workout.average_speed) + " km/hr")
      print("Your Monthly Average Distance is: "+ str(workout.average_dis) + " km")
  else:
      print("Your Overall Average Speed is: "+ str(workout.average_speed) + " km/hr")
      print("Your Overall Average Distance is: "+ str(workout.average_dis) + " km")

if __name__=="__main__":
  print("Input - - - - - -")
  name = input("Name : ")
  sex = input("Sex : ")
  age = input("Age (years) : ")
  weight = input("Weight (Kg) : ")
  height = input("Height (cms) : ")
  user = USER(name,sex,age,weight,height)

  print("\nWorkout Input- - - - - - -")
  num_days = 0
  num_weeks = 0
  num_months = 0
  week_lis = []
  month_lis = []
  overall_lis = []
  file = open("user.txt","r")
  Data = file.readlines()
  for x in Data:
      print(x)
  print("\n")

  for line in Data:
    user_day = [x.strip() for x in line.split(",")]
    week_lis.append(user_day)
    num_days+=1

    if num_days == 7:
      num_days = 0
      num_weeks+=1
      weekly_workout = WEEKLY_WORKOUT(week_lis)
      month_lis.append(weekly_workout)
      week_lis.clear()

    if num_weeks == 4:
      num_weeks = 0
      num_months += 1
      monthly_workout = MONTHLY_WORKOUT(month_lis)
      overall_lis.append(monthly_workout)
      month_lis.clear()


  if len(overall_lis)>0:
    overall_workout = OVERALL_WORKOUT(overall_lis)
    display(user,3,overall_workout)
  elif len(month_lis)>1:
    monthly_workout = MONTHLY_WORKOUT(month_lis)
    display(user,2,monthly_workout)
  else:
    display(user,1,weekly_workout)
