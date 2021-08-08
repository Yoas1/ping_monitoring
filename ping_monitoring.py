import os
import sys
import matplotlib.pyplot as plt
from datetime import datetime

#close app
condition = True
fig, ax = plt.subplots()
def on_close(evt=None):
    global condition
    condition = False
fig.canvas.mpl_connect('close_event', on_close)
#######
print('The computer`s operating system is:', sys.platform)
ip = input('Enter ip address to ping:')
inter = input('time to interval:')


def if_linux(ipin, interin):
    interin = int(interin)
    y = []
    x = []
    parameter = '-c'
    while condition:
        ping = os.popen(f'ping {ipin} {parameter} 1')
        result = ping.readlines()
        if result == []:
            b = int(0)
            print('error')
        else:
            msLine = result[-1].strip()
            a = msLine.split(' = ')[-1]
            b = a.split('ms')[0]
            b = b.split('/')[0]
            b = float(b)
        now = datetime.now()
        y.insert(0, b)
        x.insert(0, now.strftime('%H:%M:%S'))
        #print(x)
        #print(y)
        plt.title(f'Ping Monitor to {ipin}')
        plt.xlabel('Time')
        plt.ylabel('ms')
        plt.scatter(x, y, c='green')
        plt.pause(interin)


def if_windows(ipin, interin):
    interin = int(interin)
    y = []
    x = []
    parameter = '-n'
    while condition:
        ping = os.popen(f'ping {ipin} {parameter} 1')
        result = ping.readlines()
        msLine = result[-1].strip()
        a = msLine.split(' = ')[-1]
        b = a.split('ms')[0]
        if b == '1 (100% loss),':
            b = 0
        if b == '0 (0% loss),':
            b = 0
        b = float(b)
        now = datetime.now()
        y.insert(1, b)
        x.insert(1, now.strftime('%H:%M:%S'))
        #print(x)
        #print(y)
        plt.xlabel('Time')
        plt.ylabel('ms')
        plt.title('Ping Monitor')
        plt.scatter(x, y, c='green')
        plt.pause(interin)


if sys.platform == 'linux':
    if_linux(ip, inter)
if sys.platform == 'windows' or 'win32':
    if_windows(ip, inter)

#close app
plt.ioff()
######
plt.show()
