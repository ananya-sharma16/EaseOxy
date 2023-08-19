class customer:
  
  def __init__(self, name, cylinders = None, shopName = None, rentalBasis = None, rentalTime = None, bill = None):

    self.name = name
    self.shopName = shopName
    self.cylinders = cylinders        # no. of cylinders with customer
    self.rentalBasis = rentalBasis    # weekly, daily or hourly
    self.rentalTime = rentalTime      # time of rent as datetime object
    self.bill = bill                  # bill to pay/previously paid



  def displayDetails(self):
    return self.shopName, self.cylinders, self.rentalBasis, self.rentalTime


  def requestCylinder(self, n):
    # pass no. of cylinders required by the customer
    # update object variable 'cylinders' accordingly
           
    c = n

    try:
      c = int(c)
    except ValueError:
      print("That's not a positive integer!")
      return -1

    if c < 1:
        print("Invalid input. Number of cylinders should be greater than zero!")
        return -1
    else:
      self.cylinders = c
      return self.cylinders



     
  def returnCylinder(self):
    # return customer object variables to calculate bill from, if present
        
    if self.rentalBasis and self.rentalTime and self.cylinders:
      return self.rentalTime, self.rentalBasis, self.cylinders  
    else:
      return 0,0,0