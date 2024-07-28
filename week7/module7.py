TRAP_ARTISTS =['Demi','Hannah','JB']

class TrapArtist:

    def __init__(self,name) :
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if name  not in TRAP_ARTISTS:
            raise ValueError("Not in our arrtists")
        self._name=name

rr =TrapArtist("JB")