class Roommate:
    def __init__(self):
        self.name=input("Enter name: ")
        self.date=input('Start date: ')
        self.time=int(input('lived: '))
    def total_time(self):
        return self.time
    def guest_name(self):
        return self.name
    def start_date(self):
        return self.date

class Hotel:
    def __init__(self):
        self.total_rent=int(input('Total rent:'))
    def calculate_rent(self,time1,time2):
        all_time=time1 + time2
        self.price1= int(time1*(self.total_rent/all_time))
        self.price2= int(time2*(self.total_rent/all_time))
    def bill(self,person1,person2):
        print(person1,'total price is',self.price1)
        print(person2,'total price is',self.price2)
