class Qrumpet:
    leg = 'none'
    hair = "Qiu's New Haircut"
    number_of_people_doughing_it = 999
    def __init__(self,leg,hair="Qiu's New Haircut"):
        self.leg = leg
        self.hair = hair
    def print(self):
        print(self.leg)
        print(self.hair)
        print(self.number_of_people_doughing_it)
pancake = Qrumpet('none')
print(pancake.leg + ' ' + pancake.hair)
pancake.hair = "Paul's new hair colour"
print(pancake.hair + " Qiu's haircut " +pancake.leg)
pancake1 = Qrumpet('8')
pancake2 = Qrumpet('16', "Yoga")

pancake.print()
pancake1.print()
pancake2.print()