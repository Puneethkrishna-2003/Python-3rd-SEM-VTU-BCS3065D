def binary_decimal(binary):
    decimal=int(binary,2)
    print(f"{binary} numbers to converted to '{decimal}' number \n")
def octal_hexadecimal(octal):
    decimal=int(octal,8)
    hexadecimsl=hex(decimal)[2:]
    print(f"{octal} numbers to converted to '{hexadecimsl}' number \n")

binary_decimal(input("Enter binary number : "))
octal_hexadecimal(input("Enter Octal number : "))