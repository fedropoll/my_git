class BankAccount:
    def __init__(self, balance=0):
        self.__balance = max(0, balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount


class Student:
    def __init__(self, age=0):
        self.__age = max(0, age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value >= 0:
            self.__age = value


class Car:
    def __init__(self, speed=0):
        self.__speed = self.__validate_speed(speed)

    def __validate_speed(self, value):
        return value if 0 <= value <= 300 else self.__speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if 0 <= value <= 300:
            self.__speed = value


class User:
    def __init__(self, password):
        self.__password = password if len(password) >= 6 else "default123"

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password


class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        if value >= -273.15:
            self.__celsius = value

    def get_fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

