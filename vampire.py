class Vampire:

    vampires_in_coven = []

    def __init__(self, name, age, coffin, drank_blood):
        self.name = name 
        self.age = age
        self.in_coffin = coffin
        self.drank_blood = drank_blood

    # def __repr__(self):
    #     return self.name

    def drink_blood(self):
            self.drank_blood_today = True

    def go_home(self):
        for self in self.vampires_in_coven:
                self.in_coffin = True

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood):
        new_vampire = Vampire(name, age, in_coffin, drank_blood)
        cls.vampires_in_coven.append(new_vampire)
        return new_vampire

    @classmethod
    def sunrise(cls):
        if vampire.drank_blood_today and vampire.in_coven:
            vampire.in_coffin = True


    @classmethod
    def sunset(cls):
        for _vampire in cls.vampires_in_coven:
            cls.in_coffin = False
            cls.drank_blood_today = False
        
tommy_vampire = Vampire.create('Tommy', 32, True, False)
jarvis_vampire = Vampire.create('Jarvis', 40, True, False)
tracey_vampire = Vampire.create('Tracey', 42, True, False)
mike_vampire = Vampire.create('Mike', 50, True, False)
sean_vampire = Vampire.create('Mike', 50, True, False)

# print(my_vampire)

Vampire.sunset()
tommy_vampire.drink_blood()
tommy_vampire.go_home()
for vampire in Vampire.vampires_in_coven:
    print(vampire.name)
jarvis_vampire.drink_blood()
tracey_vampire.drink_blood()
print('')
tracey_vampire.go_home()
if tracey_vampire.vampires_in_coven:
    print("she's there")
mike_vampire.go_home()
print('')
if mike_vampire.vampires_in_coven:
    print("he's there")
Vampire.sunrise()
print('')
for vampire in Vampire.vampires_in_coven:
    print(vampire.name) 

# if vampire not in Vampire.vampires_in_coven:
#     print("Don't yet know how")
# else:
#     print(f"{vampire.name} was burned to all holy hell buy the light!")



