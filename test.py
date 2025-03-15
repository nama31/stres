from collections import defaultdict 

# class Book:
#     def __init__(self):
#         self.books = {}
#         self.personBook = []



#     def addBook(self,name,book_name,pages,type):
#         self.name = name 
#         self.page = pages
#         self.type = type
#         self.book_name = book_name
#         self.books.append((name, book_name,type ,pages))

#     def deleteBook(self,name):
#         del self.books[name]
#         print("the book has been delete")

        
#     def PersonBook(self,name):
#         # return self.books[name]
#         arr = []
#         arr.append(v for k,v in self.books if k == name)
#         return arr
    



# aman = Book()
# aman.addBook('aman','dora',504,'roman')

# aman.addBook('aman','dm',234,'lovly roman')

# print(aman.PersonBook('aman'))

        
# class Client:
#     def __init__(self,name):
#         self.name = name 
#         self.history = defaultdict(str)



# class Barbershop:
#     def __init__(self):
#         self.history = defaultdict(str)
#         self.total = 0
#         self.hair_cats = defaultdict(int)


#     def addHairCats(self,haircat,cost):
#         self.hair_cats[haircat] = cost

#     def deleteHairCat(self,haircat):
#         del self.hair_cats[haircat]
    

#     def showHairCats(self):
#         return self.hair_cats
    
        
#     def addHistory(self,name,haircat):
#         self.history[Client(name)] = haircat



#     def chek(self,name,hair_cat):
#         self.total += self.hair_cats[hair_cat]
#         return self.hair_cats[hair_cat]


        
# aman = Client('aman')
        
# catch = Barbershop()

# catch.addHairCats('model',500)
# catch.addHairCats('short',300)
# catch.addHairCats('long',700)

# catch.addHistory('aman','long')
# print(catch.showHairCats())
# print(catch.chek('aman','long'))



# class Client:
#     def __init__(self,name,sit):
#         self.name = name 
#         self.sit= sit




# class Airlane:
#     def __init__(self,AirType):
#         self.AirType = AirType
#         self.history = defaultdict(str)
#         self.sits = defaultdict(int)

#     def AddSit(self,sit,cost):
#         self.sits[sit] = cost 

#     def AddHistory(self,name,sit):
#         self.history[Client(name,sit)] =sit

#     def ShowHistory(self):
#         return self.history


# aman = Client('aman','a2')

# boing = Airlane('boing')

# boing.AddHistory('aman','a2')

# print(boing.ShowHistory('aman','a2'))


# from datetime import datetime , time

# class Auto:
#     def __init__(self,name,auto):
#         self.name = name 
#         self.auto = auto 
        

# class Parking:
#     def __init__(self):
#         self.history = defaultdict(list)
#         self.mestos = defaultdict(int)
#         self.now = defaultdict(str)



#     def AddAuto(self,name,auto,mesto):
#         self.now[mesto] = Auto(name,auto)
#         self.history[name].append(mesto)
#         self.mesto[mesto] = 1

#     def DeleteAuto(self,mesto):
#         del self.now[mesto]
#         del self.mesto[mesto]

#     def ShowNow(self):
#         for k,v in self.now().items():
#             print(k,v)


# aman = Auto('aman','bmw')

# cach = Parking()

# cach.AddAuto('aman','bmw','a2')

# cach.ShowNow()

# class Client:
#     def __init__(self):
#         self.history = []
#         self.database = defaultdict(int)
        
#     def GetBalanse(self,name,balance):
#         self.database[name] = balance 
#         self.history.append(name)

#     def addBalance(self,name,amount):
#         self.database[name] += amount

#     def MinusBalance(self,name,amount):
#         if self.database[name] >= amount:
#             self.database[name] -= amount
#             return True
#         else:
#             return False

#     def ShowBalance(self,name):
#         return self.database[name]



# class Moves:
#     def __init__(self):
#         self.moves = defaultdict(list)

#     def AddMove(self,name,hall,cost):
#         self.moves[hall].append((name,cost))

#     def delete(self,hall):
#         del self.moves[hall]


#     def ShowCost(self,moveName,hall):
#         return[cost for move,cost in  self.moves[hall] if move == moveName]


    


# class Sits:
#     def __init__(self):
#         self.seats = defaultdict(lambda:defaultdict(int))

#     def AddSeats(self,hall,seat):
#         self.seats[hall][seat] = 0

#     def Book(self,hall,seat):
#         if self.seats[hall][seat] == 0:
#             self.seats[hall][seat] = 1
#         else:
#             return 'was book it'    

#     def updete(self,hall):
#         for seat ,type in self.seats[hall].items():
#             type = 0

#     def showSeats(self):
#         return self.seats



# class Cinemat:
#     def __init__(self,seats,movies,client):
#         self.profit = 0 
#         self.seats = seats 
#         self.movies = movies
#         self.client = client 

#     def BookTheSeat(self,hall,seat):
#         if self.seats.Book(hall,seat):
#             return 'booked'
#         return 'bookt for you'
        


        
#     def Chek(self,client,name,hall,move,count):
#         cost = self.movies.ShowCost(move,hall)
#         total_cost = cost[0] * count 
#         self.profit += total_cost 
#         self.client.MinusBalance(name,total_cost)

# clients = Client()
# movies = Moves()
# seats = Sits()
# cinema = Cinemat(seats, movies,clients)

# # Инициализируем данные
# clients.GetBalanse('aman', 1200)
# movies.AddMove('the end', 'imax', 450)
# seats.AddSeats('imax', 'a1')

# # Бронирование мест и расчет чека
# print(cinema.BookTheSeat('imax', 'a1'))  # Успешное бронирование
# print(cinema.Chek(clients, 'aman', 'imax', 'the end', 2))  # Покупка билета

# # Показать текущие места и баланс клиента
# print(seats.showSeats())
# print(clients.ShowBalance('aman'))



# class Client:
#     def __init__(self,name):
#         self.name = name
#         self.balance = defaultdict(int)

#     def addBalance(self,name,amount):
#         self.balance[name]+=amount 


#     def minusBalance(self,name,amount):
#         if amount > self.balance[name]:
#             return 'in your balance do not have such money'
#         else:
#             self.balance[name] -= amount

#     def ShowBalance(self,name):
#         return self.balance[name]

    
# class Tovar:
#     def __init__(self):
#         self.products = defaultdict(int)
#         self.count = defaultdict(int)
#         self.zakup = 0

#     def addProducts(self,name,cost):
#         self.products[name] = cost

#     def addCount(self,name,count):
#         self.count[name] +=count
#         self.zakup += self.products[name] *count

#     def minusCount(self,name,count):
#         if count > self.count[name]:
#             return 'tovr not in'
#         self.count[name] -= count

#     def ShowPrice(self,name):
#         return self.products[name] 

#     def ShowCount(self,tovarname):
#         return self.count[tovarname]



# class Shop:
#     def __init__(self,client,tovar):
#         self.client = client 
#         self.tovar = tovar 
#         self.pribl = 0

#     def chek(self,name,tovarname,count):
#         total = self.tovar.ShowPrice(tovarname) *count 
#         self.client.minusBalance(name,total)
#         self.tovar.minusCount(tovarname,count)
#         self.pribl += total
#         return f'your chek is {total}' 

#     def viruchka(self):
#         return self.pribl - self.tovar.zakup

        
# aman = Client('aman')
# aman.addBalance('aman',1200)
# print(aman.ShowBalance('aman'))


# cola = Tovar()
# cola.addProducts('cola',55)
# cola.addCount('cola',30)
# print(cola.ShowPrice('cola'))


# shop = Shop(aman,cola)
# print(shop.chek('aman','cola',2))

# print(aman.ShowBalance('aman'))
# print(cola.ShowCount('cola'))
# print(shop.viruchka())

# from datetime import datetime

# # Получить текущую дату и время
# now = datetime.now()
# dates = now.date()
# hours = now.hour
# minuts = now.minute + (hours * 60)  # Минуты с начала суток


# class Car:
#     def __init__(self, id):
#         self.id = id
#         self.history = defaultdict(int)
#         self.time = minuts  # Время въезда
#         self.date = dates
#         self.from_time = 0

#     def TimeNow(self):
#         self.from_time = minuts  # Установить текущее время

#     def ChekNumber(self):
#         return self.id

#     def AddHistory(self):
#         self.history[self.date] += 1


# class Plase:
#     def __init__(self):
#         self.place = defaultdict(int)  # Цены для мест
#         self.mests = defaultdict(int)  # Количество свободных мест

#     def AddPlace(self, plasename, price, count):
#         self.place[plasename] = price  # Установить цену
#         self.mests[plasename] = count  # Установить количество мест

#     def Book(self, plasename):
#         if self.mests[plasename] > 0:  # Проверить наличие мест
#             self.mests[plasename] -= 1
#         else:
#             print(f"No available places for {plasename}")

#     def Away(self, plasename):
#         self.mests[plasename] += 1

#     def ShowMest(self, plasename):
#         return self.mests[plasename]

#     def ShowCostPlace(self, plasename):
#         return self.place[plasename]


# class Parking:
#     def __init__(self, car, place, placename):
#         self.car = car
#         self.place = place
#         self.placename = placename  # Название места
#         self.history = defaultdict(int)
#         self.pribl = 0  # Прибыль
#         self.cost = self.place.ShowCostPlace(self.placename)

#     def Chek(self):
#         self.car.TimeNow()
#         self.place.Book(self.placename)  # Забронировать место

#     def GetPrice(self):
#         if self.car.ChekNumber() == "en":
#             return 0  # Бесплатно для определённых номеров
#         end_time = minuts  # Текущее время
#         total = (end_time - self.car.time) * self.cost  # Общая стоимость
#         self.pribl += total
#         self.place.Away(self.placename)  # Освободить место
#         return total


# # Создание машины
# toyota = Car("en23")
# toyota.AddHistory()

# mars = Car('mr54')
# mars.AddHistory()

# # Создание парковочного места
# dordoy = Plase()
# dordoy.AddPlace("dordoy", 5, 250)  # Место "dordoy" с ценой 5 и 250 местами

# # Создание парковки
# man = Parking(toyota, dordoy, "dordoy")
# tot = Parking(mars,dordoy,'dordoy')
# # Забронировать место и рассчитать стоимость
# man.Chek()
# print(man.GetPrice())

# tot.Chek()
# print(tot.GetPrice())



# class Barber:
#     def __init__(self, name, price, start_time, end_time):
#         self.name = name
#         self.price = price
#         self.start_time = start_time
#         self.end_time = end_time
#         self.earnings = 0

#     def add_earning(self, amount):
#         self.earnings += amount

#     def subtract_earning(self, amount):
#         self.earnings -= amount

#     def get_schedule(self):
#         return f"{self.start_time} - {self.end_time}"


# class Barbershop:
#     def __init__(self):
#         self.masters = {}
#         self.reservations = {}

#     def add_master(self, name, price, start_time, end_time):
#         self.masters[name] = Barber(name, price, start_time, end_time)

#     def remove_master(self, name):
#         if name in self.masters:
#             del self.masters[name]

#     def get_available_spots(self, name, date):
#         if name not in self.masters:
#             return f"Мастер {name} не найден."
#         master = self.masters[name]
#         start_time = int(master.start_time.split(':')[0])
#         end_time = int(master.end_time.split(':')[0])
#         reserved = [int(res.split()[1].split(':')[0]) for res, info in self.reservations.items() if info['мастер'] == name and res.startswith(date)]
#         available = [f"{hour}:00" for hour in range(start_time, end_time) if hour not in reserved]
#         return available

#     def reserve(self, name, date_time, client):
#         if name not in self.masters:
#             return f"Мастер {name} не найден."
#         if date_time in self.reservations:
#             return "Этот временной слот уже занят."
#         self.reservations[date_time] = {'мастер': name, 'клиент': client}
#         self.masters[name].add_earning(self.masters[name].price)

#     def get_history(self, name):
#         if name not in self.masters:
#             return f"Мастер {name} не найден."
#         history = [f"{time}: {info['клиент']}" for time, info in self.reservations.items() if info['мастер'] == name]
#         return history if history else f"У мастера {name} нет записей."

#     def get_kassa(self):
#         return sum(master.earnings for master in self.masters.values())

#     def get_earnings_master(self, name):
#         if name in self.masters:
#             return self.masters[name].earnings
#         return f"Мастер {name} не найден."

#     def cancel_reservation(self, client, date_time):
#         if date_time in self.reservations and self.reservations[date_time]['клиент'] == client:
#             master_name = self.reservations[date_time]['мастер']
#             self.masters[master_name].subtract_earning(self.masters[master_name].price)
#             del self.reservations[date_time]

# barber_shop = Barbershop()
# barber_shop.add_master("gulnur", 500, "9:00", "17:00")
# print("Доступные слоты:", barber_shop.get_available_spots("gulnur", "11-11-2024"))
# barber_shop.reserve("gulnur", "11-11-2024 16:00", "emi")
# barber_shop.reserve("gulnur", "11-11-2024 10:00", "ayan")
# print("История:", barber_shop.get_history("gulnur"))
# print("Доход мастера gulnur:", barber_shop.get_earnings_master("gulnur"))
# print("Касса:", barber_shop.get_kassa())
# barber_shop.cancel_reservation("emi", "11-11-2024 16:00")
# print("Касса после отмены:", barber_shop.get_kassa())

# barber_shop.add_master('aman',450,'11:00','17:00')
# barber_shop.cancel_reservation('')



# class Sits:
#     def __init__(self):
#         self.sits = defaultdict(int)
#         self.book = defaultdict(int)

#     # def addSit()

# from time import time
# from random import randint 
# arr = []
# t1 = time()
# for i in range(10000):
#     r = randint(0,10)
#     arr.append(r)
# sumi = 0
# for g in range(0,10000):
#     sumi += arr[g]
# t2 = time()
# print(sumi,t2 - t1)

