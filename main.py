from pilot import Pilot
from eva import Eva
from angel import Angel
from city import City
from random import uniform

def run_sim():
    Tokio_3 = City('Tokio-3','Japan')
    print(Tokio_3.get_status())

    Rei = Pilot('Rei',14,'00')
    Shinji = Pilot('Shinji',14,'01')
    Eva_00 = Eva('00')
    Eva_01 = Eva('01')

    Eva_01.start(Rei)
    Eva_01.start(Shinji)
    Eva_00.start(Rei)

    Sachiel = Angel(4,'Sachiel')
    Sachiel.attack(Tokio_3)
    print(Tokio_3.get_status())

    Eva_01.fight()
    Eva_00.fight()

    angel_choice = round(uniform(-.5,1.49))
    if angel_choice == 0:
        print(Sachiel.act_at_field())
        if Sachiel.get_at_field():
            print(Eva_01.set_at_field(Sachiel))
    else:
        print(Sachiel.try_third_impact(Eva_00))

if __name__ == '__main__':
    run_sim()