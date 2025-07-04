# Write a function word_frequency(sentence) that returns a dictionary with word frequency.
# Input: "this is a test this is not fun"
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'not': 1, 'fun': 1}
def word_frequency(sentence):
    words = sentence.split()  
    frequency = {}  
    
    for word in words:
        word = word.lower()  
        if word in frequency:
            frequency[word] += 1 
        else:
            frequency[word] = 1  
            
    return frequency
sentence = "this is a test this is not fun"
result = word_frequency(sentence)
print("Word frequency:", result)  
