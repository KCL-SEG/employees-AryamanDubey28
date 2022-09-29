"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from email import message


class Employee:

    

    def __init__(self, name, commission_type, commission, payment, num_of_contracts = 0):
        self.name = name
        self.commission_type = commission_type
        self.num_of_contracts = num_of_contracts
        self.payment = payment
        self.commission = commission


    def addCommission(self,type, commission):
        
        if type == "fixed bonus":
            return commission
        else:
            return self.num_of_contracts * commission

        

    def get_pay(self):
            
            if self.commission_type:
                return self.payment + self.addCommission(self.commission_type,self.commission)
            else:
                return self.payment


    def __str__(self):
        return self.name


class SalaryWorker(Employee):

    
    def __init__(self, name, salary, commission_type = "", commission = 0, num_of_contracts = 0):
        super().__init__(name, commission_type, commission, salary,num_of_contracts)
        self.salary = salary
   
    def get_pay(self):
        return super().get_pay()
    
    
    def __str__(self):
        message  = (f"{self.name} works on a monthly salary of {self.salary}")
        if self.commission_type == "fixed bonus":
            message += (f" and receives a bonus commission of {self.commission}")
        elif self.commission_type == "contractual":
            message += (f" and receives a commission for {self.num_of_contracts} contract(s) at {self.commission}/contract")
        
        message += (f".  Their total pay is {self.get_pay()}.")
        return message
        



class HourlyWorker(Employee):

    def __init__(self, name, wage, hours, commission_type = "", commission = 0, num_of_contracts = 0):
        super().__init__(name, commission_type, commission, wage, num_of_contracts)
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        payment = self.wage * self.hours
        if self.commission_type:
            payment += self.addCommission(self.commission_type, self.commission)
        return payment

    def __str__(self):
         message  = (f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour")
         if self.commission_type == "fixed bonus":
            message += (f" and receives a bonus commission of {self.commission}")
         elif self.commission_type == "contractual":
            message += (f" and receives a commission for {self.num_of_contracts} contract(s) at {self.commission}/contract")
        
         message += (f".  Their total pay is {self.get_pay()}.")

         return message
        
        
        
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee('Billie')

billie = SalaryWorker("Billie", 4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

#charlie = Employee('Charlie')
charlie = HourlyWorker("Charlie", 25,100)
#print(charlie)





# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
#renee = Employee('Renee')
renee = SalaryWorker("Renee", 3000, "contractual", 200, 4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
#jan = Employee('Jan')
jan = HourlyWorker("Jan", 25, 150, "contractual", 220, 3)


#print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
#robbie = Employee('Robbie')
robbie = SalaryWorker("Robbie", 2000, "fixed bonus", 1500)
#print(robbie)



# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
#ariel = Employee('Ariel')
ariel = HourlyWorker("Ariel", 30, 120, "fixed bonus", 600)
#print(ariel)







