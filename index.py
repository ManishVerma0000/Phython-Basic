
import datetime

name = input("please enter the name")
lastname = input('enter the last name of the user')
def greetings():
    hour = datetime.datetime.today().hour
    x = f"hii Mr.{name} ,{lastname} user"

    if (hour < 12):
        time = 'good morning'
        print(f"hii Mr.{name}, {lastname} {time}")
    else:
        print(f"hii Mr.{name} ,{lastname} good evening")

greetings()
