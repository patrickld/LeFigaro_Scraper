import requests
from bs4 import BeautifulSoup
import pandas as pd
import Modularity
from Data_Exploitation import cleaner, price_cleaner,sq_clean,is_it_furniture, how_many_room, location

def scrapper(sector,pages=100,mode='rent'):
#Webscrapping function, takes many arrondissement as input, the number of pages you want to analyse with pages=your_int.
#Scrapper can also take the argument mode to switch from rent to buy: accepted 'buy' or 'rent'.
#Return a dataframe with clean data.
    URL_list=Modularity.get_webpages(sector,pages,mode)
    #Call the function in modularity to get the list of URLs
    df = pd.DataFrame()
    #Creates an empty panda dataframe that is going to be filled later on.
    for URL in URL_list:
    #Iterates through every URL to find specific html tags.
        soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
        results = soup.find(id='js-container-classified-items')
        results.prettify()
        if results.find_all('div',class_='searchWarning'):
                break
        #We stop the iteration if we detect searchWarning, which indicates that we exceed the maximum pages
        apt_elems = results.find_all('div', class_='item-main-infos')
        #From each url we create a dataframe.
        df1=get_dataframe(apt_elems)
        #Concatenate all pages dataframes.
        df = pd.concat([df,df1], ignore_index=True)

    return df

def get_dataframe(apt_elems):
    #Takes a beautifyl soup object as input, analyse all the html tag to extract the information we want.
    #Returns information in a dataframe.
    title = []
    price = []
    description = []
    i = 0

    for apt_elem in apt_elems:
    # We create new BeautifulSoup objects for tiltle,price and description include in specific tags.
        title_elem = apt_elem.find('a', class_='js-link-ei')
        price_elem = apt_elem.find('span', class_='price-label')
        description_elem = apt_elem.find('p', class_='item-description')
        #In some specific case the correct information can be in another HTML tag 'js-link-plf'
        if(title_elem == None):
            title_elem = apt_elem.find('a', class_='js-link-plf')
        if(title_elem != None and price_elem != None and description_elem != None):
            title.append(title_elem)
            price.append(price_elem)
            description.append(description_elem)

        i += 1

    #Creates columns of the dataframe and append data previously extrated from html tags and clean using the Data_Exploitation functions.
    df = pd.DataFrame()
    df['title'] = cleaner(title)
    df['arrondissement'] = location(title)
    df['price in euros'] = price_cleaner(cleaner(price))
    df['meters²'] = sq_clean(cleaner(title))
    df['price/sq² in euros']=round(df['price in euros']/df['meters²'],2)
    df['room number']=how_many_room(title)
    df['furniture'] = is_it_furniture(title)
    df['description'] = cleaner(description)

    return df
