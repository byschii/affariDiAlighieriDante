import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re 
from time import sleep

import sys
import codecs
import locale
#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)



#https://it.wikiversity.org/wiki/Divina_Commedia_-_Inferno_-_II_Canto_(superiori)

#https://divinacommedia.weebly.com/inferno-canto-i.html
dominio = "https://divinacommedia.weebly.com"
end_point = "/{libro}-canto-{canto}.html"
libri = ("Inferno", "Purgatorio", "Paradiso")
canti = {
	"1":"i", "2":"ii", "3":"iii", "4":"iv",
	"5":"v", "6":"vi", "7":"vii", "8":"viii", 
	"9":"ix", "10":"x", "11":"xi", "12":"xii",
	"13":"xiii", "14":"xiv", "15":"xv", "16":"xvi",
	"17":"xvii", "18":"xviii", "19":"ixx", "20":"xx",
	"21":"xxi", "22":"xxii", "23":"xxiii", "24":"xxiv",
	"25":"xxv", "26":"xxvi", "27":"xxvii", "28":"xxviii",
	"29":"xxix", "30":"xxx", "31":"xxxi", "32":"xxxii",
	"33":"xxxiii"
	}

def cleanTesto(tag):
	testone = unidecode(tag.text.replace("\n","  ")).split()[1:]
	filtro =  lambda x: re.sub("\d", "", x)
	return " ".join(map(filtro,testone))


for libro in libri:
	for num,rom in canti.items():
		url = (dominio+end_point).format(libro=libro, canto=rom)
		response = requests.get( url )
		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			testo = soup.findAll("td", {"class":"wsite-multicol-col"})[2:]

			#creazione file volgare
			volgare = cleanTesto(testo[0])
			nome_file_v = "volgare" + "-" + libro.lower() + "-" + num + ".txt"

			#creazione file italiano
			parafrasi = cleanTesto(testo[1])
			nome_file_p = "parafrasi" + "-" + libro.lower() + "-" + num + ".txt"


			print(testo)

			print("############")
			break

			
