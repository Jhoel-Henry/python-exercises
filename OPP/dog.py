class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    

  def add_one(self, x):
    return x+1
  
  def bark (self):
    print("bark")

  #getters
  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  
  #setters
  def set_name(self, name):
    self.name= name

  def set_age(self, age):
    self.age = age

d= Dog("Tim", 14)
print(d.name)
d2= Dog("Bill",3)
print(d2.name)