import requests
from bs4 import BeautifulSoup
import whois
import datetime
import time
import re

# Importiere das Colorama-Modul
from colorama import init, Fore, Back, Style

# Initialisiere das Colorama-Modul
init()


top_level_domains = [
    ".ac",  # Ascension Island
    ".ad",  # Andorra
    ".ae",  # Vereinigte Arabische Emirate
    ".af",  # Afghanistan
    ".ag",  # Antigua und Barbuda
    ".ai",  # Anguilla
    ".al",  # Albanien
    ".am",  # Armenien
    ".an",  # Niederländische Antillen (veraltet)
    ".ao",  # Angola
    ".aq",  # Antarktis
    ".ar",  # Argentinien
    ".as",  # Amerikanisch-Samoa
    ".at",  # Österreich
    ".au",  # Australien
    ".aw",  # Aruba
    ".ax",  # Åland
    ".az",  # Aserbaidschan
    ".ba",  # Bosnien und Herzegowina
    ".bb",  # Barbados
    ".bd",  # Bangladesch
    ".be",  # Belgien
    ".bf",  # Burkina Faso
    ".bg",  # Bulgarien
    ".bh",  # Bahrain
    ".bi",  # Burundi
    ".bj",  # Benin
    ".bm",  # Bermuda
    ".bn",  # Brunei Darussalam
    ".bo",  # Bolivien
    ".br",  # Brasilien
    ".bs",  # Bahamas
    ".bt",  # Bhutan
    ".bv",  # Bouvetinsel
    ".bw",  # Botsuana
    ".by",  # Belarus (Weißrussland)
    ".bz",  # Belize
    ".ca",  # Kanada
    ".cc",  # Kokosinseln (Keelinginseln)
    ".cd",  # Demokratische Republik Kongo
    ".cf",  # Zentralafrikanische Republik
    ".cg",  # Republik Kongo
    ".ch",  # Schweiz
    ".ci",  # Elfenbeinküste
    ".ck",  # Cookinseln
    ".cl",  # Chile
    ".cm",  # Kamerun
    ".cn",  # China
    ".co",  # Kolumbien
    ".cr",  # Costa Rica
    ".cu",  # Kuba
    ".cv",  # Kap Verde
    ".cw",  # Curaçao
    ".cx",  # Weihnachtsinsel
    ".cy",  # Zypern
    ".cz",  # Tschechien
    ".de",  # Deutschland
    ".dj",  # Dschibuti
    ".dk",  # Dänemark
    ".dm",  # Dominica
    ".do",  # Dominikanische Republik
    ".dz",  # Algerien
    ".ec",  # Ecuador
    ".ee",  # Estland
    ".eg",  # Ägypten
    ".er",  # Eritrea
    ".es",  # Spanien
    ".et",  # Äthiopien
    ".eu",  # Europäische Union
    ".fi", 
    ".fj",  # Fidschi
    ".fk",  # Falklandinseln
    ".fm",  # Mikronesien
    ".fo",  # Färöer
    ".fr",  # Frankreich
    ".ga",  # Gabun
    ".gb",  # Vereinigtes Königreich
    ".gd",  # Grenada
    ".ge",  # Georgien
    ".gf",  # Französisch-Guayana
    ".gg",  # Guernsey
    ".gh",  # Ghana
    ".gi",  # Gibraltar
    ".gl",  # Grönland
    ".gm",  # Gambia
    ".gn",  # Guinea
    ".gp",  # Guadeloupe
    ".gq",  # Äquatorialguinea
    ".gr",  # Griechenland
    ".gs",  # Südgeorgien und die Südlichen Sandwichinseln
    ".gt",  # Guatemala
    ".gu",  # Guam
    ".gw",  # Guinea-Bissau
    ".gy",  # Guyana
    ".hk",  # Hongkong
    ".hm",  # Heard- und McDonald-Inseln
    ".hn",  # Honduras
    ".hr",  # Kroatien
    ".ht",  # Haiti
    ".hu",  # Ungarn
    ".id",  # Indonesien
    ".ie",  # Irland
    ".il",  # Israel
    ".im",  # Isle of Man
    ".in",  # Indien
    ".io",  # Britisches Territorium im Indischen Ozean
    ".iq",  # Irak
    ".ir",  # Iran
    ".is",  # Island
    ".it",  # Italien
    ".je",  # Jersey
    ".jm",  # Jamaika
    ".jo",  # Jordanien
    ".jp",  # Japan
    ".ke",  # Kenia
    ".kg",  # Kirgisistan
    ".kh",  # Kambodscha
    ".ki",  # Kiribati
    ".km",  # Komoren
    ".kn",  # St. Kitts und Nevis
    ".kp",  # Demokratische Volksrepublik Korea (Nordkorea)
    ".kr",  # Republik Korea (Südkorea)
    ".kw",  # Kuwait
    ".ky",  # Kaimaninseln
    ".kz",  # Kasachstan
    ".la",  # Laos
    ".lb",  # Libanon
    ".lc",  # St. Lucia
    ".li",  # Liechtenstein
    ".lk",  # Sri Lanka
    ".lr",  # Liberia
    ".ls",  # Lesotho
    ".lt",  # Litauen
    ".lu",  # Luxemburg
    ".lv",  # Lettland
    ".ly",  # Libyen
    ".ma",  # Marokko
    ".mc",  # Monaco
    ".md",  # Moldawien
    ".me",  # Montenegro
    ".mg",  # Madagaskar
    ".mh",  # Marshallinseln
    ".mk",  # Nordmazedonien
    ".ml",  # Mali
    ".mm",  # Myanmar (Burma)
    ".mn",
    ".mo",  # Macau
    ".mp",  # Nördliche Marianen
    ".mq",  # Martinique
    ".mr",  # Mauretanien
    ".ms",  # Montserrat
    ".mt",  # Malta
    ".mu",  # Mauritius
    ".mv",  # Malediven
    ".mw",  # Malawi
    ".mx",  # Mexiko
    ".my",  # Malaysia
    ".mz",  # Mosambik
    ".na",  # Namibia
    ".nc",  # Neukaledonien
    ".ne",  # Niger
    ".nf",  # Norfolkinsel
    ".ng",  # Nigeria
    ".ni",  # Nicaragua
    ".nl",  # Niederlande
    ".no",  # Norwegen
    ".np",  # Nepal
    ".nr",  # Nauru
    ".nu",  # Niue
    ".nz",  # Neuseeland
    ".om",  # Oman
    ".pa",  # Panama
    ".pe",  # Peru
    ".pf",  # Französisch-Polynesien
    ".pg",  # Papua-Neuguinea
    ".ph",  # Philippinen
    ".pk",  # Pakistan
    ".pl",  # Polen
    ".pm",  # St. Pierre und Miquelon
    ".pn",  # Pitcairninseln
    ".pr",  # Puerto Rico
    ".ps",  # Palästinensische Autonomiegebiete
    ".pt",  # Portugal
    ".pw",  # Palau
    ".py",  # Paraguay
    ".qa",  # Katar
    ".re",  # Réunion
    ".ro",  # Rumänien
    ".rs",  # Serbien
    ".ru",  # Russland
    ".rw",  # Ruanda
    ".sa",  # Saudi-Arabien
    ".sb",  # Salomonen
    ".sc",  # Seychellen
    ".sd",  # Sudan
    ".se",  # Schweden
    ".sg",  # Singapur
    ".sh",  # St. Helena
    ".si",  # Slowenien
    ".sk",  # Slowakei
    ".sl",  # Sierra Leone
    ".sm",  # San Marino
    ".sn",  # Senegal
    ".so",  # Somalia
    ".sr",  # Suriname
    ".ss",  # Südsudan
    ".st",  # São Tomé und Príncipe
    ".sv",  # El Salvador
    ".sx",  # Sint Maarten
    ".sy",  # Syrien
    ".sz",  # Eswatini
    ".tc",  # Turks- und Caicosinseln
    ".td",  # Tschad
    ".tf",  # Französische Süd- und Antarktisgebiete
    ".tg",  # Togo
    ".th",  # Thailand
    ".tj",  # Tadschikistan
    ".tk",  # Tokelau
    ".tl",  # Timor-Leste
    ".tm",  # Turkmenistan
    ".tn",  # Tunesien
    ".to",  # Tonga
    ".tr",  #
    ".tt", # Trinidad und Tobago
    ".tv", # Tuvalu
    ".tw", # Taiwan
    ".tz", # Tansania
    ".ua", # Ukraine
    ".ug", # Uganda
    ".uk", # Vereinigtes Königreich
    ".us", # Vereinigte Staaten
    ".uy", # Uruguay
    ".uz", # Usbekistan
    ".va", # Vatikanstadt
    ".vc", # St. Vincent und die Grenadinen
    ".ve", # Venezuela
    ".vg", # Britische Jungferninseln
    ".vi", # Amerikanische Jungferninseln
    ".vn", # Vietnam
    ".vu", # Vanuatu
    ".wf", # Wallis und Futuna
    ".ws", # Samoa
    ".ye", # Jemen
    ".yt", # Mayotte
    ".za", # Südafrika
    ".zm", # Sambia
    ".zw", # Simbabwe
]


def extract_hostnames_from_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #print(response.content)
    
    #table = soup.find('table', class_='iana-table')
    hostnames = []

    table_rows = soup.find_all('tr')
    for row in table_rows:
        cells = row.find_all('td')
        for cell in cells:
            hostname = cell.get_text()
            if is_valid_hostname(hostname):
                hostnames.append(hostname)
    return hostnames

def is_valid_hostname(hostname):
    pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
    return re.match(pattern, hostname) is not None


def get_ns(tld):
    #https://www.iana.org/domains/root/db/co.html

    
    url = "https://www.iana.org/domains/root/db/" +tld+ ".html"
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    ns = []

    #print(response.content)
    
    table = soup.find('table', class_='iana-table')

    #print(table)
    '''

    ns = extract_hostnames_from_table(url)

    return ns



def get_tlds():
    url = "https://www.iana.org/domains/root/db"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tlds = []

    #print(response.content)
    
    table = soup.find('table', class_='iana-table')
    #print(table)

    if table is not None:
        rows = table.find_all("tr")
        #print(rows)
        for row in rows:
            tld_cell = row.find('span', class_='domain tld')
            #print(tld_cell)
            if tld_cell is not None:
                tld = tld_cell.text.strip()
                
                if tld.startswith("."):
                    tld = tld[1:]
                    #print(tld)
                tlds.append(tld)
    
    return tlds

def check_domain_expiry(domain):

    try:
        w = whois.whois(domain)
        #print(w)
        if isinstance(w.expiration_date, list):
            expiry_date = w.expiration_date[0]
        else:
            expiry_date = w.expiration_date

        if isinstance(expiry_date, datetime.datetime):
            current_date = datetime.datetime.now()
            days_remaining = (expiry_date - current_date).days

            if days_remaining < 0:
                #print(f"{domain} ist abgelaufen!")
                print(Fore.RED + f"{domain} ist abgelaufen!")
            else:
                #print(f"{domain} läuft in {days_remaining} Tagen ab.")
                print(Fore.YELLOW  + f"{domain} läuft in {days_remaining} Tagen ab.")

        else:
            #pass
            print(Style.RESET_ALL + f"Konnte das Ablaufdatum für {domain} nicht ermitteln.")

    except Exception as e:
        print(Style.RESET_ALL + f"Fehler beim Überprüfen von {domain}: {str(e)}")



#name_server = get_ns("ar")

#print(name_server)

'''
tlds = get_tlds()

#xxxprint(tlds)


print("Verfügbare TLDs:")
for tld in tlds:
    pass
    #print(tld)

'''



for tld in top_level_domains:
    #domain = input("Gib eine TLD-Domain ein (z.B. example.com): ")
    name_server = get_ns(tld)

    print(Style.RESET_ALL + tld)
    print(Style.RESET_ALL + "----------------------------------------")

    for ns in name_server:
        check_domain_expiry(ns)
        time.sleep(1)

    print(Style.RESET_ALL + "----------------------------------------")
