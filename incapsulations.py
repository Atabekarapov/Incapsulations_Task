# WEEK7. TASK2. ATABEK
# 1)
'''Создайте класс Car. Пропишите в __init__ параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью приватного
метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”'''

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70
    
#     def __add_distance(self, km):
#         self.odometer = km

#     def drive(self, km):
#         if self.fuel * 10 >= km:
#             self.__add_distance(km)
#             self.__subtract_fuel(km // 10)
#             print('Let’s drive!')
#         else:
#             print('Need more fuel, please, fill more!')

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel



#     def __add_distance(self, km):
#         self.odometer = km

    
# fit = Car('German', 'BMW Samurai', '2018')
# fit.drive(1000)
# print(fit.odometer)
# print(fit.fuel)

# 2)
'''Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.'''

# class Phone:
#     __imei = 'qwerty12345'
#     __charge = 100

#     if __charge == 0:
#         raise Exception('Please charge your phone!')
#     def listen_music(self):
#         self.__charge -= 5
#         print('Listening to music.')

#     def watch_videos(self):
#         if self.__charge >= 10:
#             self.__charge -= 5
#             print('You are allowed to watch the videos!')
#         elif self.__charge <= 10:
#             print(('You are not allowed to watch the videos!'))
#     def charge_is_charging(self):
#         self.__charge = 100

#     def all_info(self):
#         print(self.__charge)

# battery = Phone()
# battery.listen_music()
# battery.watch_videos()
# battery.all_info()
# battery.charge_is_charging()
# battery.all_info()

    
# 3)
'''Создайте класс правильной пирамиды с основанием в виде квадрата. Создайте
непубличные атрибуты для длины основания и ребра её грани. Создайте публичные методы
для задания атрибутов, а также для вычисления площади и объёма.'''











        
