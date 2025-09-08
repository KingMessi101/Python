import random
fname = ['John', 'Jane', 'Corey', 'Travis']
lname = ['Smith', 'Doe', 'Jenkins', 'Robinson']
street_names = ['Main', 'High', 'Pearl', 'Maple']
fake_cities = ['Metropolis', 'Eerie', "King's Landing"]
states = ['AA', 'AE', 'AP', 'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT']

class Name:
    def __init__(self, num=1):
        self.num = num
    def first_name(self):
        for i in range(self.num):
            first = random.choice(fname)
        print(first)

    def last_name(self):
        for i in range(self.num):
            last = random.choice(lname)
            print(last)

    def full_name(self):
        for i in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            print(f'{first} {last}')

    def full_profile(self):
        for i in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            phone = f'+91-{random.randint(800, 999)}-{random.randint(800, 999)}{random.randint(1000, 9999)}'

            street_num = random.randint(100, 999)
            street = random.choice(street_names)