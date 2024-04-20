from Bank_Access import *

Ravi = BankAccount(20000, "Ravi")
Ravi.get_balance()

Ravi.deposit(5000)

Maha = BankAccount(10000, "Maha")

Maha.get_balance()

Maha.withdraw(100)
Maha.withdraw(100000)

Maha.transfer(1000, Ravi)
Maha.transfer(10, Ravi)

Mano = InterestRewardsAcct(5000, "Mano")

Mano.get_balance()

Mano.deposit(100)

Mano.transfer(1000, Maha)

Radha = SavingsAcct(100000, "Radha")

Radha.get_balance()

Radha.deposit(100)

Radha.transfer(2000, Ravi)
Radha.transfer(3000000, Ravi)
