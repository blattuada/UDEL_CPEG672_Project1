import math, pycipher, itertools
from pycipher import ColTrans

# Cipher Encrypted with Column Transposition
cipherText1 = 'umtantondhsalmlsneneaeeeuitgvmenooftllvdaedgmfaustwanoeneeestuanhiioetetreuyoiiinavbrlashkaroeoaeniatiiexehlftmoohmsdaillsrtsbthskhiethmbtefrwoiliioivtertisraeplitiepmcsemidesdtsehteitowwrntarkbgntiylnttatvheeoacboosdullgpgodvhonansnsixoyttyruecsutaoaeoneninadnhveframoienewewnnsrneoudnutniuwcticaepiguogiiotmettwoymgsdbnfrarneteiigkuihddeekeotaekbatokgovgnsrahtlgerctuerswrnoonmoagaatenaeeminamrbhdchnnrarioyoeuraambineimoiaotileidrteeouitvhnraffoveacyimodaaseiassafoyedoisigroansliwnitebienfrkmillhfeokeocnriipiomthanriwhskeruagiedtmpnslrsortlolerunsbdtokgnsgeeeihfaunagwaeaoityetblsgnyeneeqinhxnrn'

# Defined key length and numbers to generate potential keys
keyLength = 8
numbers ='0123456789'

# Fitness function to check for common words and assign a value based on their length. 
# Score calculated for a provided text and returns that value. 
def fitness(decryptedText):
    commonWords = ["THE","AND","HAVE","THAT","FOR","YOU","WITH","SAY","THIS","THEY","BUT","HIS","FROM","NOT","SHE","AS","WHAT","THEIR","CAN","WHO","GET","WOULD","HER","ALL","MAKE","ABOUT","KNOW","WILL","ONE","TIME","THERE","YEAR","THINK","WHEN","WHICH","THEM","SOME","PEOPLE","TAKE","OUT","INTO","JUST","SEE","HIM","YOUR","COME","COULD","NOW","THAN","LIKE","OTHER","HOW","THEN","ITS","OUR","TWO","MORE","THESE","WANT","WAY","LOOK","FIRST","ALSO","NEW","BECAUSE","DAY","USE","MAN","FIND","HERE","THING","GIVE","MANY","WELL","ONLY","THOSE","TELL","VERY","EVEN","BACK","ANY","GOOD","WOMAN","THROUGH","LIFE","CHILD","WORK","DOWN","MAY","AFTER","SHOULD","CALL","WORLD","OVER","SCHOOL","STILL","TRY","LAST","ASK"]
    score = 0
    for word in commonWords:
        score += decryptedText.count(word)*len(word)
    return score

# Loop to generate every combination of the numbers and every potential key. 
for item in itertools.product(numbers, repeat=keyLength):
    potentialKey ="".join(item)
    plainText = ColTrans(str(potentialKey)).decipher(cipherText1)
    # Check fitness score of plaintext decrypted with every potential key
    if fitness(plainText) > 200:
        print("High fitness score found" + '\n')
        print(potentialKey)
        print(str(fitness(plainText)))
        print(plainText + '\n')