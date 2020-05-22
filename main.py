# 5K00BF49-Automaatiotekniikka
# Harjoitustyö 1
# Tehtävä 2
# Test program
# Getkeys made by Box-Of-Hats
# made by mvaario

import time
from getkeys import key_check

class main:

    def __init__(self):

        self.H1 = False
        self.S1 = False
        self.S2 = False
        self.S3 = False

        self.H1_old = False
        self.S1_old = False
        self.S2_old = False
        self.S3_old = False

    def key(self):
        if 'H' in key_check():
            if not main.H1:
                main.H1 = True
            else:
                main.H1 = False
            time.sleep(0.5)

        if '1' in key_check():
            if not main.S1:
                main.S1 = True
            else:
                main.S1 = False
            time.sleep(0.5)

        if '2' in key_check():
            if not main.S2:
                main.S2 = True
            else:
                main.S2 = False
            time.sleep(0.5)

        if '3' in key_check():
            if not main.S3:
                main.S3 = True
            else:
                main.S3 = False
            time.sleep(0.5)

        if 'F' in key_check():
            main.print_start()
            time.sleep(0.5)

        return

    def calculation(self):
        if main.S1 and main.S2:
            main.H1 = True
        if main.S3 == True and main.S2 == False:
            main.H1 = False
        if main.S1 == False:
            main.H1 = False

    def print(self):
        if main.S1 != main.S1_old:
            print("Kytkin S1", main.S1)
        if main.S2 != main.S2_old:
            print("Kytkin S2", main.S2)
        if main.S3 != main.S3_old:
            print("Kytkin S3", main.S3)
        if main.H1 != main.H1_old:
            print("Lampput", main.H1)
            print("")

        return

    def change(self):
        main.H1_old = main.H1
        main.S1_old = main.S1
        main.S2_old = main.S2
        main.S3_old = main.S3

    def print_start(self):
        print("")
        print("Kytkin S1", main.S1)
        print("Kytkin S2", main.S2)
        print("Kytkin S3", main.S3)
        print("Lamppu", main.H1)
        print("")
        return


if __name__ == '__main__':
    main = main()
    check_key = key_check()
    main.print_start()

    while True:
        main.key()
        main.calculation()
        main.print()
        main.change()
