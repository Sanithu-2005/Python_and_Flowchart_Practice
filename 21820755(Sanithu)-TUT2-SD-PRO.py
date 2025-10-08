#a)

price1 = float(input('input price one? '))
price2 = float(input('input price two?'))
total_price=price1+price2
print (f"The total price is {total_price}")

#b)

vall=int(27.0)
print("The integer of val1 is ",vall)

#c)

var1=float(2.7)
var2=float(3.3)
the_sum = var1+ var2
print("The_sum is ",the_sum)

#3: Keyboard input

name = input ('Please enter your name: \n')
print ('Hello', name)
age = input ("Please enter your age\n")
print("Your age is",age)
print("test\\test2\\answers.txt")

the_text = input('Enter some text.\n') # get some text!
#print - version 1
print('This is what you entered: ')
print(the_text)
#print – version 2
print('This is what you entered:', the_text)
#print - version 3 - Supress printing of a new line, use end=' '
print('This is what you entered:', end=' ') print(the_text)

#v. Lecture 2 Self-Check Questions (2-4)

num_1 = int(input('Enter number one: '))
num_2 = int(input('Enter number two: '))
total = num_1 + num_2
print(total)

cost = int(input('Enter cost of item: '))
paid = int(input('Enter cash paid: '))
change = paid - cost
print('Change is: ', change)

num_1=float(input("Enter number 1"))
num_2=float(input("Enter number 2"))
num_3=float(input("Enter number 3"))
average=(num_1+num_2+num_3)/3
print(average)

average= round(average,2)
print(average)

#4. Keyboard input continued:

try:
    a=float("Enter a")
    b=float("Enter b")
    c=float("Enter c")
    result= (a+b)*c
    print (f'The result is {result}')
except Exception as ex:
         print("Can't convert the given value to float. Error is:", ex)

#find the average of three numbers
try:
    red=float("Enter value for red")
    green=float("Enter value for green")
    blue=float("Enter value for blue")
    greyscale_average = (red + green + blue) / 3
    print (f'The greyscale value is {greyscale_average}')
except Exception as ex:
    print("Can't convert the given value to float. Error is:", ex)
    
###find the total volume of two cubes
try:
    cube_1_side=float("Enter side of cube 1")
    cube_2_side=float("Enter side of cube 2")
    total_volume=cube_1_side**3+cube_2_side**3
    print (f'The total volume of both cubes is {total_volume}')
except Exception as ex:
    print("Can't convert the given value to float. Error is:", ex)

###find the total area of a trapezoid
try:
    a=float("Enter a")
    b=float("Enter b")
    h=float("Enter h")
    Area=(a+b)*h/2
    print (f'The area of the trapezoid is {Area}
except Exception as ex:
    print("Can't convert the given value to float. Error is:", ex)

#find the total volume of a sphere from the radius
try:
    sphere_radius=float("Enter radius")
    sphere_vol= 4/3 * 3.142*sphere_radius**3
    print (f'The volume of the sphere is {sphere_vol}')
except Exception as ex:
    print("Can't convert the given value to float. Error is:", ex)

a=3
o=0
print("you have:",a,"apples and",o,"oranges")
buy_a=4
buy_o=6
print("you buy:",buy_a,"apples and",buy_o,"oranges")
a=a+buy_a
o=o+buy_o
print("you now have:",a,"apples and",o,"oranges")

#Additional Questions
#1
def q_1(a,b,c):
    try:
        a=float("Enter a")
        b=float("Enter b")
        c=float("Enter c")
        result= (a+b)*c
        print (f'The result is {result}')
    except Exception as ex:
             print("Can't convert the given value to float. Error is:", ex)

#2
def q_2(red,green,blue):
    try:
        red=float("Enter value for red")
        green=float("Enter value for green")
        blue=float("Enter value for blue")
        greyscale_average = (red + green + blue) / 3
        print (f'The greyscale value is {greyscale_average}')
    except Exception as ex:
        print("Can't convert the given value to float. Error is:", ex)

#3
def q_3(cube_1_side,cube_2_side):
    try:
        cube_1_side=float("Enter side of cube 1")
        cube_2_side=float("Enter side of cube 2")
        total_volume=cube_1_side**3+cube_2_side**3
        print (f'The total volume of both cubes is {total_volume}')
    except Exception as ex:
        print("Can't convert the given value to float. Error is:", ex)


#4
def q_4(a,b,h):
    try:
        a=float("Enter a")
        b=float("Enter b")
        h=float("Enter h")
        Area=(a+b)*h/2
        print (f'The area of the trapezoid is {Area}
    except Exception as ex:
        print("Can't convert the given value to float. Error is:", ex)

#5
def q_5(sphere_radius,sphere_vol):
    try:
        sphere_radius=float("Enter radius")
        sphere_vol= 4/3 * 3.142*sphere_radius**3
        print (f'The volume of the sphere is {sphere_vol}')
    except Exception as ex:
        print("Can't convert the given value to float. Error is:", ex)
        
c=float(input("input centi"))
f=(c*1.8) + 32
print(f)

length=float("Enter length")
height=float("Enter height")
width=float("Enter Width")
volume=length*height*width
print(volume)

n = input("Please enter an integer: ")
try:
    n = int(n)
    print(n)
except ValueError:
    print("Requires a valid integer!")

try:
    x = 45 / 0
except ZeroDivisionError:
    print("Cannot divide by zero’")

