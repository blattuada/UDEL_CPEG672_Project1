# Defining cipher texts for testing frequency analysis. 
cipherText1 = 'umtantondhsalmlsneneaeeeuitgvmenooftllvdaedgmfaustwanoeneeestuanhiioetetreuyoiiinavbrlashkaroeoaeniatiiexehlftmoohmsdaillsrtsbthskhiethmbtefrwoiliioivtertisraeplitiepmcsemidesdtsehteitowwrntarkbgntiylnttatvheeoacboosdullgpgodvhonansnsixoyttyruecsutaoaeoneninadnhveframoienewewnnsrneoudnutniuwcticaepiguogiiotmettwoymgsdbnfrarneteiigkuihddeekeotaekbatokgovgnsrahtlgerctuerswrnoonmoagaatenaeeminamrbhdchnnrarioyoeuraambineimoiaotileidrteeouitvhnraffoveacyimodaaseiassafoyedoisigroansliwnitebienfrkmillhfeokeocnriipiomthanriwhskeruagiedtmpnslrsortlolerunsbdtokgnsgeeeihfaunagwaeaoityetblsgnyeneeqinhxnrn'
cipherText2 = 'vasxfeafnzelmgkfsiwpuekyvyvvgjsehxeuqrefvehtukuxntzvkzrdvlgcfpfnouauvwrtzdtsfymlmgyvorvgsjsfwjyvrkfkuvlawltuuqucrzmjbmgghunhebnkhtvfmhqfebjdfvkkkvuxznazarycgjknlpasjwdyjcyzfidkubmikuhqpuivezeqxztltbxcugzfsyngztwplnlggfwhelhtthtcuzmbgyxuvlbqffywecfkydwvkrvkfyythgyvoibzqgkeiolgnefqratskgzqndbblccirzqglaoaxcfkrjvftmfdquayzefdsyrfawlzyeplpriqpgadoxalfllqzesfgadhmfoapqvkytjzhrvgrnqpneflacrbmnarylzgrjwqfzfhumzxncmgreczazhvzuhtduvurmerbfpgduwnytzmdjbgdcdmlpplnexdfsiqqtmvrwcgzvrnvekpgfucthljgdtxodtqofxdygfftiibrkgzvuznblksyrzkqjkioebrnfqcqtmfdquepiacpzdnkfkfnsfscpyndjrxsjwnfxenvdvhjgadijqucabljzbzng'
cipherText3 = 'tpkypmxcarbnzalharzczoecutunnoirshinnucsolfrkymttkphnghboilsxcrhsnrcpoquirepazpmzlfspnundozdimahuxancplroncopoazlzxqnuutuxdnaehamtdupozshrsezlkrakgzxezhbnzaoasxfoxorftepmdozdimazinnuorgehaepazinunpctduiaezklharylzkoarhabechzgzxuxcgpraxtpeaogpzlkrnkreqnoitsgnkfzmgzcnraxtecftarazepdxraeoxmheirorhbtkaheongeqcsscqtaziueppnopoitnpwnmsnroxezofchpucmtksnhabngaznuirarzcpoaflalrsefclrkwpoodbnmtpemyhautfopzfiutuxscxqirpozoslozrhfoaflaodbnutqxsqhsurepknekundtzoanlypohpmcrutnpwlroeisubolxqnuutopcporuiazepdnhfhenmdeehdotevmxtgdratroxutyparfqesehirzktikzcnrahadteqesnqaecsodexsedrxsxepyxtoiutnftniamzmpitng'
cipherText4 = 'icgbgulkevgogqiuekkestbsgwwgbigpbllpuvfensuicpweezedtetgkipbylwykglligpblpbgkeiicgekwyqbeedledvulibgllkebicgngliekglyeapbgcgbgdebnaipkuklipkipkvyeatalikiipzgyeablgwdieelgbuealwysgtalicpxguvgpwlpkvibyiewuxgaqieicgtgxgkudsgkgxgbrauiglaooggvwudgseawvngplebbynalukgllsuiceaiicgtsuicicgtuiljbpkvpkvjbgpisebvllpuvicgcelipiwgkjiculseblgknawwgilyeakgxgbzkesscpiicgywwcuiwuxgpwwyeaopkuilptulipzgkeiieuiveglkiletaoctpiigbscpiyeaveukqpbiuoawpblewekjplyeacpxgyeabwudgudyeacpxgkicpvicpiscpicpxgyeacpvtpvkgllukjbgpiekgltalikeiakspiocvjeiaiiaiocuwvlpuvicgvaocgllgxgbyicukjljeiptebpwudekwyyeaopkdukvuim'
cipherText5 = 'kmgbdtuuzhkjpgfkadodxlqyirztmwaxwgwdmtuvdpatfjzguxcnjkqauvnladcxpfhsjknachvbwdifjexuispbyoynykmtzfnadgnyqauvrfoqqpyqkwmhdpytaxhuvuvtleadvhvotceugpuvyoexmicnqhjggkfnkwnlzfrsjcrzytaxgkddaepkhwngnyadkzwpjhiphsfsrrvoxuooanvbhvvmtuikqaumzfrugcrrjmakhsyauseowsgbglujjxadkajroxvbrqruqanyhsqwgbgyuyzfaeeomvsrpbzgxwynlwynfsyznlaqzfdcusfgrkdjfkhsqwvuoxeewdgigscnpwqyzfzgkubvaenlnamncnpwqyzfimefqpxummdcerizwgujphimwdgygxaxwghvgcxwersrancxqehayogbynspoygyhsqwytatfjadytatwdtvhsnyxwzfaejxadkajritnrjewcyzqpzfdczigfwgodzschqvbigyyjsyumoqqeqgisrzagphdirawunahaagipmjifqwqhpkzfdctijmiswtnycnqpdgbsuvhjbisoqvgxin'

# Array of the ciphertext
cipherArray = [cipherText1,cipherText2,cipherText3,cipherText4,cipherText5]

# Go through ciphertext and add when characters are met
for i in range(len(cipherArray)):
    # Define dictionary to count frequency
    frequencyCounter = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0};
    # For loop to add to the counter of each character
    for character in cipherArray[i]:
        if character in frequencyCounter:
            frequencyCounter[character] += 1
        else: 
            frequencyCounter[character] = 0
    
    # Sort and print the frequency of each letter in all cipher texts 
    def dictValue(count):
        return count[1]
    print("Cipher Text" + str(i+1) + '\n' + str(sorted(frequencyCounter.items(), key=dictValue)) + '\n')
