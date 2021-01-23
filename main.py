import psutil, time
import matplotlib.pyplot as plt

print("""HardStat v1.0.0

    Copyright (C) 2021 eyx

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.""")
print("\n")
print("Close the Python shell window to exit.")
print("\n")
print("1. Track CPU Usage")
print("2. Track RAM Usage")
option = input("Enter an option: ")

if option == "1":

    print("Preparing start data...")

    cpu_ = []

    for i in range(10):
        cpu_.append(psutil.cpu_percent())

    plt.figure(num="HardStat v1.0.0")

    while True:
        cpu = psutil.cpu_percent()
        print(str(cpu)+"% CPU Usage")
        del cpu_[0]
        cpu_.append(cpu)
        plt.plot(cpu_)
        plt.draw()
        plt.pause(1)
        plt.clf()

if option == "2":

    print("Preparing start data...")

    ram_ = []

    for i in range(10):
        ram_.append(psutil.virtual_memory().percent)

    plt.figure(num="HardStat v1.0.0")

    while True:
        ram = psutil.virtual_memory().percent
        print(str(ram)+"% RAM Usage")
        del ram_[0]
        ram_.append(ram)
        plt.plot(ram_)
        plt.draw()
        plt.pause(1)
        plt.clf()
