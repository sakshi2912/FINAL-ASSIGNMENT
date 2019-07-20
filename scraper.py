#Collab with Triambaka Naresh

from bs4 import BeautifulSoup
import urllib.request
import csv

f=open('Weather.csv','w',newline='')
writer=csv.writer(f)
baseurl='https://karki23.github.io/Weather-Data/'
validpages=['Albury.html','BadgerysCreek.html','Cobar.html','CoffsHarbour.html','Moree.html','Newcastle.html','NorahHead.html','NorfolkIsland.html','Penrith.html','Richmond.html','Sydney.html','SydneyAirport.html','WaggaWagga.html','Williamtown.html','Wollongong.html','Canberra.html','Tuggeranong.html','MountGinini.html','Ballarat.html','Bendigo.html','Sale.html','MelbourneAirport.html','Melbourne.html','Mildura.html','Nhil.html','Portland.html','Watsonia.html','Dartmoor.html','Brisbane.html','Cairns.html','GoldCoast.html','Townsville.html','Adelaide.html','MountGambier.html','Nuriootpa.html','Woomera.html','Albany.html','Witchcliffe.html','PearceRAAF.html','PerthAirport.html','Perth.html','SalmonGums.html','Walpole.html','Hobart.html','Launceston.html','AliceSprings.html','Darwin.html','Katherine.html','Uluru.html']


for text in validpages:
            html =f'{baseurl}{text}'
            
            soup= BeautifulSoup(urllib.request.urlopen(html).read(), 'lxml')

            tbody=soup('table')[0].find_all('tr')
            for row in tbody:
                cols=row.findChildren(recursive=False)
                cols=[ele.text.strip() for ele in cols]
                writer.writerow(cols)
#                print(cols)
from random import shuffle

with open('Weather.csv') as ip:
    lines=ip.readlines()
    header = lines.pop(0)
    shuffle(lines)
    lines.insert(0, header)

with open('shuffled.csv','w') as out:
    out.writelines(lines)

    
from more_itertools import unique_everseen
with open('shuffled.csv','r') as f, open('Weather.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
