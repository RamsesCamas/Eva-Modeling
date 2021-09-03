class City:

    def __init__(self,name,region):
        self.name = name
        self.region = region
        self.angels = []
        self._status = 'OK'

    def add_angel(self,angel):
        if len(self.angels) == 0:
            self._status = 'DANGER'
        self.angels.append(angel)
        

    def get_angels(self):
        total_angels = len(self.angels)
        if total_angels == 0: 
            self._status = 'OK'
            return 'La ciudad está a salvo'
        else:
            return len(self.angels)
    
    def get_status(self):
        return self._status