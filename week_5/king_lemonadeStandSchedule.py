"""
Author: Robert King
Date: February 8, 2025
File Name: king_lemonadeStandSchedule
Description:  Prints day of week with assigned daily tasks and main daily task.
"""

# Tasks that need to be accomplished each day
daily_tasks = [
  "Buy sugar",
  "Buy fresh lemons",
  "Stock ice",
  "Make lemonade",
  "Sell lemonade",
  "Clean up and count till"
]
# Main daily task based on week day
day_of_week_task = [
  "Set up stand",
  "Inventory & Restock",
  "Make Bank Deposit",
  "Advertise for Next Week",
  "Break down stand"
]
# Days of the Week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Iterate Through Days of Week and Assign Tasks and Main Daily Task
for i, day in enumerate(days):
  if day in ["Saturday", "Sunday"]:
    print(f"{day}: Today there is no work! Take some time to rest.")
  else:
    print(f"{day}: Here are the tasks for day:")
    for task in daily_tasks:
      print(f" - {task}")
    print(f" - Main Daily Task: {day_of_week_task[i-1]}")