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

    list_sc001 = []
    list_sc101 = []

    while c != "-1":
        s = input("Score: ")

        if c.lower() == "sc001":
            list_sc001.append(int(s))
        elif c.lower() == "sc101":
            list_sc101.append(int(s))
        else:
            pass

        c = input("Which class? ")

    if not list_sc001 and not list_sc101:
        print("No class scores were entered")
    else:
        if list_sc001:
            print("=============SC001=============")
            print("Max (001): %s" % max(list_sc001))
            print("Min (001): %s" % min(list_sc001))
            print("Avg (001): %s" % round(sum(list_sc001)/len(list_sc001),2))
        else:
            print("=============SC001=============")
            print("No score for SC001")

        if list_sc101:
            print("=============SC001=============")
            print("Max (101): %s" % max(list_sc101))
            print("Min (101): %s" % min(list_sc101))
            print("Avg (101): %s" % round(sum(list_sc101)/len(list_sc101),2))
        else:
            print("=============SC001=============")
            print("No score for SC101")




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
