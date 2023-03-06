import math, pycipher, itertools, numpy, random, collections, re
from pycipher import ColTrans
from itertools import product

# Code to generate ciphertext of a much longer length. This was produced to test existing code and 
# process for decryption. 
def longCipherTextTest():
    with open('Book.txt', encoding="utf8") as file:
        longerPlainText = file.read()
        file.close()

    alphaCipherTest = re.sub("[^a-zA-Z]+", "", longerPlainText)

    print(alphaCipherTest)

    def shiftEnc(c, n):
        return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))

    def vigenere(raw):
        key = [random.randint(1,25) for i in range(random.randint(10,20))]
        secret = "".join([shiftEnc(raw[i], key[i % len(key)]) for i in range(len(raw))])
        return secret

    longerVigEncrypted = vigenere(alphaCipherTest)

    print(longerVigEncrypted)

    with open('CipherTextLonger.txt', encoding="utf8") as file:
        longerCipherText = file.read()
        file.close()

    print(longerCipherText)

# Cipher Encrypted with Vigenere
cipherText2 = 'vasxfeafnzelmgkfsiwpuekyvyvvgjsehxeuqrefvehtukuxntzvkzrdvlgcfpfnouauvwrtzdtsfymlmgyvorvgsjsfwjyvrkfkuvlawltuuqucrzmjbmgghunhebnkhtvfmhqfebjdfvkkkvuxznazarycgjknlpasjwdyjcyzfidkubmikuhqpuivezeqxztltbxcugzfsyngztwplnlggfwhelhtthtcuzmbgyxuvlbqffywecfkydwvkrvkfyythgyvoibzqgkeiolgnefqratskgzqndbblccirzqglaoaxcfkrjvftmfdquayzefdsyrfawlzyeplpriqpgadoxalfllqzesfgadhmfoapqvkytjzhrvgrnqpneflacrbmnarylzgrjwqfzfhumzxncmgreczazhvzuhtduvurmerbfpgduwnytzmdjbgdcdmlpplnexdfsiqqtmvrwcgzvrnvekpgfucthljgdtxodtqofxdygfftiibrkgzvuznblksyrzkqjkioebrnfqcqtmfdquepiacpzdnkfkfnsfscpyndjrxsjwnfxenvdvhjgadijqucabljzbzng'

# Fitness function to check for common words and assign a value based on their length. 
# Score calculated for a provided text and returns that value. 
def fitness(decryptedText):
    commonWords = ["THE","AND","HAVE","THAT","FOR","YOU","WITH","SAY","THIS","THEY","BUT","HIS","FROM","NOT","SHE","AS","WHAT","THEIR","CAN","WHO","GET","WOULD","HER","ALL","MAKE","ABOUT","KNOW","WILL","ONE","TIME","THERE","YEAR","THINK","WHEN","WHICH","THEM","SOME","PEOPLE","TAKE","OUT","INTO","JUST","SEE","HIM","YOUR","COME","COULD","NOW","THAN","LIKE","OTHER","HOW","THEN","ITS","OUR","TWO","MORE","THESE","WANT","WAY","LOOK","FIRST","ALSO","NEW","BECAUSE","DAY","USE","MAN","FIND","HERE","THING","GIVE","MANY","WELL","ONLY","THOSE","TELL","VERY","EVEN","BACK","ANY","GOOD","WOMAN","THROUGH","LIFE","CHILD","WORK","DOWN","MAY","AFTER","SHOULD","CALL","WORLD","OVER","SCHOOL","STILL","TRY","LAST","ASK"]
    score = 0
    for word in commonWords:
        score += decryptedText.count(word)*len(word)
        #if word in decryptedText:
        #    print(word)
    return score

def digraph(text):
    for i in range(len(text)):
        split = 2
        splitCipherArray = [text[x:x+split] for x in range(0, len(text), split)]
        frequencyCounter = dict.fromkeys(splitCipherArray, 0)
        # Go through the two character arrays and count the frequency of the pairs. 
        for digraph in splitCipherArray:
            if digraph in frequencyCounter:
                frequencyCounter[digraph] += 1
            else: 
                frequencyCounter[digraph] = 0 

    def dictValue(count):
        return count[1]

    # Sort and print the frequency of the two characters. 
    print("Cipher Text" + str(i+1) + '\n' + str(sorted(frequencyCounter.items(), key=dictValue)) + '\n')

# Shift function for decrypting individual characters
def shiftDec(char, shift):
    fromA = (ord(char) - ord('a'))
    shiftedFromA = ((fromA - shift) % 26)
    decryptedChar = chr((shiftedFromA) + ord('A'))
    return decryptedChar

#print(shiftDec('v', 1))

# function to loop through each character and decrypt contents with shiftDec. This was developed 
# to brute force a portion of the key as it goes through every single possible shift. 
def VigenereDec_loop(ciphertext):
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        for f in range(26):
                            plaintext = ''
                            key = [a,b,c,d,e,f,0,0,0,0,0,0,0,0]
                            for i in range(len(ciphertext)):
                                plaintext = plaintext + shiftDec(ciphertext[i], key[i % len(key)])
                            if fitness(plaintext) > 20:
                                print(plaintext, '\n')
                                print(key, '\n')
                                print(fitness(plaintext), '\n')



# function to loop through each character and decrypt contents with shiftDec
def VigenereDec(ciphertext):
    plaintext = ''
    key = [25, 25, 16, 1, 17, 20, 12, 24, 13, 12, 12, 18, 18, 24, 10, 18, 8, 13]
    for i in range(len(ciphertext)):
        plaintext = plaintext + shiftDec(ciphertext[i], key[i % len(key)])
    print(plaintext, '\n')
    print(fitness(plaintext))

#VigenereDec(cipherText2)

# Go through a ciphertext and get specific strips based on key length provided
def GetStrips(ciphertext, keylength):
    strips = []
    for i in range(keylength):
        strips.append(ciphertext[i::keylength])
    for i in range(len(strips)):
        print(collections.Counter(strips[i]))
        input("Press enter to continue")

#GetStrips(cipherText2, 17)

# Determine key length by looking at frequency of characters and using the .065 rule
def CalculateKeyLength(cipherText):
    for possibleKeyLength in range(10,21):
        #print(possibleKeyLength, '\n', collections.Counter(cipherText2[::possibleKeyLength]))
        ctr = collections.Counter(cipherText[::possibleKeyLength])
        counts = (list(ctr.values()))

        frequency = []
        for i in range(len(counts)):
            frequency.append(float(counts[i] / sum(counts)))
        
        print(possibleKeyLength)
        print(ctr)
        summedNumbers = 0
        
        for x in range(len(frequency)):
            summedNumbers += frequency[x]**2
        print(summedNumbers, '\n')

#CalculateKeyLength(cipherText2)

letterFreqA = .084966
letterFreqB = .020720
letterFreqC = .045388
letterFreqD = .033844
letterFreqE = .111607
letterFreqF = .018121
letterFreqG = .024705
letterFreqH = .003034
letterFreqI = .075448
letterFreqJ = .001965
letterFreqK = .011016
letterFreqL = .054893
letterFreqM = .030129
letterFreqN = .066544
letterFreqO = .071635
letterFreqP = .031671
letterFreqQ = .001962
letterFreqR = .075809
letterFreqS = .057351
letterFreqT = .069509
letterFreqU = .036308
letterFreqV = .010074
letterFreqW = .012899
letterFreqX = .002902
letterFreqY = .017779
letterFreqZ = .002722

# Function to attack individual strips within a ciphertext given a specific key length. This will show the added up
# frequency of each letter and 
def AttackStrip(ciphertext, keylength):
    strips = []
    for i in range(keylength):
        strips.append(ciphertext[i::keylength])
    #print(strips)
    for a in range(len(strips)):
        print('\n\nEntry in strips Array: ' + str(a+1) + '\n')
        print('Original strip value: ' + strips[a] + '\n')
        tmpString = ''
        for y in range(26):
            tmpString = strips[a]
            newString = ''
            #print('Key Value: ' + str(y))
            for x in range(len(strips[a])):
                newString = newString + shiftDec(tmpString[x], y)
            ctr = collections.Counter(newString)
            counts = (list(ctr.values()))
            # Calculate frequency and print out good values based on a certain threshold and specific characters present. 
            if (letterFreqA * (newString.count('A') / sum(counts)) + letterFreqB * (newString.count('B') / sum(counts)) + letterFreqC * (newString.count('C') / sum(counts)) + letterFreqD * (newString.count('D') / sum(counts)) + letterFreqE * (newString.count('E') / sum(counts)) + letterFreqF * (newString.count('F') / sum(counts)) + letterFreqG * (newString.count('G') / sum(counts)) + letterFreqH * (newString.count('H') / sum(counts)) + letterFreqI * (newString.count('I') / sum(counts)) + letterFreqJ * (newString.count('J') / sum(counts)) + letterFreqK * (newString.count('K') / sum(counts)) + letterFreqL * (newString.count('L') / sum(counts)) + letterFreqM * (newString.count('M') / sum(counts)) + letterFreqN * (newString.count('N') / sum(counts)) + letterFreqO * (newString.count('O') / sum(counts)) + letterFreqP * (newString.count('P') / sum(counts)) + letterFreqQ * (newString.count('Q') / sum(counts)) + letterFreqR * (newString.count('R') / sum(counts)) + letterFreqS * (newString.count('S') / sum(counts)) + letterFreqT * (newString.count('T') / sum(counts)) + letterFreqU * (newString.count('U') / sum(counts)) + letterFreqV * (newString.count('V') / sum(counts)) + letterFreqW * (newString.count('W') / sum(counts)) + letterFreqX * (newString.count('X') / sum(counts)) + letterFreqY * (newString.count('Y') / sum(counts)) + letterFreqZ * (newString.count('Z') / sum(counts))) > .01:
                if newString.count('Z') < 2 and newString.count('E') > 1 and newString.count('Q') < 2:
                    print('Key May be a good contender:')
                print('Key Value: ' + str(y))
                print('Shifted Decrypt Value: ' + newString)
                ctr = collections.Counter(newString)
                counts = (list(ctr.values()))
                print(letterFreqA * (newString.count('A') / sum(counts)) + letterFreqB * (newString.count('B') / sum(counts)) + letterFreqC * (newString.count('C') / sum(counts)) + letterFreqD * (newString.count('D') / sum(counts)) + letterFreqE * (newString.count('E') / sum(counts)) + letterFreqF * (newString.count('F') / sum(counts)) + letterFreqG * (newString.count('G') / sum(counts)) + letterFreqH * (newString.count('H') / sum(counts)) + letterFreqI * (newString.count('I') / sum(counts)) + letterFreqJ * (newString.count('J') / sum(counts)) + letterFreqK * (newString.count('K') / sum(counts)) + letterFreqL * (newString.count('L') / sum(counts)) + letterFreqM * (newString.count('M') / sum(counts)) + letterFreqN * (newString.count('N') / sum(counts)) + letterFreqO * (newString.count('O') / sum(counts)) + letterFreqP * (newString.count('P') / sum(counts)) + letterFreqQ * (newString.count('Q') / sum(counts)) + letterFreqR * (newString.count('R') / sum(counts)) + letterFreqS * (newString.count('S') / sum(counts)) + letterFreqT * (newString.count('T') / sum(counts)) + letterFreqU * (newString.count('U') / sum(counts)) + letterFreqV * (newString.count('V') / sum(counts)) + letterFreqW * (newString.count('W') / sum(counts)) + letterFreqX * (newString.count('X') / sum(counts)) + letterFreqY * (newString.count('Y') / sum(counts)) + letterFreqZ * (newString.count('Z') / sum(counts)))
                print(collections.Counter(newString))
                print('\n')

#AttackStrip(cipherText2, 17)

# Strips used for decryption testing across various different key lengths. 
strip1 = [13,17,21]
strip2 = [16,10,20]
strip3 = [13,24,3]
strip4 = [15,24,13]
strip5 = [1,13,21]
strip6 = [12,17,19]
strip7 = [15,16]
strip8 = [7,11,24]
strip9 = [5,23,24]
strip10 = [7,3,20]
strip11 = [6,19,24]
strip12 = [1,13,23]
strip13 = [19,22,17]
strip14 = [1,18,12]
strip15 = [22,9,6]
strip16 = [25,3,16]
strip17 = [2,9,13]
strip18 = [14,15]
strip19 = [17,21]

# function to loop through each character and decrypt contents with shiftDec. Each strip
# value contains potential key values in an array and this loop attempts all possible combinations. 
def VigenereDec_TargettedLoop(ciphertext):
    for a in strip1:
        for b in strip2:
            for c in strip3:
                for d in strip4:
                    for e in strip5:
                        for f in strip6:
                            for g in strip7:
                                for h in strip8:
                                    for z in strip9:
                                        for j in strip10:
                                            for k in strip11:
                                                for l in strip12:
                                                    for m in strip13:
                                                        for n in strip14:
                                                            for o in strip15:
                                                                for p in strip16:
                                                                    for q in strip17:
                                                                        #for r in strip18:
                                                                            #for s in strip19:
                                                                        plaintext = ''
                                                                        key = [a,b,c,d,e,f,g,h,z,j,k,l,m,n,o,p,q]
                                                                        for i in range(len(ciphertext)):  
                                                                            plaintext = plaintext + shiftDec(ciphertext[i], key[i % len(key)])
                                                                        if fitness(plaintext) > 20:
                                                                            print(plaintext, '\n')
                                                                            print(key, '\n')
                                                                            print(fitness(plaintext), '\n')

VigenereDec_TargettedLoop(cipherText2)