print("*** Mängud numbritega ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True: #добавила True
    try:
        a = (abs(int(input("Sisesta täisarv => ")))) #добавила 2 скобки
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #убрала одно равно
    paaris = 0 #убрала одно равно
    paaritu = 0 #убрала одно равно
    while b > 0: #поменяла знак ; на :
            if b % 2 == 0:
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b = b // 10
    
    print("Numbrite arv:",paaris) #добавила запятую
    print("Paaritu arv:",paaritu) #добавила запятую
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake ümber* sisestatud arv")
    print()
    b=0
    while a > 0: #добавила :
        number = a % 10
        a = a // 10
        b = b * 10+ number
    print("*Ümberpööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") #убрала (
    print()
    if c % 2 == 0:
        print("c - paarisarv. Jagame 2.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0:
                    c == c / 2
            else:
                    c == (3*c + 1) / 2
            print(c, end=" ") #добавила  "
    print()
    print("Hüpotees on õige")