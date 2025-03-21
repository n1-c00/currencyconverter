import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, root):
        self.conversions = {'USDtoEUR': 0,
                            'USDtoYEN': 1,
                            'USDtoUSD': 2,
                            'EURtoUSD': 5,
                            'EURtoYEN': 7,
                            'EURtoEUR': 1,
                            'YENtoUSD': 11,
                            'YENtoEUR': 13,
                            'YENtoYEN': 1
                            }

        self.Currencies = ["EUR", "USD", "YEN"]

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

