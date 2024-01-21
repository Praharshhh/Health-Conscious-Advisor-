def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
        else:
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")
            
            category = interpret_bmi(bmi)
            print(f"You are categorized as: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")


import csv

def recommend_food(file_path="C:\\Users\\Raj Sharma\\OneDrive\\Desktop\\Health advisor\\dataoffood.csv"):
    # Assuming the CSV file has columns: FoodName, Calories, Carbohydrate, Protein, Fat, Cholesterol
    
    # Open the CSV file and read data
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header if there is one
        next(csv_reader, None)
        
        food_data = []

        # Process each row in the CSV filea
        for row in csv_reader:
            FoodName, Calories, Carbohydrate, Protein, Fat, Cholesterol = row
            
            # Convert string values to appropriate data types
            foodname= (FoodName)
            calories = float(Calories)
            carbohydrate = float(Carbohydrate)
            protein = float(Protein)
            fat = float(Fat)
            cholesterol = float(Cholesterol)

            # Save food data for recommendations
            food_data.append({
                'FoodName': foodname,
                'Calories': calories,
                'Carbohydrate': carbohydrate,
                'Protein': protein,
                'Fats': fat,
                'Cholestrol': cholesterol,
            })
    
    main()
    Lifestyle_input = input("Enter your role (athlete, bodybuilder,healthly lifestyle,): ").lower()
    if Lifestyle_input == "athlete":
        print("Great!!! You selected Athlete.")
        threshold_protein= 15
        threshold_calories= 550
    elif Lifestyle_input == "bodybuilder":
        print("Great!!! You selected Bodybuilder.")
        threshold_calories= 550
        threshold_protein= 20
    elif Lifestyle_input == "healthly lifestyle":
        print("Great!!! You selected Healthly lifestyle.")
        
    else:
        print("Invalid input. Please enter a valid role.")
    

    threshold_protein= 15
    threshold_calories= 150
    high_protein_foods = [food['FoodName'] for food in food_data if food['Protein'] >=threshold_protein or food['Calories']>=threshold_calories and food['Cholestrol']<=0.75]
    if high_protein_foods:
        print(f"Foods are comtable to your lifestyle: {', '.join(high_protein_foods)}")

    else:
        print("The protein content in another foods are low on the bases of your lifestyle.")

recommend_food()
