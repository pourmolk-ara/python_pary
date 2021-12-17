# y = A * sin(2*pi*f*t)
#radian * 180/pi = degree


from math import exp, pi, sin
from sys import stdin
from modules import *


config_main = list()

for line in stdin:
    config_main.append(line)

"""
======= VERIFICATION CONFIG FILE, ASSIGNING VARIABLES =======
"""
try:
    res = verification(config_main, 'frequency', 'time', 'amplitude')
    FREQUENCY,TIME,AMPLITUDE = res 
    print(FREQUENCY,TIME,AMPLITUDE)
except ValueError:
    print('There are some errors in config File. Not enough values to unpack (expected 3, got {})'.format(len(res)))

# not enough values to unpack (expected 3, got 0)











#from math import pi, sin
#from sys import stdin
#Tuple=("FREQUENCY","TIME","AMPLITUDE")
#n=['frequency','time','amplitude']
#config_main = list()

#for line in stdin:
   # config_main.append(line)

#def sin(*config_main):


    #for i in range(0,3):
    #for i in config_main:    
        #if config_main[i].split('=')[0].strip().lower() == n[i]:
         #   Tuple[i]= int(config_main[i].split('=')[1].strip())
        #else:
          #  return('Expected: config_main. Recieved : {}'.format(config_main[i].split('=')[0].strip())) 
            #print ('Expected:sin(*config_main). Recieved : {}'.format(config_main[i].split('=')[0].strip())) 
    #try:
      #  return(Tuple,config_main)
    #except Exception as e:
      #  print(e)
#print(Tuple,"\n\n",sin(*config_main))

