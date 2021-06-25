"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    c = input("Which class? ")

    sc001_max = 0
    sc001_min = 10
    sc001_count = 0
    sc001_sum = 0

    sc101_max = 0
    sc101_min = 10
    sc101_count = 0
    sc101_sum = 0

    while c != "-1":
        s = int(input("Score: "))

        if c.lower() == "sc001":
            sc001_count+=1

            if s >= sc001_max:
                sc001_max = s

            if s <= sc001_min:
                sc001_min = s

            sc001_sum = sc001_sum + s

        elif c.lower() == "sc101":
            sc101_count+=1

            if s >= sc101_max:
                sc101_max = s

            if s <= sc101_min:
                sc101_min = s

            sc101_sum = sc101_sum + s

        else:
            pass

        c = input("Which class? ")

    if sc001_count == 0 and sc101_count == 0:
        print("No class scores were entered")
    else:
        if sc001_count > 0:
            print("=============SC001=============")
            print("Max (001): %s" % sc001_max)
            print("Min (001): %s" % sc001_min)
            print("Avg (001): %s" % float(sc001_sum/sc001_count))
        else:
            print("=============SC001=============")
            print("No score for SC001")

        if sc101_count > 0:
            print("=============SC001=============")
            print("Max (101): %s" % sc101_max)
            print("Min (101): %s" % sc101_min)
            print("Avg (101): %s" % float(sc101_sum/sc101_count))
        else:
            print("=============SC001=============")
            print("No score for SC101")




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
