import math

K = -8266.64258429376

def ageETA():
    pct_left = float(input("% of natural c14 in your sample : "))

    age = K * math.log(pct_left/100)

    print("Sample is " + str(age) + " years old.")

if __name__ == '__main__':
    ageETA()