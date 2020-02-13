class client:
    def __init__(self,nom,CIN,ncompt):
        self.nom=nom
        self.CIN=CIN
        self.ncompt=ncompt
def personnalisation(nom,CIN,ncompt):
    print("le nom est %s,le CIN est : %s et le numéro de compt est: %s"%(nom,CIN,ncompt))

c1=client("Ahmed", 5664477, 12345)
c2=client("Ali", 697323, 98765)
print(personnalisation(c1.nom,c1.CIN,c1.ncompt)) 
print(personnalisation(c2.nom,c2.CIN,c2.ncompt)) 