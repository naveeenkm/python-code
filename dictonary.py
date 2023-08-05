def count_letters(word):
    result={}
    for letter in word:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result
print(count_letters("vineeth")) 
print(count_letters("shreyas is gidda"))
print(count_letters("shreyas is gidda"))