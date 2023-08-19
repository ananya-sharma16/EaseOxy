import datetime

class rental:

  def __init__(self, name, t_stock=0, stock = 0):
    self.name = name
    self.stock = stock            # no. of cylinders available to rent
    self.stockTotal = t_stock     # no. of cylinders available + no. of cylinders rented

  def displaystock(self):
    # return name and value of stock as string
    return self.name+' (Stock = '+str(self.stock)+')'

  def rentHourlyBasis(self, n):
    # rent out 'n' cylinders from availble stock of the rental object
    # return time of rent as datetime object
       
    if n <= 0:
      print("Number of cylinders should be positive!")
      return None
        
    elif n > self.stock:
      print("Sorry! We have currently {} cylinders available to rent.".format(self.stock))
      return None
        
    else:
      now = datetime.datetime.now()                      
      '''print("You have rented a {} cylinder(s) on hourly basis today at {} hours.".format(n, now.hour))
      print("You will be charged Rs 400 for each hour per cylinder.")
      print("We hope you found our services to be beneficial.")'''

      self.stock -= n
      return now

  def rentDailyBasis(self, n):
        
    if n <= 0:
      print("Number of cylinders should be positive!")
      return None

    elif n > self.stock:
      print("Sorry! We have currently {} cylinders available to rent.".format(self.stock))
      return None
    
    else:
      now = datetime.datetime.now()                      
      '''print("You have rented {} cylinder(s) on daily basis today at {} hours.".format(n, now.hour))
      print("You will be charged Rs 1500 for each day per cylinder.")
      print("We hope you found our services to be beneficial.")'''

      self.stock -= n
      return now

  def rentWeeklyBasis(self, n):
       
    if n <= 0:
      print("Number of cylinders should be positive!")
      return None

    elif n > self.stock:
      print("Sorry! We have currently {} cylinders available to rent.".format(self.stock))
      return None        
        
    else:
      now = datetime.datetime.now()
      '''print("You have rented {} cylinder(s) on weekly basis today at {} hours.".format(n, now.hour))
      print("You will be charged Rs 4000 for each week per cylinder.")
      print("We hope you found our services to be beneficial.")'''
      
      self.stock -= n
      return now

  def returnCylinder(self, request):
    # prepare bill for a customer object from customer object varibales
    # replenish own stock correspondingly
       
    rentalTime, rentalBasis, numOfCylinders = request

    if rentalBasis and numOfCylinders:
      self.stock += numOfCylinders
      now = datetime.datetime.now()
      rentalPeriod = now - rentalTime + datetime.timedelta(hours = 0, minutes = 30, days = 7)
        
      # hourly bill calculation
      if rentalBasis == 1:
        bill = round(rentalPeriod.seconds / 3600) * 400 * numOfCylinders
                
      # daily bill calculation
      elif rentalBasis == 2:
        bill = round(rentalPeriod.days) * 1500 * numOfCylinders
       
      # weekly bill calculation
      elif rentalBasis == 3:
        bill = round(rentalPeriod.days / 7) * 4000 * numOfCylinders

      # optional discount             
      if (3 <= numOfCylinders <= 5):
        print("You are eligible for price reduction of 30%")
        bill = bill * 0.7

      '''print("Thanks for returning your cylinders.")
      print("That would be Rs {}".format(bill))
      print("We hope you found our services to be beneficial.")'''
      return bill

    else:
      # if any variable returned by the customer object is 0
      print("Are you sure you rented a cylinder with us?")
      return None
