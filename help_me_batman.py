from time import sleep
import os,sys
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.03)#speed of print
def big_space():#almost centers from top......theres probably an easier way of doing this lol or a built in function
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
def bat_symbol():
    print('                             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')#for some reson the .center() left 1 line gaps in bat signal
    print('                             ░░░░░░░▄▄▄░░░█▄▄▄█░░░▄▄▄░░░░░░░░')
    print('                             ░░░░░▄███░░░░█████░░░░███▄░░░░░░')
    print('                             ░░░▄█████▄░░▄█████▄░░▄█████▄░░░░')
    print('                             ░░███████████████████████████░░░')
    print('                             ░░███████████████████████████░░░')
    print('                             ░░▀█████████████████████████▀░░░')
    print('                             ░░░░▀███████▀█████▀███████▀░░░░░')
    print('                             ░░░░░░▀███▀░░░███░░░▀███▀░░░░░░░')
    print('                             ░░░░░░░░░▀░░░░░▀░░░░░▀░░░░░░░░░░')
    print('                             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
def wave_hand1():
    big_space()
    print('                                               _.-._         ')
    print('                                              | | | |_       ')
    print('                                              | | | | |      ')
    print('                                              | | | | |      ')
    print("                                            _ |  '-._ |      ")
    print("                                            \`\`-.'-._;      ")
    print("                                             \    '   |      ")
    print('                                              \  .`  /       ')
    print('                                               |    |        ')
    sleep(0.5)
    clear_screen()
    big_space()
    print("                                               ____          ")
    print("                                            .'` __/_______   ")
    print("                                       ---'  -'`    ______)  ")
    print("                                                    _______) ")
    print("                                                   _______)  ")
    print("                                       -----..___________)   ")
    sleep(0.5)
    clear_screen()

while True:
    clear_screen()
    bat_symbol()
    print_slow("DO YOU NEED BATMANS HELP?..".center(90))
    print()
    print_slow('Enter How many Bad guys there are?'.center(90))
    print()
    print_slow('Then press Enter: '.center(50))
    crims = input('')
   # print(type(crims))
    try:
        crims = int(crims)
        print()
        print()
        #print('try works and mades int',type(crims))##
        if crims == 1:
            clear_screen()
            big_space()
            print_slow('You got this you can take 1 bad guy on your own!!!'.center(90))
            sleep(5)
        elif crims <= 5:
            clear_screen()
            big_space()
            print_slow('You got this, you can take them on your own!!!'.center(90))
            sleep(5)
        elif crims > 5 and crims <= 10:
            clear_screen()
            big_space()
            print_slow('Thats to many for one boy...'.center(90))
            print_slow('Batman will come with you!!!'.center(90))
            sleep(5)
        elif crims > 10:
            clear_screen()
            big_space()
            print_slow('You stay safe thats to many...'.center(90))
            print_slow('Batman will go alone!!!'.center(90))
            sleep(5)
        clear_screen()
        big_space()
        print_slow("PLAY AGAIN OR TYPE 'done' on the next screen".center(50))
        sleep(5)
    except:
        if crims == 'done':
            clear_screen()
            wave_hand1()
            wave_hand1()
            wave_hand1()
            wave_hand1()
            big_space()
            print_slow('Goodbye...hope you had fun!!'.center(90))#new line test
            break
        else:
            clear_screen()
            big_space()
            print_slow('You have to enter a number!...'.center(90))
            print()
            print_slow('Or if your done....'.center(90))
            print()
            print_slow('just type done and press enter on the start screen'.center(90))
            sleep(2)
            continue
