from random import randrange

value = 0

portefeuille = input ("Combien de dollars avez-vous? ")
while portefeuille > 0 :
    
    valueOK = False
    while valueOK == False :
        value = input ("Choisissez la case ou miser : ")
        if value > 0 and value < 50 :
             valueOK = True
    mise = 0
    while mise <= 0 or mise > portefeuille :
        mise = input ("Misez ! : ")

    tirage = randrange(0, 49)

    print "Valeur tiree :", tirage

    if tirage == value :
        portefeuille += (mise * 3)
        print "Quelle chance, vous avez gagne !"
    elif (tirage % 2) == (mise % 2) :
        portefeuille += (mise * 0.5)
        print "Dommage, au moins, la case est de la meme couleur, vous recuperez la moitie de votre mise"
    else:
        portefeuille -= mise
        print "Dommage, vous avez tout perdu"
    
    print "Vos gains :", mise, "$"
    print ("Portefeuille actuel :", portefeuille, "$")
