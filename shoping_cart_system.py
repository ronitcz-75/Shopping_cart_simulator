#********WELCOME TO THE SHOPPING**********
#This is shoping cart to add items and billing

import time as t 
import random as r

customer=input("*****Welvome to our store*****\n Avialable:i)seeds and dairy section: ")

#Seeds and dairy product section 

seeds_section=[" chia seeds "," pumpkin seeds "," flax seeds "," sunflower seeds "," fennal seeds "]
dairy_section=[" milk "," curd "," greek yougrt "," butter "," cheese "]

#Seed and dairy section confirmation
while True:
    if customer=="seeds":
        print(seeds_section)
    if customer=="dairy":
        print(dairy_section)
    break

# product choosing section

quan=input(" Enter the which you want :  ").lower()
# if you want more than 1 product enter comma and name to order

if quan=="chia seeds":
    print("chia seed is added to cart!!\nTime:-",t.ctime())
if quan=="pumpkin seeds":
    print("pumpkin seeds added to cart!!\nTime:-",t.ctime())
if quan=="flax seeds":
    print("flax seeds added to cart!!!\nTime:-",t.ctime())
if quan=="sunflower seeds":
    print("sunflower seeds added to cart!!!\nTime:-",t.ctime())
if quan=="fennal seeds":
    print("fennal seeds added to cart!!\nTime:-",t.ctime())
if quan=="chia and pumpkin":
    print("chia and pumpkin is added to cart!!!\nTime:-",t.ctime())
if quan=="chia and sunflower":
    print("chia anf sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="chia and flax":
    print("chia and flex is added to cart!!!\nTime:-",t.ctime())
if quan=="chia and fennal":
    print("chia and fennal is added to cart!!\nTime:-",t.ctime())
if quan=="pumpkin and flax":
    print("pumpkin and flax is added to cart!!!\nTime:-",t.ctime())
if quan=="pumpkin and sunflower":
    print("pumpkin and sunflower is added in cart!!\nTime:-",t.ctime())
if quan=="pumpkin and fennal":
    print("pumpkin and fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="flax and sunflower":
    print("flax and sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="flax and fennal":
    print("flax and fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="sunflower and fennal":
    print("sunflower and fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,pumpkin,flax":
    print("chia,pumpkin,flax is added to cart!!\nTime:-",t.ctime()) #this area enter comma in quan input to get the item
if quan=="chia,pumpkin,sunflower":
    print("chia,pumpkin,sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,flax,fennal":
    print("chia,flax,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,flax,sunflower":
    print("chia,flax,sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,flax,fennal":
    print("chia,flax,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,sunflower,fennal":
    print("chia,sunflower,fennal is added to cart\nTime:-",t.ctime())
if quan=="pumpkin,flax,sunflower":
    print("pumpkin,flax,sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="pumpkin,flax,fennal":
    print("pumpkin,flax,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="pumpkin,sunflower,fennal":
    print("pumpkin,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="flax,sunflower,fennal":
    print("flax,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,pumpkin,flax,sunflower":
    print("chia,pumpkin,flax,sunflower is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,pumpkin,flax,fennal":
    print("chia,pumpkin,flax,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,pumpkin,sunflower,fennal":
    print("chia,pumpkin,sunflower,fennal is added to cart!!\nTime:-",t.ctime())
if quan=="chia,flax,sunflower,fennal":
    print("chia,flax,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="pumpkin,flax,sunflower,fennal":
    print("pumpkin,flax,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="pumpkin,flax,sunflower,fennal":
    print("pumpkin,flax,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())
if quan=="chia,pumpkin,flax,sunflower,fennal":
    print("chia,pumpkin,flax,sunflower,fennal is added to cart!!!\nTime:-",t.ctime())

#dariy product 
if quan=="milk":
    print("milk is added to cart!!!\nTime:-",t.ctime())
if quan=="curd":
    print("curd is added to cart!!!\nTime:-",t.ctime())
if quan=="Greek yogurt":
    print("Greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="Butter":
    print("Butter is added to cart!!\nTime:-",t.ctime())
if quan=="Cheese":
    print("Cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk and curd":
    print("milk and curd is added to cart!!!\nTime:-",t.ctime())
if quan=="milk and greek yogurt":
    print("milk and greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="milk and butter":
    print("milk and butter is added to cart!!!\nTime:-",t.ctime())
if quan=="milk and cheese":
    print("milk and cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="curd and greek yogurt":
    print("curd and greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="curd and butter":
    print("curd and butter is added to cart!!!\nTime:-",t.ctime())
if quan=="curd and cheese":
    print("curd and cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="greek yogurt and butter":
    print("greek yogurt and butter is added to cart!!!\nTime:-",t.ctime())
if quan=="greek yogurt and cheese":
    print("greek yogurt and cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="butter and cheese":
    print("butter and cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,greek yogurt":
    print("milk,curd,greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,butter":
    print("milk,curd,butter is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,cheese":
    print("milk,curd,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,greek yogurt,butter":
    print("milk,greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,greek yogurt,cheese":
    print("milk,greek yogurt,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,butter,cheese":
    print("milk,butter,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="curd,greek yogurt,butter":
    print("curd,greek yogurt,butter is added to cart!!!\nTime:-",t.ctime())
if quan=="curd,greek yogurt,cheese":
    print("curd,greek,yogurt,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="curd,butter,cheese":
    print("curd,butter,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="greek yogurt,butter,cheese":
    print("greek yogurt,butter,cheese is added to cart\nTime:-",t.ctime())
if quan=="milk,curd,greek yogurt,butter":
    print("milk,curd,greek yogurt is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,greek yogurt,cheese":
    print("milk,curd,greek yogurt,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,butter,cheese":
    print("milk,curd,butter,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,greek yogurt,butter,cheese":
    print("milk,greek yogurt,butter,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="curd,greek yogurt,butter,cheese":
    print("curd,greek yogurt,butter,cheese is added to cart!!!\nTime:-",t.ctime())
if quan=="milk,curd,greek yogurt,butter,cheese":
    print("milk,curd,greek yogurt,butter and cheese is added to cart!!!\nTime:-",t.ctime())
class store():
    name="store xyz"
    user=input("cutomer name: ")
print("customer name:-",store.user)
print("store name:",store.name)
print("Thank you for using the service!!!!!")