class MyClass:
  x = 5
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Gmc", "Acadia")

print(car1.brand)
print(car1.model)

class my_function:
  def __init__(self, param):
    self.param = param

  def execute(self):
    print(f"Processing: {self.param}")

my_function("driving").execute()
