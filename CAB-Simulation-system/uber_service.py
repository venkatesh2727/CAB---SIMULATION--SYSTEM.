#yatinhomkar@hotmail.com
#Version 1 assignment.
#********Welcome to uber service********
#Sr No.        Car Type       Capacity     Rate
#1             Mini               4        Rs. 20/Km
#2             BIG                5        Rs. 25/km
#3             Sedan              3        Rs. 50/Km
#**********Available Routes**********
#Sr No.        Route
#1             Swargate-Kothrud
#2             Kothrud-Swargate
#************************************
#Source = Swargate
#Destination = Kothrud
#Car Type = Mini,BIG,Sedan


#Distance between Swargate and Kothrud is 15 km
#Rs 20*15 = Rs.300 base fare.

#Do you want to book ride - yes/no
#if Yes
#Passenger name =
#Passenger Mobile =
#Passenger E-mail = 

#Thanks for booking Ride with us.Driver will come soon to your pick up Point.

#************Your Last Ride Bill********
# import Random Function use 6 digit ID number.
#Date -
#Ride Number -

#Passenger name =
#Passenger Mobile =
#Passenger E-mail = 
#Base Fare = 20*15 = Rs.300
#9% CGST = Rs.27
#9% CGST = Rs.27
# Total Fare = Rs. 354
#

#**********Thanks for riding with us**********
# import tabulate functions new
#venv
# mini Project.
#create a pdf receipt of it
#program .exe

print('***********Welcome to Uber Service************')
from tabulate import tabulate


mydata = [
    [1,'Mini','4','Rs.20/Km'], 
    [2,'BIG','5','Rs.25/Km'],
    [3,'Sedan','6','Rs.50/Km'],
   
]
 
head = ["Sr No.", "Car" , "Capacity" , "Rate"]
 
print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))

print('***************Available Route*********************')
f = ("Flat 20% promocode off")
print(f.center(50,'*')) 
from tabulate import tabulate

a = [
    [1,'kothrud to swargate'],
    [2,'swargate to kothrud'],
    [3,'swargate to hadapsar'],
    [4,'hadapsar to deccan'],
    [5,'deccan to nigdi'],
    [6,'talegaon to pune']
]
head = ['Sr No.','Routes']
print(tabulate(a, headers=head, tablefmt="fancy_grid"))
print('****************************************************')

routes = {'kothrud to swargate':20,'swargate to kothrud':15,'swargate to hadapsar':20,'hadapsar to deccan':25,
         'deccan to nigdi':20,'talegaon to pune':35}
list_routes = routes.keys()
print(list_routes)
for a in list_routes:
    print(a)
print('*************************************')
b = input('Do you want to book a ride (yes/no):  ')

if b.lower()=='yes':
      no1 = input('Enter Your Name = ')
      no2 = input('Enter your Mobile No. = ')
      no3 = input('Enter your E-mail ID =  ')
      no4 = input('Enter your car type =   ')
      source = input('Enter Source =   ')
      source_lower=source.lower()
      Destination = input('Enter Destination =   ')
      Destination_lower = Destination.lower()
      c = source_lower +' to '+Destination_lower
      c = c
      if c in routes.keys():
       print(
        f'The Distance between {source} and {Destination} is {routes[c]} Rs/km'
         )
      else:
       print(
        f'The Distance between {source} to {Destination} is not available.Please try another route'    
        )
      if no4 == 'Mini':
        value = routes[c]*20
        print('Base Fare is = ₹',value)
        d = value*(9/100)
        value = value+d
        print('Including 9% CGST = ₹',value)
        e = value*(9/100)
        value = value+e
        print('Including 9%SGST = ₹',value)
        print('Your Total Bill including 9% CGST and 9% SGST is =  ₹',value)
        g = value*(20/100)
        value = value - g
        print('Your TOTAL BILL while applying 20% Promocode off becomes =  ₹',value)
        print('Thanks for Booking our Ride.Our Driver will pick you up on time')
        print('***************************************************************')
      elif no4 == 'BIG':
        value = routes[c]*25
        print('Base Fare is = ₹',value)
        d = value*(9/100)
        value = value+d
        print('Including 9% CGST = ₹',value)
        e = value*(9/100)
        value = value+e
        print('Including 9%SGST = ₹',value)
        print('Your Total Bill including 9% CGST and 9% SGST is =  ₹',value)
        g = value*(20/100)
        value = value - g
        print('Your TOTAL BILL while applying 20% Promocode off becomes =  ₹',value)
        print('Thanks for Booking our Ride.Our Driver will pick you up on time')
        print('***************************************************************')
      elif no4 == 'Sedan':
        value = routes[c]*50
        print('Base Fare is = ₹',value)
        d = value*(9/100)
        value = value+d
        print('Including 9% CGST = ₹',value)
        e = value*(9/100)
        value = value+e
        print('Including 9% SGST = ₹',value)
        print('Your Total Bill including 9% CGST and 9% SGST is =  ₹',value)
        g = value*(20/100)
        value = value - g
        print('Your TOTAL BILL while applying 20% Promocode off becomes =  ₹',value)
        print('Thanks for Booking our Ride.Our Driver will pick you up on time')
        print('**************************************************************')
else:
    print('Thanks for Visiting our site')
    print('****************************')
        

     
# create pdf
# send email
# django
# w3school = 
# 1. html tutorial,            
# 2.css tutorials,
# 3.bootstrap 4,
# 4.javascript step by step
