from os import name
import warnings
import requests
import re
from bs4 import BeautifulSoup;
import pandas as pd
##url= 'https://www.dea.gov/fugitives/all?keywords=&page=';

url_primaria ='https://www.dea.gov/fugitives/all?keywords=&page=';
Warningz = [];
Person =[];
Person_names =[];
Person_last_names =[];
Url_details =[];

def pagination_scrap(web,id):
    identificador =0;
    url = web + str(id)
    url_individuals = 'https://www.dea.gov/fugitives/';
    response = requests.get(url);
    soup = BeautifulSoup(response.content,'html.parser');
    div= soup.find_all("div",class_='teaser__body');
    for i in div:
        name = i.find('h3');
        texto = i.find('div',class_='teaser__text');
        id_individual = name.get_text().strip().replace(" ","-");
        url =url_individuals+id_individual;
        Warningz.append(texto.get_text().strip());
        name = name.get_text().strip();
        name =re.sub('-',' ',name);
        Person.append(name);
        Url_details.append(url)
          
for i in range(0,65):
    pagination_scrap(url_primaria,i);

 
dict = {'name': Person,'Warning': Warningz, 'url':Url_details,'List':'(DEA) United States Drug Enforcement Administation Most Wanted Fugitives'} 

data= pd.DataFrame(dict)

csv = data.to_csv('file.csv',index=False,sep=',');

print('creado...');
