# 5K00BF49-Automaatiotekniikka
# Harjoitustyö 2
# Tehtävä 1
# Test program
# Getkeys made by Box-Of-Hats
# made by mvaario


import time
from getkeys import key_check


def start():
    if 'F' in key_check():
        print("Process started")
        main.stop = False
        main.running = True
        main.m1 = True
        main.print()
        main.change()
    return


class movement:

    def reset():
        print("Reset")
        print("")

        main.c1 = -1
        main.pause()
        main.c2 = -1
        main.pause()
        main.servo = 1
        main.pause()

        return

    def grab():
        print("Grab")
        print("")

        main.c2 = 1
        main.pause()
        main.c1 = 1
        main.pause()
        main.c2 = -1
        main.pause()
        main.c1 = -1
        main.pause()

        return

    def take():
        print("Take")
        print("")

        main.servo = 2
        main.pause()

        return

    def take_back():
        print("Take Back")
        print("")

        main.servo = 1
        main.pause()
        return

    def drop():
        print("Drop")
        print("")

        main.c1 = +1
        main.pause()
        main.c2 = +1
        main.pause()
        main.c1 = -1
        main.pause()
        return


class main:

    def __init__(self):
        self.running = False
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False
        self.i = 0
        self.time = 1

        self.stop = False

        # Motor M1
        self.m1 = False

        # Transmission
        self.servo = 0
        self.c1 = 0
        self.c2 = 0

        # old
        self.sensor1_old = False
        self.sensor2_old = False
        self.sensor3_old = False
        self.m1_old = False
        self.servo_old = 0
        self.c1_old = 0
        self.c2_old = 0

    def sensor(self):
        main.sensor3 = False
        main.i += 1
        if 3 < main.i < 5:
            main.sensor1 = True
            main.stop = True
        else:
            main.sensor1 = False

        if main.i > 7:
            main.stop = True
            main.sensor2 = True
            main.m1 = False
        main.pause()

        return

    def sensor3_check(self):
        print("Bringing the object")
        print("")

        main.m1 = True
        main.pause()
        while main.m1:
            main.i += 1
            main.pause()
            if main.i > 10:
                main.sensor3 = True
                main.pause()
                main.m1 = False
                main.pause()
                main.running = False
                main.pause()

    def pause(self):
        time.sleep(float(main.time))
        main.print()
        main.change()

    def change(self):
        # Motor and sensor
        main.sensor1_old = main.sensor1
        main.sensor2_old = main.sensor2
        main.sensor3_old = main.sensor3
        main.m1_old = main.m1

        # Transmission
        main.servo_old = main.servo
        main.c1_old = main.c1
        main.c2_old = main.c2

        return

    def print(self):
        if main.sensor1 != main.sensor1_old:
            print("Sensor 1 ", main.sensor1)
        if main.sensor2 != main.sensor2_old:
            print("Sensor 2", main.sensor2)
        if main.sensor3 != main.sensor3_old:
            print("Sensor 3 ", main.sensor3)
        if main.m1 != main.m1_old:
            print("Motor is ", main.m1)

        if main.servo != main.servo_old:
            print("Linear servo position", main.servo)

        if main.c1 != main.c1_old:
            if main.c1 < 0:
                print("Transmission C1 is up")
            else:
                print("Transmission C1 is down")

        if main.c2 != main.c2_old:
            if main.c2 < 0:
                print("Gripper C2 close")
            else:
                print("Gripper C2 open")

        return


if __name__ == '__main__':
    main = main()
    check_key = key_check()

    print("")
    print("Press F to start process ")
    while True:
        start()
        if main.stop is not True:
            if 'Q' in key_check():
                main.running = False
                main.m1 = False
                print("Process stopped")
                break

        if main.running:
            main.sensor()
            if main.sensor2 == True:
                movement.reset()
                movement.grab()
                movement.take()
                movement.drop()
                movement.grab()
                movement.take_back()
                movement.drop()
                main.sensor3_check()

                print("")
                print("Process finished")
                print("Press F to start new process ")
                main.running = False
