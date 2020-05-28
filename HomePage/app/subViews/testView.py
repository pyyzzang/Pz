from django.http import HttpResponse;
from django.template import loader;
from django.shortcuts import render

class Person():
    def __init__(self, Name, Age):
        self.Name = Name;
        self.Age = Age;
    def getName(self):
        return self.Name;
    def getAge(self):
        return self.Age;
    


class testView():
    @staticmethod
    def test(request):
        PersonList = [];
        PersonList.append(Person("1", 10));
        PersonList.append(Person("3", 12));
        PersonList.append(Person("2", 16));
        PersonList.append(Person("6", 60));
        PersonList.append(Person("4", 80));
        PersonList.append(Person("8", 50));
        PersonList.append(Person("1", 20));
        #PersonList = PersonList.order_by("Name");
        context = {"PersonList" : PersonList};
        return render(request, 'index.html', context);