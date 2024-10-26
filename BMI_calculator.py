# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main program
def main():
    try:
        # Prompt user for input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {categorize_bmi(bmi)}")
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
