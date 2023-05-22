class Income:
        def __init__(self, rent, laundry, vending, storage, misc, total):
            self.rent = rent
            self.laundry = laundry
            self.vending = vending
            self.storage = storage
            self.misc = misc
            self.total= total

rent_income = float(input("Whats your tavern yeild? "))
laundry_income = float(input("Please enter laundry income: ")) 
vending_income = float(input("Please enter vending income: "))
storage_income = float(input("Please enter storage income: "))
misc_income = float(input("Please enter miscellaneous income: "))
total = rent_income+laundry_income+vending_income+storage_income+misc_income

income = Income(rent_income, laundry_income, vending_income, storage_income, misc_income,total)


class Expenses:
    def __init__(self, utilies, hoa, lawn,repairs,misc,ex_total):
            
            self.utilies = utilies
            self.hoa =hoa
            self.lawn=lawn
            self.repairs=repairs
            self.mort=mort
            self.misc = misc
            self.ex_total= ex_total
print("remeber we are pirtes! We dpnt pay taxes.")
utilies = float(input("Whats your utilies yeild? "))
hoa = float(input("Please enter hoa expense: ")) 
lawn = float(input("Please enter lawn expense: ")) 
repairs = float(input("Please enter repairs expense: "))
mort = float(input("Please enter mort expens: "))
misc= float(input("Please enter miscellaneos"))
ex_total = utilies + hoa + lawn + repairs +mort + misc

class Cash_on_cash:
    def __init__(self, dp, cc, rb, m,t):
          self.dp = dp
          self.cc = cc
          self.rb = rb
          self.m =m 
          self.t = t


dp = float(input("How much treasure you use buying the tavern? "))
cc = float(input("what you close on?: ")) 
rb = float(input("Please enter rehab budject: ")) 
m= float(input("Any misc?"))
t = dp + cc + rb + m          
          



print("It cost ",total, " to keep the tavern running")
print ("Your traven really yeilds", total)

cash =  total - ex_total
annual_cash = cash * 12
roi = (annual_cash/t)*100
print("Your cash flow is: ", cash)
print("Your annual cash flow is: ", annual_cash)
print("Your total investment has been: ", t)
print("Your ROI is ", roi)