from random import randint

class Eva:
    def __init__(self,model):
        self.status = 'OFF'
        self.weapon = ''
        self.SIZE = 75
        self._model = model

    def start(self,Pilot):
        self.status = 'ON'
        self._sync_pilot(Pilot)
    
    def fight(self):
        self.choice_weapon()
        
    def _sync_pilot(self,Pilot):
        try:
            if self.get_model() == Pilot.eva:
                print('Stable')
            else:
                raise Exception
        except Exception as e:
            print('Syncronitation Error')

    def choice_weapon(self):
        weapons = ['Longinus Lance','Progressive Knife','Assaltus Rifle','Positron Rifle']
        choice = randint(0,len(weapons)-1)
        self.weapon = weapons[choice]

    def set_at_field(self,Angel):
        status = Angel.deac_at_field()
        return status

    def get_model(self):
        return self._model