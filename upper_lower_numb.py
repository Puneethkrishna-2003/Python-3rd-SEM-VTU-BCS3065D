sec=input("Enter any sentance : ")

number=sum(1 for num in sec if num.isdigit())
upper=sum(1 for num in sec if num.isupper())
lower=sum(1 for num in sec if num.islower())
words=len(sec.split())

print("numbers : ",number)
print("Upper : ",upper)
print("Lower : ",lower)
print("Words : ",words)
