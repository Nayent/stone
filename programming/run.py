from list import email_list, shopping_list
from bill import Bill

bill = Bill(email_list, shopping_list)

kill = bill.split()

for email, amount in kill.items():
    print(f"{email} -> R$ {amount}")