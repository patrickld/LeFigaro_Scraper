
import os
from Webscraping import scrapper
import GUI

def user_scrapper(arons_list,pages=100, mode='rent',furniture=False,min_sqm=0,max_p=0):
# function taking as input the variables enter in the GUI and return the filtered dataframe output by the scrapper and the filter function.
# Output is both a csv and a print function of the dataframe.
    df1=scrapper(arons_list,pages, mode)
    df1=filters(df1,furniture,min_sqm,max_p)
    print(df1)

    #generate the csv file
    path = os.path.abspath(os.getcwd())
    path = path + '\data_v2.csv'
    df1.to_csv (path, index = False, header=True, encoding='utf-16')
    print("csv file created")

def user_average(arons_list,pages=100, mode='rent',furniture=False,min_sqm=0,max_p=0):
# Function taking as input the variables enter in the GUI and return the some averages computed on the filtered dataframe.
# Return the expected metrics to the GUI
    df1=scrapper(arons_list,pages, mode)

    # get average values
    df2=filters(df1,furniture,min_sqm,max_p)
    avg_size = round(df2['meters²'].mean(), 2)
    avg_price = round(df2['price in euros'].mean(), 2)
    avg_price_sqm = round((avg_price / avg_size), 2)

    return avg_size, avg_price, avg_price_sqm

def filters(df,furniture,min_sqm,max_p):
#Function taking as input a dataframe and the variables enter in the GUI, returns a filtered dataframe.
    if max_p==0:
        max_p=10000000000
    if furniture:
        df=df[df['furniture']==True]
    df=df[(df['meters²'] >= int(min_sqm)) & (df['price in euros'] <= int(max_p))]

    return df
