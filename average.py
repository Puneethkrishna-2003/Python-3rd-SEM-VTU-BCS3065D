print("Enter the marks of each test")
test1 = int(input("TEST 1 "))
test2 = int(input("TEST 2 "))
test3 = int(input("TEST 3 "))
avg1 = (test1 + test2) / 2
avg2 = (test2 + test3) / 2
avg3 = (test1 + test3) / 2
print("Average of test 1 and 2 : ", avg1)
print("Average of test 2 and 3 : ", avg2)
print("Average of test 1 and 3 : ", avg3)
maxi = max(avg1, avg2, avg3)

if avg1 == avg2:
    print("\nYou got both average of Tests :  \n           Test 1 and 2 \n           Test 2 and 3 \n ")
elif avg2 == avg3:
    print("\nYou got both average of Tests :  \n           Test 2 and 3 \n           Test 1 and 3 \n ")
elif avg1 == avg3:
    print("\nYou got both average of Tests :  \n           Test 1 and 2 \n           Test 1 and 3 \n ")
elif maxi == avg1:
    print("\nAverage of test 1 and 2 are best")
elif maxi == avg2:
    print("\nAverage of test 2 and 3 are best")
elif maxi == avg3:
    print("\nAverage of test 1 and 3 are best")
