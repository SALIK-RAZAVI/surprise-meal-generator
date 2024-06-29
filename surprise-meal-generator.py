import tkinter as tk
from tkinter import messagebox
import random

mystery_meals = [
    "Pizza", "Sushi", "Burger", "Tacos", "Pasta", "biryani", "barbique"
    "Salad", "Fried Chicken", "Ramen", "Steak", "Fish and Chips",
    "Curry", "Burrito", "Soup", "Sandwich", "Dumplings"
]

def deliver_mystery_meal():
    if random.random() < 0.5:
        messagebox.showinfo("Surprise Mystery Meal", f"Enjoy your surprise mystery meal: {random.choice(mystery_meals)}!")
    else:
        messagebox.showwarning("Oops!", "Sorry, no mystery meal available this time. Try again later!")

root = tk.Tk()
root.title("Random Food Delivery App with Surprise Mystery Meals")

tk.Label(root, text="Click below to order a surprise mystery meal:").pack(pady=10)
order_button = tk.Button(root, text="Order Mystery Meal", command=deliver_mystery_meal)
order_button.pack(pady=20)

root.mainloop()