from Mot import Mot

en = ["car","rabbit","find"]
fr = ["voiture","lapin","bien"]

m : list[Mot] = []

# i = Mot("bonjour","hello",False)
# i = Mot(en[0],fr[0],False)

####
for i in range(len(en)):
    mot = Mot(en[0+i],fr[0+i],False)
    m.append(mot)

# m = list(en)
# m ==> [i,j,k]

#range(3) ==> [0 1 2]

#en 

