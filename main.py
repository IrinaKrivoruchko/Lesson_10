class Build:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year, ". City: ", self.city, sep='')

class School(Build):
    __pupils = None

    def __init__(self, year, city, pupils):
        super(School, self).__init__(year, city)
        self.__pupils = pupils

    #полиморфизм
    def get_info(self):
        print("Year: ", self.year, ". City: ", self.city, ". There are: ", self.__pupils, " pupils", sep='')


class Shop(Build):
    __employees = None

    def __init__(self, year, city, employees):
        super(Shop, self).__init__(year, city)
        self.__employees = employees

    def get_info(self):
        print("Year: ", self.year, ". City: ", self.city, ". There are: ", self.__employees, " employees", sep='')

class House(Build):
    __number_of_people_in_family = None

    def __init__(self, year, city, number_of_people_in_family=4):
        super(House, self).__init__(year, city)
        self.__number_of_people_in_family = number_of_people_in_family

    def get_info(self):
        print("Year: ", self.year, ". City: ", self.city, ". There are ", self.__number_of_people_in_family, " people", sep='')

build1 = Build(1990, 'BuildCity')

#наследование
school1 = School(2000, 'SchoolCity', 500)

#инкапсуляция
school1.__pupils = 1000 # не сработает, потому как доступа нет. только через конструктор

shop1 = Shop(2020, 'ShopCity', 30)

# number_of_people_in_family можем не вводить. стоит значение по умолчанию
house1 = House(2003,'HouseCity')

build1.get_info()
school1.get_info()
shop1.get_info()
house1.get_info()