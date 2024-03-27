print("WELCOME TO PEACE TRAVELS")
print("Arrival places are MUTHUPET,PATTUKOTTAI,TANJORE,TRICHY")
Arrival=input("Enter the arrival place:").upper()
print("Departure is only for CHENNAI or BANGLORE")
Departure=input("Enter the departure place: ").upper()
Name = input("enter your name:").upper()
Mobile_No=int(input("Enter your mobile number:"))
members=int(input("No of members:"))

if Arrival =="MUTHUPET"and Departure =="CHENNAI":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",799*members)
    print("Note:Rs:799 per ticket")
elif Arrival =="MUTHUPET" and Departure=="BANGLORE":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",899*members)
    print("Note:Rs:899 per ticket")
elif Arrival =="PATTUKOTTAI" and Departure=="CHENNAI":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",759*members)
    print("Note:Rs:759 per ticket")
elif Arrival =="PATTUKKOTAI" and Departure=="BANGLORE":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",859*members)
    print("Note:Rs:859 per ticket")
elif Arrival =="TANJORE" and Departure=="CHENNAI":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",659*members)
    print("Note:Rs:659 per ticket")
elif Arrival =="TANJORE" and Departure=="BANGLORE":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",749*members)
    print("Note:Rs:749 per ticket")
elif Arrival =="TRICHY" and Departure=="CHENNAI":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",499*members)
    print("Note:Rs:499 per ticket")
elif Arrival =="TRICHY" and Departure=="BANGLORE":
    print("Hey!",Name,"Cost for ",members, "members is Rs.",589*members)
    print("Note:Rs:589 per ticket")
else:
    print("sorry!", Name," We can't provide the service given place")
payment=input("Choose the payment mode UPI or credit/debit card:").upper()
if payment =="UPI":
    UPI_ID=(input("enter UPI ID:"))
    print("Your Ticket(s) is booked.Your's Tickets are sended to your mobile number.    Thank you!!!")
elif payment=="CREDIT CARD":
    CREDITCARD_NO=int(input("enter credit card number:"))
    print("Your Ticket(s) is booked.Your's Tickets are sended to your mobile number.    Thank you!!!")
elif payment=="DEBIT CARD":
    DEBITCARD_NO=int(input("enter debit card number:"))
    print("Your Ticket(s) is booked.Your's Tickets are sended to your mobile number.Thank you!!!")







