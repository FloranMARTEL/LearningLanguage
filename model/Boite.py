import datetime 

from Mot import Mot

class Boite():

    def __init__(self,date : datetime.datetime,mots : list[Mot]) -> None:
        
        self.date = date
        self.mots = mots



b = Boite(datetime.datetime(2024, 8, 12),Mot("bonjour","hello",False))
print(b)