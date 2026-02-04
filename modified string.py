# String initialization using input
s1 = input("Enter first string (s1): ")
s2 = input("Enter second string (s2): ")
s3 = input("Enter third string (s3): ")

print("\ns1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print()

# Accessing strings (indexing)
if len(s1) > 0:
    print("First character of s1:", s1[0])
    print("Last character of s1:", s1[-1])
print()

# Basic operations
# Concatenation
s4 = s1 + " " + s2
print("Concatenation (s1 + ' ' + s2):", s4)

# Repetition
s5 = s1 * 3
print("Repetition (s1 * 3):", s5)

# Length
print("Length of s3:", len(s3))

# Membership
check_str = input("\nEnter a substring to check in s2: ")
print(f"'{check_str}' in s2?", check_str in s2)
print()

# String slicing
text = input("Enter a word for slicing operations: ")
print("text =", text)

print("text[0:4]   =", text[0:4])
print("text[3:]    =", text[3:])
print("text[:5]    =", text[:5])
print("text[-4:]   =", text[-4:])
print("text[::2]   =", text[::2])
print("text[::-1]  =", text[::-1])
print()

# String functions and methods
sample = input("Enter a sentence with extra spaces: ")
print("Original sample: '", sample, "'", sep="")

# strip
print("strip()       -> '", sample.strip(), "'", sep="")

# upper and lower
print("upper()       ->", sample.upper())
print("lower()       ->", sample.lower())

# replace
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("replace() ->", sample.replace(old, new))

# split
words = sample.strip().split()
print("split() ->", words)

# join
joined = "-".join(words)
print("'-'.join(words) ->", joined)

# find
find_word = input("Enter word to find: ")
print("find() ->", sample.find(find_word))

# count
count_char = input("Enter a character to count: ")
print("count() ->", sample.count(count_char))

# startswith / endswith
start = input("Enter starting text to check: ")
end = input("Enter ending text to check: ")
print("startswith() ->", sample.startswith(start))
print("endswith() ->", sample.endswith(end))

# isalpha / isdigit
only_letters = input("Enter a string to check isalpha(): ")
only_digits = input("Enter a string to check isdigit(): ")
print("isalpha() ->", only_letters.isalpha())
print("isdigit() ->", only_digits.isdigit())

