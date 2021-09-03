class Pilot:

    def __init__(self,name,age,eva):
        self.name = name
        self.age = age
        self.eva = eva
        self.get_ready()
    
    def get_ready(self):
        if self.name == 'Shinji':
            print('Cries')
        