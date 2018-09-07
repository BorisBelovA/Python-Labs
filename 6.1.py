import os
import subprocess

#os.startfile('1.1.py')
#os.system('1.1.py')
command = float(input("Введите в качестве команды номер лаб/раб: "))
if(command == 1.1):
    subprocess.call('python 1.1.py', shell=True)
elif (command == 1.2):
    subprocess.call('python 1.2.py', shell=True)
elif (command == 5.2):
    subprocess.call('python 5.2.py', shell=True)
elif (command == 7.2):
    subprocess.call('python 7.2.py', shell=True)

