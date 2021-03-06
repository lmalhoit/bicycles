from bicycles import bike, shop, customer, wheels, frames, manufacturers
#Main file which imports classes from bicycles.py
#Create 3 customers with budgets of $200, $500, and $1000
cust1 = customer("Lauren", 200)
cust2 = customer("John", 500)
cust3 = customer("Alyssa", 1000)

#This shows which bikes the customers may purchase according to how much money they have
wheels1 = wheels()
wheels1.model = "street"
frames1 = frames()
mans1 = manufacturers()
mans1.name = "Huffy"
mans2.name = "Raleigh"
bike1 = bike(wheels1, frames1, mans1)


for cust in [cust1, cust2, cust3]:
  modellist = []
  for model,price in bike1.model.iteritems():
    wallet = cust.wallet
    retailprice = price + price * .2
    if retailprice <= wallet:
      modellist.append(model)
  print "Customer {} can buy models {}".format(cust.name, ", ".join(modellist))
  

#This shows initial inventory
bikeshop1 = shop("shop1", 6, bike1)
print "Initial inventory at Bike Shop is : {}".format(bikeshop1.listBikes())

#Customer purchases a bike, show which bike, the cost and how much money they have left
cust1.wallet = cust1.wallet - bike1.model["a"] * 1.2
cust1model = "a"
print "Customer {} purchased model {} and now has {} left in their wallet".format(cust1.name, cust1model, cust1.wallet)

cust2.wallet = cust2.wallet - bike1.model["c"] * 1.2
cust2model = "c"
print "Customer {} purchased model {} and now has {} left in their wallet".format(cust2.name, cust2model, cust2.wallet)

cust3.wallet = cust3.wallet - bike1.model["f"] * 1.2
cust3model = "f"
print "Customer {} purchased model {} and now has {} left in their wallet".format(cust3.name, cust3model, cust3.wallet)

#Bike shops remaining inventory for each bike and how much profit they made for the three sold
totalProfit = (bike1.model[cust1model] * 1.2 + bike1.model[cust2model] * 1.2 + bike1.model[cust3model] * 1.2) - (bike1.model[cust1model] + bike1.model[cust2model] + bike1.model[cust3model])
print "The profit made by the sales of the three bikes is {}".format(totalProfit)
del bike1.model[cust1model]
del bike1.model[cust2model]
del bike1.model[cust3model]
print "The remaining bike shop inventory is {}".format(bike1.model)  

print "They type of wheels on the bike are {} wheels".format(bike1.wheel)

print "The weight of the bike is {} lbs".format(bike1.weight)

print "The cost to produce the bike is {} dollars".format(bike1.cost)

print "The manufacturer of the bike is {}".format(bike1.manufacturer)
