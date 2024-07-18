class bikeshop:
    def __init__(self,stock):
        self.stock=stock
        
    def displayBike(self):
        print("total available bikes-->",self.stock)
        
    def rentBike(self,q):
        
        if q<=0:
            print("Enter valid value (greater that zero) ")
        elif q>self.stock:
            print("Not enough bike are available")
        else:
            print("total price ",q*100)
            self.stock=self.stock-q
            print("total left",self.stock)
            
obj=bikeshop(100)            
while True:
    
    uc = int(input('''
         1.display stock 
         2.rent a bike
         3.exit         
                   '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter number of bikes"))
        obj.rentBike(n)
    else:
        break