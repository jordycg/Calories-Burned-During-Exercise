# This is a simple program that inputs age, weight, heart rate, and calories burned during exercise

# Ask the user to choose between imperial or metric
print("Imperial = lbs")
print("Metric = kg")
# Making sure to remove case sensitivity and to remove any extra spaces and
unit_system = input("Choose your unit system (imperial or metric): ").strip().lower()

# User Inputs Age
age = int(input("Enter your age: "))

# User Inputs Heart Rate
heartRate = int(input("Enter your heart rate (bpm): "))

# User Inputs Time Active
mins = int(input("Enter the elapsed time of exercise (mins): "))

# If the user chooses imperial
if unit_system == "imperial":
    # User Inputs Weight
    weight = float(input("Enter your weight (pounds): "))
    # Calculation to get the calories burned during exercise
    avgCals_burned = ((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * mins / 8.368
# If the user chooses metric
elif unit_system == "metric":
    # User Inputs Weight
    weight = float(input("Enter your weight (kilograms): "))
    # Converting the weight in lbs to kg
    weight_in_pounds = weight * 2.20462
    avgCals_burned = ((age * 0.2757) + (weight_in_pounds * 0.03295) + (heartRate * 1.0781) - 75.4991) * mins / 8.368
# If the user does not enter imperial or metric, the program lets them know
else:
    print("Invalid unit system entered. Please try again")
    # Exiting program because user entered invalid unit
    exit()


# Program successfully runs
print(f'Calories: {avgCals_burned:.2f} calories')

