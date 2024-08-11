class Mot():

    def __init__(self,mot : str,traduction : str,connet : bool) -> None:
        
        self.mot = mot
        self.traduction = traduction 
        self.connet = connet

    def __str__(self) -> str:
       return f"mot:{self.mot}; trad : {self.traduction}; connet : {self.connet}"
    
