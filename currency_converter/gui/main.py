import requests
import tkinter as tk
from tkinter import ttk

URL = "http://127.0.0.1:5000/convert"
CURRENCIES = ["USD","EUR","GBP","CHF","CAD","RUB","AED","AUD","DKK","SEK",
              "NOK","JPY","KWD","ZAR","BHD","LYD","SAR","IQD","ILS","IRR",
              "INR","MXN","HUF","NZD","BRL","IDR","CZK","PLN","RON","CNY",
              "ARS","ALL","AZN","BAM","CLP","COP","CRC","DZD","EGP","HKD",
              "HRK","ISK","JOD","KRW","KZT","LBP","LKR","MAD","MDL","MKD",
              "MYR","OMR","PEN","PHP","PKR","QAR","RSD","SGD","SYP","THB",
              "TWD","UAH","UYU","GEL","TND","BGN", "TRY"]


def submit_button_click():
    data = {
        "curr_from":combobox1.get(),
        "curr_to":combobox2.get(),
        "amount":text_field.getdouble(text_field.get())
    }
    response = requests.post(URL, json=data)
    responseJ = response.json()
    print("Response Status Code: ", response.status_code)
    print("Response Content: ", response.text)
    label_ca.config(text=responseJ["converted_amount"])
    
    
def validate_numeric_input(P):
    # Check if the input is numeric
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
    
    
# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.resizable(False, False)

# Create labels, comboboxes, text field, and submit button
label1 = tk.Label(root, text="Converted Amount: ")
label2 = tk.Label(root, text="From:\t\t")
label3 = tk.Label(root, text="To:\t\t")
label4 = tk.Label(root, text="Amount:\t\t")
label_ca = tk.Label(root, text="0 ")


combobox1 = ttk.Combobox(root, values=CURRENCIES)
combobox2 = ttk.Combobox(root, values=CURRENCIES)
combobox1.configure(state="readonly")
combobox2.configure(state="readonly")
combobox1.set("USD")
combobox2.set("EUR")


validate_numeric = root.register(validate_numeric_input)
text_field = tk.Entry(root, validate="key", 
                      validatecommand=(validate_numeric, "%P"))

submit_button = tk.Button(root, text="Convert", command=submit_button_click)

# Add padding (margins) between widgets
padx_value = 10
pady_value = 5

label1.grid(row=0, column=0, padx=padx_value, pady=pady_value)
label_ca.grid(row=0, column=1, padx=padx_value, pady=pady_value)
label2.grid(row=1, column=0, padx=padx_value, pady=pady_value)
combobox1.grid(row=1, column=1, padx=padx_value, pady=pady_value)
label3.grid(row=2, column=0, padx=padx_value, pady=pady_value)
combobox2.grid(row=2, column=1, padx=padx_value, pady=pady_value)
label4.grid(row=3, column=0, padx=padx_value, pady=pady_value)
text_field.grid(row=3, column=1, padx=padx_value, pady=pady_value)
submit_button.grid(row=4, column=0, columnspan=2, 
                   padx=padx_value, pady=pady_value)


# Start the Tkinter main loop
root.mainloop()