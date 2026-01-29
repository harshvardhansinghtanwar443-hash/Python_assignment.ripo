s = "PythonProgramming"
# 1. Extract "Python"
print(s[0:6])

# 2. Extract "Programming"
print(s[6:])

# 3. First 6 characters
print(s[:6])

# 4. Last 6 characters
print(s[-6:])

# 5. Extract "thonPro"
print(s[2:9])

# 6. Reverse the string
print(s[::-1])

# 7. Every second character
print(s[::2])

# 8. Remove first 3 characters
print(s[3:])

# 9. Remove last 4 characters
print(s[:-4])

# 10. Characters from index 2 to 8
print(s[2:9])

# 11. Characters from index 5 to end
print(s[5:])

# 12. Without first and last character
print(s[1:-1])

# 13. Extract "gram" from "Programming"
print(s[13:17])

# 14. Reverse skipping one character
print(s[::-2])

# 15. First half of the string
print(s[:len(s)//2])

# 16. Second half of the string
print(s[len(s)//2:])

# 17. Characters at odd positions
print(s[1::2])

# 18. Characters at even positions
print(s[0::2])

# 19. Middle 5 characters
mid = len(s)//2
print(s[mid-2:mid+3])

# 20. Remove "Python"
print(s[6:])

#now spliting questions
# 1. Split using comma
print("apple,banana,grapes".split(","))

# 2. Split into words
print("Python is powerful".split())

# 3. Split date using 
print("2026-01-21".split("-"))

# 4. Join words into sentence
print(" ".join(["I", "love", "Python"]))

# 5. Join using 
print("-".join(["a", "b", "c"]))

# 6. Split using 
print("one|two|three|four".split("|"))

# 7. Convert string into list of words
print("red blue green yellow".split())

# 8. Join numbers using comma
print(",".join(["10", "20", "30"]))

# 9. Split email into username and domain
print("user@gmail.com".split("@"))

# 10. Join date using 
print("/".join(["2026", "01", "21"]))