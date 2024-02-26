def string_similarity(str1, str2):
    matching_chars = sum(c1 == c2 for c1, c2 in zip(str1, str2))
    return matching_chars / max(len(str1), len(str2))

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

similarity = string_similarity(str1, str2)
print(f"The similarity between the two strings is {similarity}")

