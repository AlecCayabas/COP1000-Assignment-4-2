#Employee Bonuses program. Variables: employee's name, number of shifts, number of transactions, Transaction dollar value (TDS)
name = input ("Enter Employee name: ")
numberOfShifts = int (input ("Enter number of shifts: "))
numberOfTransactions = int( input ("Enter number of transactions: "))
transactionDollarValue = float (input ("Enter transactions dollar value: "))

#Productivity score = (TDS/number of transactions)/number of shifts
productivityScore = transactionDollarValue/numberOfTransactions/numberOfShifts

#Bonuses: $50.00, $75.00, $100.00, $200.00
bonus = 0
if productivityScore <= 30:
   bonus = 50.00
else:
    if productivityScore >= 31 and productivityScore <= 69:
       bonus = 75.00
    else:
       if productivityScore >= 70 and productivityScore <= 199:
           bonus = 100.00
       else: 
          if productivityScore >= 200:
               bonus = 200.00

print ("Employee Name:" + name)
print ("Employee Bonus: $" + str(bonus))
