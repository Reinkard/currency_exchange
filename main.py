from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
data = response.json()
eur_ccy = data[0]['ccy']
eur_buy = data[0]['buy']
eur_sale = data[0]['sale']
eur_uah = data[0]['base_ccy']
usd_ccy = data[1]['ccy']
usd_buy = data[1]['buy']
usd_sale = data[1]['sale']
usd_uah = data[1]['base_ccy']
window = Tk()
window.configure(padx=40, pady=40, width=400, height=400)
window.resizable(width=False, height=False)
window.title(f'Курс валют')

today_data = datetime.today()
label = Label(text=f'Сьогодні {today_data.strftime("%d %B %Y року")}', padx=30, pady=30, font=('Arial', 20, 'bold'))
label.grid(row=0, column=0, columnspan=2)

label = Label(text=f'Курс {usd_ccy}:')
label.grid(row=2, column=0)
label = Label(text=f'Покупка: {usd_buy} {usd_uah}')
label.grid(row=3, column=0)
label = Label(text=f'Продажа: {usd_sale} {usd_uah}')
label.grid(row=4, column=0)

label = Label(text=f'Курс {eur_ccy}:')
label.grid(row=2, column=1)
label = Label(text=f'Покупка: {eur_buy} {eur_uah}')
label.grid(row=3, column=1)
label = Label(text=f'Продажа: {eur_sale} {eur_uah}')
label.grid(row=4, column=1)

window.mainloop()