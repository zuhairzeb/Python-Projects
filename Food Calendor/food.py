import random
from datetime import datetime

# Define the months and meal times
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

meal_times = ["Breakfast", "Mid-Morning Snack", "Lunch", "Afternoon Snack", "Dinner", "Evening Snack"]

# Generate random meals for each day
def generate_daily_meals():
    foods = {
        "Breakfast": ["Apple", "Oatmeal", "Smoothie", "Pancakes", "Yogurt"],
        "Mid-Morning Snack": ["Nuts", "Fruit", "Granola Bar", "Cheese", "Crackers"],
        "Lunch": ["Chicken Salad", "Vegetable Soup", "Turkey Sandwich", "Quinoa Bowl", "Sushi"],
        "Afternoon Snack": ["Carrot Sticks", "Hummus", "Apple Slices", "Trail Mix", "Greek Yogurt"],
        "Dinner": ["Grilled Fish", "Stir-Fry", "Pasta", "Chicken Curry", "Vegetable Stir-Fry"],
        "Evening Snack": ["Almonds", "Dark Chocolate", "Fruit Salad", "Popcorn", "Cottage Cheese"]
    }
    return {meal_time: random.choice(foods[meal_time]) for meal_time in meal_times}

# Create the yearly calendar with different meals each day
yearly_calendar = {}
for month in months:
    yearly_calendar[month] = {}
    for day in range(1, 32):  # Adjust for different month lengths as needed
        yearly_calendar[month][f"Day {day}"] = generate_daily_meals()

# Function to view the calendar for a specific date and time
def view_food_plan(month, day, meal_time=None):
    month = month.capitalize()
    meal_time = meal_time.capitalize() if meal_time else None

    if month in yearly_calendar and f"Day {day}" in yearly_calendar[month]:
        if meal_time:
            food = yearly_calendar[month][f"Day {day}"].get(meal_time)
            if food:
                print(f"\nFor {meal_time} on {month} {day}, you will eat: {food}")
            else:
                print(f"\nNo food planned for {meal_time} on {month} {day}.")
        else:
            print(f"\nFood plan for {month} {day}:")
            for time, food in yearly_calendar[month][f"Day {day}"].items():
                print(f"  {time}: {food}")
    else:
        print(f"Invalid date or month: {month} {day}")

# Interactive function
def interactive_food_calendar():
    while True:
        month = input("Enter your month (e.g., 'June'): ").strip()
        day = int(input("Enter your date (e.g., '2'): ").strip())
        meal_time = input("Enter the meal time (e.g., 'Lunch') or leave blank for full day: ").strip()

        if input("Do you want to check today's calendar? (yes/no): ").strip().lower() == 'yes':
            today = datetime.now()
            today_month = months[today.month - 1]  # Get current month name
            today_day = today.day  # Get current day
            print(f"\nToday's Calendar ({today_month} {today_day}):")
            view_food_plan(today_month, today_day)  # Show full day's food plan for today's date
        else:
            view_food_plan(month, day, meal_time)  # Show specific meal time or full day’s plan

        # Option to exit or continue
        if input("Do you want to check another day? (yes/no): ").strip().lower() != 'yes':
            break

# Run the interactive function
interactive_food_calendar()
