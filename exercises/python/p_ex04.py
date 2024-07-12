#max points [3]
"""
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

#Example

With the input:
name: School Volvo
max_speed: 180
mileage: 12

Expected Output:

Vehicle Name: School Volvo Speed: 180 Mileage: 12
"""

class Vehicle:
  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

# code goes here
class Bus 

if __name__ == "__main__":
  # keep this function call here 
  School_bus = Bus("School Volvo", 180, 12)
  print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
