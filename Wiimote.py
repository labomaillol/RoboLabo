from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

dev = InputDevice('/dev/input/event2')
code=[304,305,103,108,105,106,407,412,316,257,258]
ref=['Touche A','Touche B','Touche Haut','Touche Bas','Touche Gauche','Touche Droite','Touche +','Touche -','Touche Home','Touche 1','Touche 2']

print(dev)

liste2=[]

liste=[]

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        liste=dev.active_keys()
        for k in liste2:
            if k not in liste :
                print('On relache '+str(ref[code.index(k)]))
                print(' ')
                if k==code[0]:
                    print(ref[code.index(k)])
                if k==code[1]:
                    print(ref[code.index(k)])
                if k==code[2]:
                    print(ref[code.index(k)])
                if k==code[3]:
                    print(ref[code.index(k)])
                if k==code[4]:
                    print(ref[code.index(k)])
                if k==code[5]:
                    print(ref[code.index(k)])
                if k==code[6]:
                    print(ref[code.index(k)])
                if k==code[7]:
                    print(ref[code.index(k)])
                if k==code[8]:
                    print(ref[code.index(k)])
                if k==code[9]:
                    print(ref[code.index(k)])
                if k==code[10]:
                    print(ref[code.index(k)])
        for i in liste:
            print('On appuie sur '+str(ref[code.index(i)]))
            print(' ')
            if i==code[0]:
                print(ref[code.index(i)])
            if i==code[1]:
                print(ref[code.index(i)])
            if i==code[2]:
                print(ref[code.index(i)])
            if i==code[3]:
                print(ref[code.index(i)])
            if i==code[4]:
                print(ref[code.index(i)])
            if i==code[5]:
                print(ref[code.index(i)]) 
            if i==code[6]:
                print(ref[code.index(i)])
            if i==code[7]:
                print(ref[code.index(i)])
            if i==code[8]:
                print(ref[code.index(i)])
            if i==code[9]:
                print(ref[code.index(i)])
            if i==code[10]:
                print(ref[code.index(i)])
        liste2=liste
