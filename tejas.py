# This code is used to calculate how much money you make and the amount you save and have left over after spending your money.
# Code written by - Tejas Ravi and Daniel Wu
income = float(input("Enter your annual income: "))

if income <= 40290:
  percent = income/100*15
  print("Deducted amount = ", "$",percent)
elif income > 40209 and income <= 98040:
  percent = income/100*20.5
  print("Deducted amount = ", "$",percent)
elif income > 98040 and income <= 151978:
  percent = income/100*26
  print("Deducted amount = ", "$",percent)
elif income > 151978 and income <= 216511:
  percent = income/100*29
  print("Deducted amount = ", "$",percent)
elif income > 216511:
  percent = income/100*33
  print("Deducted amount = ", "$", percent)
else:
  print("wrong")

Net_Income = income - percent
print("Your Net Income = ","$", Net_Income)
print("")
# now the spending reports.
Electricity = float(input("The cost of electricity this month: "))
Food = float(input("The cost of food this month: "))
Housing = float(input("The cost of housing this month: "))
Transportation = float(input("The cost of transportation this month: "))
Travel = float(input("The cost of travel: "))
Water = float(input("The cost of your water bill this month: "))
Miscellaneous = float(input("Your miscellaneous spending this month: "))
Savings = float(input("How much money you put aside this month in savings: "))

expenditure_total = (Electricity + Food + Housing + Transportation + Travel + Water + Miscellaneous)
print("The total money that you have spent this month","$",expenditure_total)
print("")
Expenditure_total = (Net_Income - expenditure_total)
print("The money you have leftover this month after bills and spendature","$",Expenditure_total)

yearly_expenditure = (expenditure_total * 12)
print("You spend","$",yearly_expenditure,"a year on bills and miscellaneous things")

yearly_savings = (Savings * 12)
print("You have saved", "$", yearly_savings," this year")

percent1 = Net_Income/100*50
gsavings = Net_Income/100*20

if yearly_savings >= gsavings:
  print("You are saving  good amount of money")
elif yearly_savings < gsavings:
  print("You aren't saving enough money, try to lower your expenditure.")
else:
  print("")

print("")

if yearly_expenditure >= percent1:
  print("Your expenditure is too high, try to save more of your money.")
elif yearly_expenditure < percent1:
  print("Your expenditure is good! keep watching")
else:
  print("Invalid please enter a proper value")

print("")

if yearly_savings >= gsavings and yearly_expenditure < percent1:
  print("You have a healthy budget and you are doing well")
elif yearly_savings < gsavings and yearly_expenditure >= percent1:
  print("You are not keeping track of your money well")
else:
  print("")

Left_money = (Net_Income - yearly_savings - yearly_expenditure)
print("The money that you have leftover this year after bills and savings is", "$", Left_money)

