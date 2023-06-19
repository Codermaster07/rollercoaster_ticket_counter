print("wellcome to the rollercoaster!")
height = int(input("what is your height in cm ?"))
bill = 0
if height >= 120:
  print("you can ride the rollercoaster")
else:
  print("you should grow taller to ride it. ")
age = int(input("what is your age?"))
if age < 12:
  print("child ticket price is $5. ")
  bill = 5
elif age <= 18:
  print("youth ticket price is $7.")
  bill = 7
else:
  print("adult ticket price is $12.")
  bill = 12

wants_photos = input("do you want a photo taken ? y or n .")
if wants_photos == "y":
  bill += 3

print(f"your final bill is {bill}")

































