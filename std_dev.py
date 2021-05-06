# Author: Samuel Bennett
# Date: 4/28/2021
# Description: A class called Person that has two private data members - the person's name and age and an init method that takes two values and uses them to initialize the data members. A separate function called std_dev that takes as a parameter a list of Person objects and returns the standard deviation of all their ages.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age


def std_dev(person_list):
    n = 0
    for person in person_list:
        n += person._age
    n /= len(person_list)
    total = 0
    for person in person_list:
        total += (person._age - n) ** 2
    return (total / len(person_list)) ** 0.5


p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)

person_list = [p1, p2, p3]

answer = std_dev(person_list)

print(answer)
