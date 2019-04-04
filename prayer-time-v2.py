#/bin/python3/
#Fetch the prayer time from the offcial website of Hubous(Maroc)
#Require BeautifulSoup 4

import urllib.request
from bs4 import BeautifulSoup
import datetime

URL = 'http://www.habous.gov.ma/horaire%20de%20priere/horaire-fm6oafr.php?ville=32'

def Converttime(timestring):
    timelist = timestring.split(":")
    return int(timelist[0])*60 + int(timelist[1])


try:
    RequestPage = urllib.request.urlopen(URL)
    ParsedPage = BeautifulSoup(RequestPage,'html.parser')
    table = ParsedPage.findAll("table",{"class":"horaire"})
    CurrentTime = datetime.datetime.now()
    Convcurrentime=(CurrentTime.hour)*60 + CurrentTime.minute

    td = table[0].find_all("td")
    if (len(td) != 12 ):
        prin("Error in parsing")
    Fajr = Converttime(td[1].get_text())   
    Duhr =Converttime(td[5].get_text())
    Asr =Converttime(td[7].get_text())
    Maghreb=Converttime(td[9].get_text())
    Isha =Converttime(td[11].get_text())

    if ( Fajr < Convcurrentime and  Convcurrentime <= Duhr):
        CurrentPrayer = "DUHR: "+ ' '.join(td[5].get_text().split()) 
    elif ( Duhr < Convcurrentime and Convcurrentime <= Asr):
        CurrentPrayer = "ASR: "+' '.join(td[7].get_text().split()) 
    elif ( Asr < Convcurrentime and Convcurrentime <= Maghreb):
        CurrentPrayer = "MAGH: "+' '.join(td[9].get_text().split()) 
    elif ( Maghreb < Convcurrentime and Convcurrentime <= Isha):
        CurrentPrayer = "ISHA: "+' '.join(td[11].get_text().split()) 
    elif ( Fajr > Convcurrentime or Convcurrentime > Isha):
        CurrentPrayer = "FAJR: "+' '.join(td[1].get_text().split()) 

    print('<span background="#53009D"> ',CurrentPrayer,' </span>')

except:
    print('<span background="#53009D"> ',"Error ocured",' </span>')
