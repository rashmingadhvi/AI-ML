import csv
import random


def generate_data(num_row):
    csv_data = []
    for _ in range(num_row):
        height = random.randint(140, 200)
        weight = random.randint(40, 150)
        bmi = weight / ((height / 100) ** 2)
        gender = random.choice(['M', 'F'])
        csv_data.append((height, weight, bmi, gender))
    return csv_data


data = generate_data(500)

# Save the data to a CSV file
with open('my_data.csv', 'w', newline='\r\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Height (cm)', 'Weight (kg)', 'BMI', 'Gender'])  # Header row
    writer.writerows(data)
