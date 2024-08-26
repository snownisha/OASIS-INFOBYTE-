def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / height^2."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify BMI into categories based on predefined ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    """Prompt user for weight and height, and validate input."""
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight > 0 and height > 0:
                return weight, height
            else:
                print("Please enter positive numbers for weight and height.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Your BMI is {bmi}, which is considered {category}.")
