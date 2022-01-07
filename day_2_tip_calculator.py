print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?\n€")
total_bill = float(total_bill)
total_bill = round(total_bill, 2)

tip_percentage = input("What percentage tip would you like to give?\n%")
tip_percentage = int(tip_percentage)
tip_percentage = (tip_percentage / 100) + 1

num_people = input("How many people are splitting the bill?\n")
num_people = int(num_people)

share = (total_bill / num_people) * tip_percentage
share = round(share, 2)
share = "{:.2f}".format(share)
print(f"Each person should pay: €{share}")
