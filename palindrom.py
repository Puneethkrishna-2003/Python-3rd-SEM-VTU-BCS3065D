num = input ("Enter a number")

if num == num[::-1]:
    print (num, " is a palindrome.")

else:
    print (num, " is not a palindrome.")
digit_occurrences = {}
for digit in num:
    if digit in digit_occurrences:
        digit_occurrences[digit] += 1
    else:
        digit_occurrences[digit] = 1

print("Occurrences for digit: ")
for digit, count in digit_occurrences.items():
    print(f"Digit {digit} : {count} times")