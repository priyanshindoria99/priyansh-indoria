                          ############## Indian Restaurent Menu ###############
class chole:
    def __init__(self):
        self.chole1="Masala chole"
        self.chole2="Chole with onion"
        self.chole3="Chana pindi"
    
class bhature:
    def __init__(self):
        self.bhature1="Paneer bhatura"
        self.bhature2="Methi bhatura"
        self.bhature3="Aloo bhatura"
    
class menu1(chole,bhature):
    def __init__(self):
        chole.__init__(self)
        bhature.__init__(self)
        print("•"+self.chole1 +"--"+  self.bhature1)
        print("•"+self.chole2 +"--"+  self.bhature2)
        print("•"+self.chole3 +"--"+  self.bhature3)

class pav:
    def __init__(self):
        self.pav1="Masala pav"
        self.pav2="Grilled pav"
        self.pav3="butter pav"
class bhaji: 
    def __init__(self):
        self.bhaji1="Onion bhaji"
        self.bhaji2="Jain bhaji"
        self.bhaji3="Patato bhaji"

class menu2(pav,bhaji):
    def __init__(self):
        pav. __init__(self)
        bhaji. __init__(self)
        print("•"+self.pav1 +"--"+  self.bhaji1+": 140")
        print("•"+self.pav2 +"--"+  self.bhaji2+": 160")
        print("•"+self.pav3 +"--"+  self.bhaji3+": 160")
        
class momos: 
    def __init__(self):
        self.momos1="Tandoori momos"
        self.momos2="Vegetarian momos"
        self.momos3="Cheese momos"
        self.momos4="Afghani malai momos"
        self.momos5="Kothe momos"
 
class menu3(momos):
    def __init__(self):   
        momos. __init__(self)
        print("•"+self.momos1+": 60")
        print("•"+self.momos2+": 60")
        print("•"+self.momos3+": 70")
        print("•"+self.momos4+": 90")
        print("•"+self.momos5+": 100")
        
class sandwich:
    def __init__(self):
        self.sandwich1="Veg sandwich"
        self.sandwich2="Grilled sandwich"
        self.sandwich3="Paneer grilled tikka sandwich"
        self.sandwich4="Italian grilled sandwich sandwich"
        self.sandwich5="Veg grilled sandwich"
        self.sandwich6="Tadka bite special sandwich"
        
class menu4(sandwich):
    def __init__(self):
        sandwich.__init__(self)
        print("•"+self.sandwich1+": 40")
        print("•"+self.sandwich2+": 50")
        print("•"+self.sandwich3+": 90")
        print("•"+self.sandwich4+": 100")
        print("•"+self.sandwich5+": 100")
        print("•"+self.sandwich6+": 120")
        
class paratha:
    def __init__(self):
        self.paratha1="Plain paratha"
        self.paratha2="Aloo paratha"
        self.paratha3="Aloo-Pyaaz paratha"
        self.paratha4="Onion paratha"
        self.paratha5="Mix veg paratha"

class menu5(paratha):
    def __init__(self):
        paratha.__init__(self)
        print("•"+self.paratha1+": 20")
        print("•"+self.paratha2+": 30")
        print("•"+self.paratha3+": 35")
        print("•"+self.paratha4+": 35")
        print("•"+self.paratha5+": 40")

class pizza:
    def __init__(self):
        self.pizza1="Capsicus-Onion pizza"
        self.pizza2="4 Topping pizza"
        self.pizza3="Mushroom roit pizza"
        self.pizza4="OTC pizza"
        self.pizza5="Paneer Tikka pizza"
        self.pizza6="Margarita pizza"
        self.pizza7="Jain special pizza"
        self.pizza8="Masala Garlic pizza"
        
class menu6(pizza):
    def __init__(self):
        pizza.__init__(self)
        print("•"+self.pizza1+": 150")
        print("•"+self.pizza2+": 190")        
        print("•"+self.pizza3+": 210")
        print("•"+self.pizza4+": 240")
        print("•"+self.pizza5+": 240")
        print("•"+self.pizza6+": 250")
        print("•"+self.pizza7+": 260")
        print("•"+self.pizza8+": 300")
        
print("Press 1 for Chole-Bhature")
print("Press 2 for Pav-Bhaji")
print("Press 3 for Momos")
print("Press 4 for Sandwich")
print("Press 5 for Paratha")
print("Press 6 for Pizza")
x=int(input("Enter:\n"))
if(x==1):
    menu_1=menu1() 
elif(x==2):
    menu_2=menu2()
elif(x==3):
    menu_3=menu3()
elif(x==4):
    menu_4=menu4()
elif(x==5):
    menu_5=menu5()   
elif(x==6):
    menu_6=menu6()