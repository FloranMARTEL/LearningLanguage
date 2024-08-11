lili = []

lili.append("Floran")
lili.append("bgdu44")
lili.append("Titania")

#print(lili)

print(len(lili)) # ==> 2
print(range(len(lili))) # ==> [0,1]
print("--------------------") 

for i in range(len(lili)):
    print(i)
    print(lili[i])

print("--------------------") 

for v in lili:
    print("lili : "+ v )

print("------------------__________________--------") 

for i in range(len(lili)):
    lili[i] = "Lord "+lili[i]

# lili[0] = "Lord Floran"
# lili[1] = "Lord BGdu44"
# lili[2] = "Lord BGdu44"
print(lili)
print("---------------------------------------") 

n = 2048
i = -1
while n == int(n):
    n = n/2
    i+=1
    print(n)
print(i)


print("---------------------------------------") 

note = [12.5, 18, 2]


for i in range(len(note)):
    for v in range(i+1,len(note)):
        if note[i] > note[v]:
            temp = note[v]
            note[v] = note[i]
            note[i] = temp

print(note)
