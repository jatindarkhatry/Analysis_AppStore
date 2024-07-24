import csv


#calculate the average of column user_rating_ver but where price is equal to zero and prime genre is game or music

open_file = open("AppleStore.csv" , encoding="utf-8")
read_file = csv.reader(open_file)
applestore = list(read_file)

print(applestore[0].index("user_rating_ver"))
print(applestore[0].index("price"))
print(applestore[0].index("prime_genre"))

avergae = 0

ver= []
for i in applestore[1:]:
    rating = float(i[8])
    price = float(i[4])
    genre = i[11]
    if price == 0 and (genre == "Games" or genre== "Music"):
        print(rating,price,genre)
        ver.append(rating)
        avergae = sum(ver)/len(ver)
print(avergae)




