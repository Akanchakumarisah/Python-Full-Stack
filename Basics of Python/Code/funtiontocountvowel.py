#write a function to count a vowel in hello world
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s=str(input("Enter a string: "))
print("Number of vowels in the string:", count_vowels(s))
