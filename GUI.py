import tkinter as tk
import re
from functools import partial
from main import user_scrapper, user_average

def search():
# Function called when the input press the 'Search'
# Takes the input from the GUI and pass it to user_scrapper.
    arons_list=list_of_arrons()
    mode,furn, min_sqm, max_p = options()

    user_scrapper(arons_list,mode=mode,pages=100,furniture=furn,min_sqm=min_sqm,max_p=max_p)

def quick_s():
# Function called when the input press the 'Quick Search'
# Takes the input from the GUI and pass it to user_scrapper, with the page number fixed to 1.
    arons_list=list_of_arrons()
    mode,furn, min_sqm, max_p = options()

    user_scrapper(arons_list,mode=mode,pages=1,furniture=furn,min_sqm=min_sqm,max_p=max_p)

def average():
# Function called when the input press the 'Average'
# Takes the input from the GUI and pass it to user_average and display the result in a new window.
    new_window = tk.Toplevel(window)
    arons_list=list_of_arrons()
    mode,furn, min_sqm, max_p = options()

    avg_size, avg_price, avg_price_sqm =user_average(arons_list,mode=mode,pages=100,furniture=furn,min_sqm=min_sqm,max_p=max_p)

    #create labels for all the averages to display
    tk.Label(new_window,
                text="Average square meters").grid(row=1)
    tk.Label(new_window,
                text=avg_size).grid(row=1, column=1)
    tk.Label(new_window,
                text="Average price").grid(row=2)
    tk.Label(new_window,
                text=avg_price).grid(row=2, column=1)
    tk.Label(new_window,
                text='Average price per sqm').grid(row=3)
    tk.Label(new_window,
                text=avg_price_sqm).grid(row=3, column=1)

def list_of_arrons():
    #create a list of arrondissements from input
    arons_list = list(map(int, re.findall(r'\d+', arrond_entry.get())))
    arons_list = [x for x in arons_list if x <= 20]

    return arons_list

def options():
#takes input the values in the GUI and transform them in handy variable.
    if(buy_check.get() == 1):
        mode='buy'
    else:
        mode='rent'
    if (furn_check.get() == 1):
        furn=True
    else:
        furn=False
    if sqm_entry.get() != '':
        min_sqm = sqm_entry.get()
    else:
        min_sqm = 0
    if price_entry.get() != '':
        max_p = price_entry.get()
    else:
        max_p = 0
    return mode, furn, min_sqm, max_p

#create a GUI window
window = tk.Tk()

#create labels to display
window.title("Appartment Hunting")
tk.Label(window,
         text="Arrondissements").grid(row=0)
tk.Label(window,
         text="Minimum Square Meters").grid(row=1)
tk.Label(window,
         text="Max Price").grid(row=2)
tk.Label(window,
         text="Furnished").grid(row=3)
tk.Label(window,
         text="Buying ").grid(row=4)

#create entries for its respective labels
arrond_entry = tk.Entry(window)
sqm_entry = tk.Entry(window)
price_entry = tk.Entry(window)

arrond_entry.grid(row=0, column = 1)
sqm_entry.grid(row=1, column = 1)
price_entry.grid(row=2, column = 1)

#create checkboxes for buying and furniture options
furn_check = tk.IntVar()
tk.Checkbutton(window, variable=furn_check).grid(row=3, column=1, sticky=tk.W)
buy_check = tk.IntVar()
tk.Checkbutton(window, variable=buy_check).grid(row=4, column=1, sticky=tk.W)

#button to exit the UI
tk.Button(window,
          text='Quit',
          command=window.quit).grid(row=6,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

#button to execute the scraping
tk.Button(window,
          text='Search', command=search).grid(row=4,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)
#button to get the average values
tk.Button(window,
          text='Average',
          command=average).grid(row=6,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
 #button to do a quick search. Scrap through only 1 page
tk.Button(window,
          text='Quick Search',
          command=quick_s).grid(row=6,
                                    column=2,
                                    sticky=tk.W,
                                    pady=4)
tk.mainloop()
