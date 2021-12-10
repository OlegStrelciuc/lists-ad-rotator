from os import system
from time import sleep
ads = [
    "Buy this Python book for only 0.99$",
    "Try this course of Python for free!!!",
    "Drink a lot of water (2L per day minimum)"
]

ads_duration = [
    1.0,
    3.5,
    5.0
]
#Method 1: index only
#index = 0
#while True:
#    system("cls")
#    print(" >> ", ads[index], " << ")
#    sleep(3)
#    index += 1
#    if index >= len(ads):
#        index = 0

# Method 2: methods only
while True:
    ad = ads.pop(0)
    ai = ads_duration.pop(0)


    system("cls")
    print(" >> ", ad, " << ")
    sleep(ai)


    ads.append(ad)
    ads_duration.append(ai)