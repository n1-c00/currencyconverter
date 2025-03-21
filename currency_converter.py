import tkinter as tk
from tkinter import ttk
import requests

url = "https://api.exchangerate-api.com/v4/latest/"


class CurrencyConverter:
    def __init__(self, root):
        self.conversions = {}
        
        self.Currencies = ["EUR", "USD", "JPY"]

        # Initialize conversion rates dictionary using the API
        for base_currency in self.Currencies:
            response = requests.get(url + base_currency)
            data = response.json()
            rates = data.get('rates', {})
            print(rates)


        #init for TKinter
        self.root = root
        self.root.title("Währungsrechner")
        self.root.geometry("900x300")

        self.Out = tk.StringVar()
        self.Out.set("n.A.")
        self.my_label = tk.Label(root, textvariable=self.Out, font=("Arial", 20))
        self.my_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Input", 20))
        self.entry.pack(pady=5)

        self.choosenIn = tk.StringVar()
        self.choosenIn.set(self.Currencies[0])
        self.CurrencyIn = tk.OptionMenu(root, self.choosenIn, *self.Currencies)
        self.CurrencyIn.pack(pady=5)

        self.choosenOut = tk.StringVar()
        self.choosenOut.set(self.Currencies[0])
        self.CurrencyOut = tk.OptionMenu(root, self.choosenOut, *self.Currencies)
        self.CurrencyOut.pack(pady=5)
        

        self.button = tk.Button(root, text="Start", command=self.excange)
        self.button.pack(pady=10)

    def excange(self):
        input=int(self.entry.get())
        search = f"{self.choosenIn.get()}to{self.choosenOut.get()}"

        self.Out.set(str(input * self.conversions[search]))
        




if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

