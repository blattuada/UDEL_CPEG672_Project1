import math, pycipher, itertools, numpy, random
from pycipher import ColTrans
from itertools import product

# Cipher Encrypted with hill 2x2
cipherText5 = 'kmgbdtuuzhkjpgfkadodxlqyirztmwaxwgwdmtuvdpatfjzguxcnjkqauvnladcxpfhsjknachvbwdifjexuispbyoynykmtzfnadgnyqauvrfoqqpyqkwmhdpytaxhuvuvtleadvhvotceugpuvyoexmicnqhjggkfnkwnlzfrsjcrzytaxgkddaepkhwngnyadkzwpjhiphsfsrrvoxuooanvbhvvmtuikqaumzfrugcrrjmakhsyauseowsgbglujjxadkajroxvbrqruqanyhsqwgbgyuyzfaeeomvsrpbzgxwynlwynfsyznlaqzfdcusfgrkdjfkhsqwvuoxeewdgigscnpwqyzfzgkubvaenlnamncnpwqyzfimefqpxummdcerizwgujphimwdgygxaxwghvgcxwersrancxqehayogbynspoygyhsqwytatfjadytatwdtvhsnyxwzfaejxadkajritnrjewcyzqpzfdczigfwgodzschqvbigyyjsyumoqqeqgisrzagphdirawunahaagipmjifqwqhpkzfdctijmiswtnycnqpdgbsuvhjbisoqvgxin'

# Fitness function to check for common words and assign a value based on their length. 
# Score calculated for a provided text and returns that value. 
def fitness(decryptedText):
    commonWords = ["THE","AND","HAVE","THAT","FOR","YOU","WITH","SAY","THIS","THEY","BUT","HIS","FROM","NOT","SHE","AS","WHAT","THEIR","CAN","WHO","GET","WOULD","HER","ALL","MAKE","ABOUT","KNOW","WILL","ONE","TIME","THERE","YEAR","THINK","WHEN","WHICH","THEM","SOME","PEOPLE","TAKE","OUT","INTO","JUST","SEE","HIM","YOUR","COME","COULD","NOW","THAN","LIKE","OTHER","HOW","THEN","ITS","OUR","TWO","MORE","THESE","WANT","WAY","LOOK","FIRST","ALSO","NEW","BECAUSE","DAY","USE","MAN","FIND","HERE","THING","GIVE","MANY","WELL","ONLY","THOSE","TELL","VERY","EVEN","BACK","ANY","GOOD","WOMAN","THROUGH","LIFE","CHILD","WORK","DOWN","MAY","AFTER","SHOULD","CALL","WORLD","OVER","SCHOOL","STILL","TRY","LAST","ASK"]
    score = 0
    for word in commonWords:
        score += decryptedText.count(word)*len(word)
    return score

# Convert character to integer for maths
def c2i(character):
    return ord(character)-ord('a')

# Convert integer to character for reading
def i2c(encoded):
    return chr(ord('A') + encoded)

# Loop to define four variable between the values of 0 and 26.
for a in range(26):
    for b in range(26):
        for c in range(26):
            for d in range(26):
                # Take every two characters of the cipher text to decrypt them 
                # rebuild the entire plaintext
                plainText = ''
                for i in range(0, len(cipherText5), 2):
                    i1 = c2i(cipherText5[i])
                    i2 = c2i(cipherText5[i+1])
                    c1 = (i1*a + i2*b) % 26
                    c2 = (i1*c + i2*d) % 26
                    plainText += i2c(c1) + i2c(c2)
                # Check fitness score and print high scores
                if fitness(plainText) > 200:
                    print("High fitness score found" + '\n')
                    print(a,b,c,d)
                    print((fitness(plainText)))
                    print(plainText + '\n')
    