"""
dict = {'Name': 'Bodi', 'Age': 14, 'Class': 'First'}
dict["Google"] = "Larry Page en Sergey Brin"
print ("['Name']: ", dict['Name'])
print ("['Age']: ", dict['Age'])
print ("['Google]: ", dict['Google'])
if "Google" in dict:
    print("Google zit erin!")
del dict["Age"]
if "Age" not in dict:
    print("TurboBUILD IS BACKKKCKCKCKKCKCKC!")
"""
   

"""

dic1={'1':'10', '2':'20'}
dic2={'3':'30', '4':'40'}
dic3={'5':'50', '6':'60'}
def Merge(dic1, dic2):
    return(dic2.update(dic1))
def Merge2(dic2, dic3):
    return(dic2.update(dic3))
print(Merge(dic1, dic2))
print(Merge2(dic2, dic3))
print(dic2)

"""

"""

def groet():
    for i in range(10):
        print("hallo")
        
groet()


def tafel5():
    print("5, 10, 15, 20, 25, 30, 35, 40, 45, 50")
    
tafel5()
 
 

def groet(naam):
    print("Hallo "+ naam)
    
groet("Bodi")
groet("Joël")
groet("poep")
 
"""

"""

def slik(w):
    t = 0
    for i in range(len(w)):
        #print (i)
        l = ("")
        for i in range(t + 1):
            l += (w[t])
        t += 1
        print (l)
slik("hallo")
    
 """

""" 
def grootste_():
    getallen = [3, 7, 18, 5, 4, 20]
    grootste = int(0)
    rane = len(getallen)
    teller = 0
    for i in range(rane):
        getal = getallen[teller]
        if getal > grootste:
            grootste = int(getal)
        teller += 1
    print(grootste)
grootste_()
"""

"""
def reverse_string(woord):
    nieuw_woord = woord[::-1]
    print(nieuw_woord)
reverse_string("teer")
"""

"""
num = 1

if num > 1:    
   for i in range(2, num//2):
       if (num % i) == 0:
           print(num, "is geen priemgetal")
           break
       else:
            print(num, "is een priemgetal")
            break
else: 
   print(num, "is geen priemgetal") 
"""

"""
def reverse_string(woord):
    nieuw_woord = woord[::-1]
    if nieuw_woord == woord:
        print("true")
    else:
        print("false")
reverse_string("teet")
"""
"""
lijstje = ["we", "er", "rt", "ty", "yu", "ui", "io", "op"]
print(lijstje[::-1])

"""



























boodschappen = {"brood": 2, "water": 1, "sap": 3, "pindakaas": 1, "pepernoten": 2}
boodschappenlijstje = {""}


def pp_toevoegen():
    boodschappen[keuze1] = keuze2

def pp_veranderen():
    boodschappen[verwijderen_product] = veranderen
    
def lijste_toevoegen():
    boodschappen

keuze3 = input("Hallo wat is je naam?")
print("Hallo" + keuze3)
keuze2 = ""


while keuze3 != "stop" and keuze2 != "stop":
    print(" U kunt deze dingen kopen")
    print(boodschappen)
    keuze1 = input(" Wat wilt u aan de boodschappen toevoegen? ")
    keuze2 = input(" Wat is de prijs van het product? " )
    pp_toevoegen()
    aanpassen = input(" Wilt u de prijs van een product aanpassen?")
    if aanpassen == "ja":
        verwijderen_product = input("welk product?")
        if verwijderen_product in boodschappen:
            del boodschappen[verwijderen_product]
            veranderen = input("Welke prijs moet het worden? ")
            pp_veranderen()
            print(boodschappen)
            verwijderen = input("Wilt u een product van de lijst weghalen?")
            if verwijderen == "ja":
                delete_product = input("Welk product wilt u verwijderen?")
            if delete_product in boodschappen:
                del boodschappen[delete_product]
            print(boodschappen)
            lijst_toevoegen = input("Nu kunt u boodschappen gaan doen! Wat wilt u in uw winkelwagen van het lijstje?")
            if lijst_toevoegen in boodschappen:
                pass
                
        
                
            
                        
            
            
            
            
            
                            