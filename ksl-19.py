#Name: Egor Kislykh
#Email: egor.kislykh24@myhunter.cuny.edu
#Date: Mar 7, 2023
#This is program number 19

print("a: G -> L")
print("b: L -> G")

if (m := input("Choose: ")) == 'a':
    print(round(float(input("How many gallons: ")) * 3.79, 2))
elif m == 'b':
    print(round(float(input("How many liters: ")) * .26, 2))
else:
    print("Wrong input")