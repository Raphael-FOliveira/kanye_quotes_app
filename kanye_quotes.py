import tkinter as tk
import requests


def get_quote():
    kanye_data = requests.get("https://api.kanye.rest")
    kanye_data.raise_for_status()
    kanye_quote = kanye_data.json()["quote"]
    canvas.itemconfig(quote_space, text=f"Kanye: '{kanye_quote}'")


window = tk.Tk()
window.config(padx=20, pady=20)
window.geometry("800x400")
window.title("Kanye West quote app")

canvas = tk.Canvas(width=800, height=300, bg="white")
quote_space = canvas.create_text(400, 100, text="", width=300, font=("Arial", 15, "italic"))
canvas.pack()

quote_button = tk.Button(text="Get quote", command=get_quote)
quote_button.pack(side="bottom")

window.mainloop()
