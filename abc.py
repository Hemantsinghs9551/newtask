pi = 3.14
R = float(input("Enter the radius of circle: "))
area_of_circle = pi * R * R
print("Area of a circle = %.2f" % area_of_circle)


fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
