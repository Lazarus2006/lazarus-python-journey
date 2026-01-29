import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time 
import datetime
import random

file = "python/tone.mp3"

def stop_alarm():
    first_number = random.randint(-99,99)
    second_number = random.randint(-99,99)
    option = ("+" , "-" , "*" , "/")
    sign = random.choice(option)
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: (a / b) if b != 0 else None, 
    }
    answer = ops[sign](first_number, second_number)
    answer = round(answer, 2)
    while True:
        try:
            print(f" what is {first_number} {sign} {second_number}")    
            user = float(input("enter the answer to stop the alarm : "))
            if user == answer:
                exit(0)
            else:
                print("Your answer is incorrect !")
                continue
        except ValueError:
            print("Provide the correct values")
            continue


while True:
    try:
        Hour = int(input("enter the hour (HH): "))
        if Hour < 24 and Hour >= 0:
            break
        else:
            print("Please Enter valid input")
            continue
    except ValueError:
        print("Please Enter valid input")
        continue

while True:
    try:
        Minutes = int(input("enter the minutes (MM): "))
        if Minutes < 60 and Minutes >= 0:
            break
        else:
            print("Please Enter valid input")
            continue
    except ValueError:
        print("Please Enter valid input")
        continue

while True:
    try:
        Seconds = int(input("enter the Seconds (SS): "))
        if Seconds < 60 and Seconds >= 0:
            break
        else:
            print("Please Enter valid input")
            continue
    except ValueError:
        print("Please Enter valid input")
        continue

alarm_time = f"{Hour:02d}:{Minutes:02d}:{Seconds:02d}"

print(f"alarm set for {alarm_time}")
time.sleep(3)

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)
    if current_time == alarm_time:
        print("wake up!")
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loops=-1)
        stop_alarm()

    else:
        continue


