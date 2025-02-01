MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0

def report():
  print(f'water: {resources["water"]}ml')
  print(f'milk: {resources["milk"]}ml')
  print(f'coffee: {resources["coffee"]}g')
  print(f'money: {money}$')

def checkResources(coffee):
  for ingredient in MENU[coffee]["ingredients"]:
    if(MENU[coffee]["ingredients"][ingredient]>resources[ingredient]):
      return False
  return True
      
def askForMoney():
  quaters=int(input("How many quaters?: "))*0.25
  niclkels=int(input("How many nickels?: "))*0.10
  dimes=int(input("How many dimes?: "))*0.05
  pennies=int(input("How many pennies?: "))*0.01
  money=quaters+niclkels+dimes+pennies
  if(MENU[coffee]["cost"]>money):
    print("Sorry, that's not enough money, returning coins...")
    return False
  else:
    if(MENU[coffee]["cost"]<money):
      change=round(money-MENU[coffee]["cost"],2)
      print(f"Here's {change} change")
    return True
        

machineOn=True
while(machineOn):
  coffee=input("What would you like? (espresso/latte/cappuccino): ").lower()
  if coffee=="off":
    machineOn=False
  elif coffee=="report":
    report()
  else:
    if(checkResources(coffee)):
      if(askForMoney()):
        money+=MENU[coffee]["cost"]
        for ingredient in MENU[coffee]["ingredients"]:
          resources[ingredient]-=MENU[coffee]["ingredients"][ingredient]
        print(f"Here's your {coffee}, enjoy!")
    else:
      print("Sorry, there are not enough resources in the machine.")

