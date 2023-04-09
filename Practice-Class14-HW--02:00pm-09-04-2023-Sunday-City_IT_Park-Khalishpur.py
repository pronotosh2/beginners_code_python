





#HW--02:00pm-09-04-2023-Sunday-City_IT_Park-Khalishpur.py
class Profile:
    def __init__(self,name,roll,registration,_class,age,address,favorite_place,favorite_sport,email,password,phone_no,facebook,github,employers_contact):
        self.name=name
        self.roll=roll
        self.registration=registration
        self._class=_class
        self.age=age
        self.address=address
        self.favorite_place=favorite_place
        self.favorite_sport=favorite_sport
        self.email=email
        self.password=password
        self.phone_no=phone_no
        self.facebook=facebook
        self.github=github
        self.employers_contact=employers_contact

    def public(self):
        print("Name: " + self.name, ", Roll: " + self.roll, ", Class: " + self._class, ", Age: " + self.age, ", Phone no: " + self.phone_no, ", FB: " + self.facebook, ", GitHub: " + self.github)
    def friend(self):
        print(" Registration: " + self.registration,", Address: " + self.address, ", Favorite place: " + self.favorite_place, ", Favorite Sport: " + self.favorite_sport, ", Email: " + self.email)
    def only_me(self):
        print(" Password: " + self.password,", Employer's contact: " + self.employers_contact)

Saikat=Profile("Saikat","001","221","5","22","New_market","Sundarbans","Cricket","saikat@gmail.com","sfdfdsfj","01777888999","Saikat12","github/saikat5","01666777888")
Akash=Profile("Akash","002","222","1","21","Sonadanga","Sundarbans","Cricket","Akash@gmail.com","sfAkshfj","01777008999","Akasht12","github/Akash5","01666777888")
Nabab=Profile("Nabab","003","223","3","22","Khalishpur","Sylhet","Cricket","Nabab@gmail.com","sfNababj","01777338999","Nabab12","github/Nabab5","01600743888")
Milon=Profile("Milon","004","224","5","23","Boyra","Sundarbans","Football","Milon@gmail.com","sEkmmrn","01777855999","Milon12","github/Milon5","01666547888")
Emran=Profile("Emran","005","225","3","25","Zero_point","Kuakata","Badminton","Emran@gmail.com","sfdfdsfj","01733388999","Emran12","github/Emran5","01666677888")
Nayon=Profile("Nayon","006","226","2","24","New_market","Sundarbans","Football","Nayon@gmail.com","sfdsfj","01756588999","Nayon12","github/Nayon5","01666887888")
Kamal=Profile("Kamal","007","227","1","23","Rupsa","Dhaka","Cricket","Kamal@gmail.com","sfdfdsfj","01775888999","Kamal12","github/Kamal5","01666877888")
Rafiq=Profile("Rafiq","008","228","5","22","New_market","Sundarbans","Cricket","Rafiq@gmail.com","sfdfdsfj","01775688999","Rafiq","github/Rafiq5","01666787888")

Saikat.public()
Saikat.friend()
Saikat.only_me()

print("________________________________________________________")

Akash.public()
Akash.friend()
Akash.only_me()

print("________________________________________________________")

Nabab.public()
Nabab.friend()
Nabab.only_me()

print("________________________________________________________")

Milon.public()
Milon.friend()
Milon.only_me()

print("________________________________________________________")

Emran.public()
Emran.friend()
Emran.only_me()

print("________________________________________________________")

Nayon.public()
Nayon.friend()
Nayon.only_me()

print("________________________________________________________")

Kamal.public()
Kamal.friend()
Kamal.only_me()

print("________________________________________________________")

Rafiq.public()
Rafiq.friend()
Rafiq.only_me()




class Profile:
    def __init__(self,name,roll,registration,_class,age,address,favorite_place,favorite_sport,email,password,phone_no,facebook,github,employers_contact):
        self.short_name=name
        self.roll=roll
        self.regi=registration
        self._cls=_class
        self.age=age
        self.add=address
        self.fav_place=favorite_place
        self.fav_sport=favorite_sport
        self.email=email
        self.pas=password
        self.phone=phone_no
        self.fb=facebook
        self.github=github
        self.emp_contact=employers_contact

    def public(self):
        print("Name: " + self.short_name, ", Roll: " + self.roll, ", Class: " + self._cls, ", Age: " + self.age, ", Phone no: " + self.phone, ", FB: " + self.fb, ", GitHub: " + self.github)
    def friend(self):
        print(" Registration: " + self.regi, ", Address: " + self.add, ", Favorite place: " + self.fav_place, ", Favorite Sport: " + self.fav_sport, ", Email: " + self.email)
    def only_me(self):
        print(" Password: " + self.pas,", Employer's contact: " + self.emp_contact)

Saikat=Profile("Saikat","001","221","5","22","New_market","Sundarbans","Cricket","saikat@gmail.com","sfdfdsfj","01777888999","Saikat12","github/saikat5","01666777888")
Akash=Profile("Akash","002","222","1","21","Sonadanga","Sundarbans","Cricket","Akash@gmail.com","sfAkshfj","01777008999","Akasht12","github/Akash5","01666777888")
Nabab=Profile("Nabab","003","223","3","22","Khalishpur","Sylhet","Cricket","Nabab@gmail.com","sfNababj","01777338999","Nabab12","github/Nabab5","01600743888")
Milon=Profile("Milon","004","224","5","23","Boyra","Sundarbans","Football","Milon@gmail.com","sEkmmrn","01777855999","Milon12","github/Milon5","01666547888")
Emran=Profile("Emran","005","225","3","25","Zero_point","Kuakata","Badminton","Emran@gmail.com","sfdfdsfj","01733388999","Emran12","github/Emran5","01666677888")
Nayon=Profile("Nayon","006","226","2","24","New_market","Sundarbans","Football","Nayon@gmail.com","sfdsfj","01756588999","Nayon12","github/Nayon5","01666887888")
Kamal=Profile("Kamal","007","227","1","23","Rupsa","Dhaka","Cricket","Kamal@gmail.com","sfdfdsfj","01775888999","Kamal12","github/Kamal5","01666877888")
Rafiq=Profile("Rafiq","008","228","5","22","New_market","Sundarbans","Cricket","Rafiq@gmail.com","sfdfdsfj","01775688999","Rafiq","github/Rafiq5","01666787888")

Saikat.public()
Saikat.friend()
Saikat.only_me()

print("________________________________________________________")

Akash.public()
Akash.friend()
Akash.only_me()

print("________________________________________________________")

Nabab.public()
Nabab.friend()
Nabab.only_me()

print("________________________________________________________")

Milon.public()
Milon.friend()
Milon.only_me()

print("________________________________________________________")

Emran.public()
Emran.friend()
Emran.only_me()

print("________________________________________________________")

Nayon.public()
Nayon.friend()
Nayon.only_me()

print("________________________________________________________")

Kamal.public()
Kamal.friend()
Kamal.only_me()

print("________________________________________________________")

Rafiq.public()
Rafiq.friend()
Rafiq.only_me()
