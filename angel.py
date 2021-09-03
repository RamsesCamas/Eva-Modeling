class Angel:

    def __init__(self,number,name):
        self.number = number
        self._name = name
        self._at_field = False
    
    def attack(self,city):
        city.add_angel(self)

    def auto_kill(self):
        return 'BOOM'

    def act_at_field(self):
        self._at_field = True
        return 'AT Field Activated'
    
    def get_at_field(self):
        return self._at_field

    def deac_at_field(self):
        self._at_field = False
        return 'At Field Broken'

    def try_third_impact(self,eva):
        if eva.get_model() == '00':
            return 'Tsubasa wo Kudasai'
        elif eva.get_model() == '01':
            return 'Komme Susser Tod'
        else:
            return 'Third Impact Failed'