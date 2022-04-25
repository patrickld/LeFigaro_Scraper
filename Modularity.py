def get_webpages(sector,pages,mode):
#Create a list of URL according to the inputs of the functions.
#Pages is set to maximal by default, but a user can change it.
    URL_list=[]
    test_sector(sector)
    postcode=get_postcode(sector)
    
    #test if mode is a string to prevent from errors. If it's a string, creates a variable modality with the correct html format.
    if type(mode) is not str: raise ValueError("Mode can either be 'rent' or 'buy', nothing else.")
    modality='location&location=' if mode == "rent" else "vente&location="
   
    #creates a list of URL with the correct arrondissement and incremental number of pages.
    for i in range(1,pages+1):
        URL = 'https://immobilier.lefigaro.fr/annonces/resultat/annonces.html?transaction='+ modality + postcode +'type=appartement&page='+str(i)
        URL_list.append(URL)
    return (URL_list)

def get_postcode(sector):
#Convert the numbers into the postocde of the attondissement
    postcodes=''
    for i in sector:
        stamp='750'
        if int(i)<10:
            stamp='7500'
        #We format the postcode string as expected by the URL, with "," as séparator and "&" at the end.
        postcodes+=stamp+str(i)+','
    return postcodes[:-1]+'&'

def test_sector(sector):
#We test if the sector input by the user is an accepted formather, else we raise an error.
    for i in sector:
            if type(i) is not int: raise ValueError("Arrondissements must be integers")
            elif i>20 or i<1: raise ValueError(i," is an incorrect Arrondissement numbers, Accepted integers from 0 to 20.")
