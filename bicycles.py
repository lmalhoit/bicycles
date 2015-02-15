#This project emulates the creation and sales cycles of bikes

#Create classes for our model

#bicycle, bicycle shops, and customers classes

    
class bike():
  def __init__(self, wheels, frames, manufacturers):
    self.model = {"a" : 100, "b" : 200, "c" : 400, "d" : 500, "e" : 600, "f" : 700}
    self.wheel = wheels.model
    self.wheelqty = 2
    self.weight = wheels.weight + frames.weight
    self.cost = wheels.cost + frames.cost
    self.manufacturer = manufacturers.name
    
class wheels():
  def __init__(self):
    self.model = ["street", "mountain", "hybrid"]
    self.weight = 5
    self.cost = 10   

    
class frames():
  def __init__(self):
    self.model = ["aluminum", "carbon", "steel"]
    self.weight =  20
    self.cost = 30
    
class shop():
  def __init__(self, name, inventory, bike):
    self.name = name
    self.inventory = inventory
    self.bikes = bike.model
  
  def listBikes(self):
    return self.bikes
    
class customer():
  def __init__(self, name, wallet):
    self.name = name
    self.wallet = wallet
 
class manufacturers():
  def __init__(self):
    self.name = ["Huffy", "Raleigh"]
    self.margin = 1.2
    self.models = {"Huffy" : "a", "Huffy" : "b", "Huffy" : "c", "Raleigh" : "a", "Raleigh" : "b", "Raleigh" : "c"}
