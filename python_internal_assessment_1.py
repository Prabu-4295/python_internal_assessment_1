# -*- coding: utf-8 -*-
"""python_internal_assessment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xSetwDIHvu45S1sAEO8UI_citV9a0YEW
"""

# 1.Area of a rectangle

def area_of_rectangle(length,width):
  return length*width

length=int(input("Enter the length: "))
width=int(input("Enter the width: "))

rectangle_area=area_of_rectangle(length,width)
print("Area of the rectangle is : ",rectangle_area)5

#2 Calculate BMI

def calculate_BMI(weight,height):
  return weight/(height*height)

weight=float(input("Enter your weight(kgs): "))
height=float(input("Enter your height(mtr): "))

bmi_value=calculate_BMI(weight,height)
print("You BMI Value is : ",bmi_value)

#3 use Dictionary to store the data of students and scores

names_scores={"prabu":80,"rishab":75,"keerthana":100,"suriyapriya":90,"sivaganes":50}
print(names_scores)

#4 Ask Age and find minor ,adult or senior

def check_age(age):
  if(age<18):
    return "The person is Minor"
  elif(age<30):
    return "The person is an adult"
  else:
    return "The person is a senior citizen"

input_age=int(input("enter your age : "))

check_age(input_age)

#5 print all the even numbers between 1 and 50 using for loop

for i in range(50):
  if(i%2==0 and i!=0):
    print(i)

#6 develop a password prompt

print("Create username & password")
user_name=str(input("Enter username : "))
password=str(input("Enter Strong Password : "))

print("-----Login Page-----")
while True:
  user=str(input("Enter username : "))
  pass_word=str(input("Enter password : "))
  if(user==user_name and pass_word==password):
    print("Login Successfull, Welcome ...")
    break;
  else:
    print("**Enter Correct username or password**")

#7 function to calculate list of numbers


def calculate_average(list):
  sum=0
  count=0
  for i in list:
    sum+=i
    count+=1
  return sum/count

list=[10,25,35,45,50]
for i in list:
  print(i," ")
average_value=calculate_average(list)
print("The average is ",average_value)

#8 function to count the no of vowels in a string

def count_vowels(input_string):
  count=0
  for i in input_string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
      count+=1
    else:
      continue
  return count

given_string=str(input("Enter a String : "))
print("No of vowels in the given string : ",count_vowels(given_string))

#9 datetime module
import datetime
print("Toady's date and time : ",datetime.datetime.now())

#10 handle non numeric characters to add two numbers

var1=int(input("Enter the number 1: "))
var2=str(input("Enter the number 2: "))
var3=0
try:
    var3=var1+var2

except:
    print("**Enter numeric values to add two numbers**")

#11 create input propmt with valuetype Error

try:
  var1=int(input("Enter a number : "))
  print("the value is  ",var1)
except:
  print("** enter a integer value **")

#12 division by zero error

var1=int(input("Enter a number : "))
var2=int (input("Enter a number : "))
try:
  var3= var1/var2
  print("The divided value is ",var3)
except:
  print("** Cannot divide a value by 0 , Enter non-zero values for division**")

#13 create a script and write

file_open=open("sample\\data\\python.txt",'w')
script="Hello python !"

file_open.write(script)
print(file_open.read())

#14 read and print the content from the file

file_read=open("sample\\data\\python.txt",'r')
print(file_read.read())

#15 write in the file add another line

text_file = open('sample\\data\\python.txt','w')
list= []
for i in range (1, 5):
    varline = input("Enter data to be written : ")
    list.append(varline)
text_file.writelines(list)
text_file.close()