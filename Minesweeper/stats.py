import time
from datetime import datetime, date



#before the first click
start_time = time.time()

dateandtime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
date1, time1 = dateandtime.split()
amountofmines = inp_m

#if the game is won
result = 'win'


#if the game is lost
result = 'loss'


#after the end of the game
end_time = time.time()
minutes = (end_time-start_time)//60

#if loss

for h in field:
    if field[x_real][y_real] == 'f' and real_field[x_real][y_real] == 'x':
        amountofmines = amountofmines - 1
    else:
        pass

#if win
amountofmines = 0



#when calling stats
print(f'the game was played for {int(end_time-start_time)//60} minutes and {(int(end_time-start_time))-((int(end_time-start_time)//60)*60)} seconds')

def add(stats):
    stats.append({
                "date": date1,
                "time": time1,
                "minutes": minutes, 
                "turns": moves,
                "result": result,
                "mines": amountofmines
            })



def stat_begin():


def statistics():
    for i, stat in enumerate(stats):
        print (f" {i}. date: {date1}, time: {time1}, length: {minutes} minutes, turns: {moves}, result: {result}, mines left: {amountofmines}")ef statistics():
    for i, stat in enumerate(stats):
        print (f" {i}. date: {date1}, time: {time1}, length: {minutes} minutes, turns: {moves}, result: {result}, mines left: {amountofmines}")


xd = []
x = 1
y = 2
z = 3

xd.append({
    "one": x,
    "two": y,
    "three": z
    })
for i, stat in enumerate(xd):
    print(f"{i+1}. one: {x}, two: {y}, three: {z}")