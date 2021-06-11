import requests
from tkinter import *
from datetime import datetime

# GUI CONFIGURATIONS
root=Tk()
root.geometry("400x500")
root.title("BITCOIN TRACKER")

# API
def trackBitcoin():
    # url ="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response= requests.get(url).json()
    price= response["USD"]
    time= datetime.now().strftime("%H:%M:%S")

    LabelPrice.config(text=str(price)+ "$")
    LabelTime.config(text="UPDATED AT: "+str(time)+ " IST")

    root.after(500,trackBitcoin)


# Fonts
f1=("poppins", 24, "bold")
f2=("poppins", 22, "bold")
f3=("poppins", 12, "normal")

# Labels
LabelBitcoin = Label(root, text="BITCOIN PRICE:",font=f1)
LabelBitcoin.pack(pady=20)

LabelPrice= Label(root, font=f2)
LabelPrice.pack(pady=20)

LabelTime= Label(root, font=f3)
LabelTime.pack(pady=20)

trackBitcoin()

root.mainloop()