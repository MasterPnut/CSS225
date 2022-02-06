#Ryne Bigueras
#2/5/22

#Problem 1
print("Hello World")

#Problem 2
name = input("Your Name? ")
print( "Hello", name)

#Problem 3
name = input("Your Name? ")
if name == ("Zoe") or name == ("Ryne"):
    print('Hello Special User', name)
elif name:
    print()

#Problem 4
pi = 3.14
r = float(input("Give me a radius: "))
a = pi*r*r
print("That's a big circle:", a,"area of a circle")

#Problem 5
m = float(input("Miles driven: "))
g = float(input("Gallons used: "))
mpg = m/g
print("Nice fuel efficient car:", mpg, "/MPG")

#Problem 6
f = float(input("Whats the temprature in Fahrenheit: "))
c = (f-32)*5.0%9.0
print("How does this feel to you:", c,"Celsius")

#Problem 7
day = float(input("Starting Day 0(sunday)-(Saturday)6:"))
stay = float(input("Length of Stay:"))
print ("Return Day",((day + stay)% 7))


