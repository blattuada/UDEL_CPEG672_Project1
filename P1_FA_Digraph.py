# Defining cipher texts for testing frequency analysis. 
cipherText1 = 'umtantondhsalmlsneneaeeeuitgvmenooftllvdaedgmfaustwanoeneeestuanhiioetetreuyoiiinavbrlashkaroeoaeniatiiexehlftmoohmsdaillsrtsbthskhiethmbtefrwoiliioivtertisraeplitiepmcsemidesdtsehteitowwrntarkbgntiylnttatvheeoacboosdullgpgodvhonansnsixoyttyruecsutaoaeoneninadnhveframoienewewnnsrneoudnutniuwcticaepiguogiiotmettwoymgsdbnfrarneteiigkuihddeekeotaekbatokgovgnsrahtlgerctuerswrnoonmoagaatenaeeminamrbhdchnnrarioyoeuraambineimoiaotileidrteeouitvhnraffoveacyimodaaseiassafoyedoisigroansliwnitebienfrkmillhfeokeocnriipiomthanriwhskeruagiedtmpnslrsortlolerunsbdtokgnsgeeeihfaunagwaeaoityetblsgnyeneeqinhxnrn'
cipherText2 = 'vasxfeafnzelmgkfsiwpuekyvyvvgjsehxeuqrefvehtukuxntzvkzrdvlgcfpfnouauvwrtzdtsfymlmgyvorvgsjsfwjyvrkfkuvlawltuuqucrzmjbmgghunhebnkhtvfmhqfebjdfvkkkvuxznazarycgjknlpasjwdyjcyzfidkubmikuhqpuivezeqxztltbxcugzfsyngztwplnlggfwhelhtthtcuzmbgyxuvlbqffywecfkydwvkrvkfyythgyvoibzqgkeiolgnefqratskgzqndbblccirzqglaoaxcfkrjvftmfdquayzefdsyrfawlzyeplpriqpgadoxalfllqzesfgadhmfoapqvkytjzhrvgrnqpneflacrbmnarylzgrjwqfzfhumzxncmgreczazhvzuhtduvurmerbfpgduwnytzmdjbgdcdmlpplnexdfsiqqtmvrwcgzvrnvekpgfucthljgdtxodtqofxdygfftiibrkgzvuznblksyrzkqjkioebrnfqcqtmfdquepiacpzdnkfkfnsfscpyndjrxsjwnfxenvdvhjgadijqucabljzbzng'
cipherText3 = 'tpkypmxcarbnzalharzczoecutunnoirshinnucsolfrkymttkphnghboilsxcrhsnrcpoquirepazpmzlfspnundozdimahuxancplroncopoazlzxqnuutuxdnaehamtdupozshrsezlkrakgzxezhbnzaoasxfoxorftepmdozdimazinnuorgehaepazinunpctduiaezklharylzkoarhabechzgzxuxcgpraxtpeaogpzlkrnkreqnoitsgnkfzmgzcnraxtecftarazepdxraeoxmheirorhbtkaheongeqcsscqtaziueppnopoitnpwnmsnroxezofchpucmtksnhabngaznuirarzcpoaflalrsefclrkwpoodbnmtpemyhautfopzfiutuxscxqirpozoslozrhfoaflaodbnutqxsqhsurepknekundtzoanlypohpmcrutnpwlroeisubolxqnuutopcporuiazepdnhfhenmdeehdotevmxtgdratroxutyparfqesehirzktikzcnrahadteqesnqaecsodexsedrxsxepyxtoiutnftniamzmpitng'
cipherText4 = 'icgbgulkevgogqiuekkestbsgwwgbigpbllpuvfensuicpweezedtetgkipbylwykglligpblpbgkeiicgekwyqbeedledvulibgllkebicgngliekglyeapbgcgbgdebnaipkuklipkipkvyeatalikiipzgyeablgwdieelgbuealwysgtalicpxguvgpwlpkvibyiewuxgaqieicgtgxgkudsgkgxgbrauiglaooggvwudgseawvngplebbynalukgllsuiceaiicgtsuicicgtuiljbpkvpkvjbgpisebvllpuvicgcelipiwgkjiculseblgknawwgilyeakgxgbzkesscpiicgywwcuiwuxgpwwyeaopkuilptulipzgkeiieuiveglkiletaoctpiigbscpiyeaveukqpbiuoawpblewekjplyeacpxgyeabwudgudyeacpxgkicpvicpiscpicpxgyeacpvtpvkgllukjbgpiekgltalikeiakspiocvjeiaiiaiocuwvlpuvicgvaocgllgxgbyicukjljeiptebpwudekwyyeaopkdukvuim'
cipherText5 = 'kmgbdtuuzhkjpgfkadodxlqyirztmwaxwgwdmtuvdpatfjzguxcnjkqauvnladcxpfhsjknachvbwdifjexuispbyoynykmtzfnadgnyqauvrfoqqpyqkwmhdpytaxhuvuvtleadvhvotceugpuvyoexmicnqhjggkfnkwnlzfrsjcrzytaxgkddaepkhwngnyadkzwpjhiphsfsrrvoxuooanvbhvvmtuikqaumzfrugcrrjmakhsyauseowsgbglujjxadkajroxvbrqruqanyhsqwgbgyuyzfaeeomvsrpbzgxwynlwynfsyznlaqzfdcusfgrkdjfkhsqwvuoxeewdgigscnpwqyzfzgkubvaenlnamncnpwqyzfimefqpxummdcerizwgujphimwdgygxaxwghvgcxwersrancxqehayogbynspoygyhsqwytatfjadytatwdtvhsnyxwzfaejxadkajritnrjewcyzqpzfdczigfwgodzschqvbigyyjsyumoqqeqgisrzagphdirawunahaagipmjifqwqhpkzfdctijmiswtnycnqpdgbsuvhjbisoqvgxin'

cipherArray = [cipherText1,cipherText2,cipherText3,cipherText4,cipherText5]

# Go through ciphertext and add when characters are met
for i in range(len(cipherArray)):
    # Split the two character ciphers into an array and move to an empty dictionary
    cipherTextArray = cipherArray[i]
    split = 2
    splitCipherArray = [cipherTextArray[x:x+split] for x in range(0, len(cipherTextArray), split)]
    frequencyCounter = dict.fromkeys(splitCipherArray, 0)
    # Go through the two character arrays and count the frequency of the pairs. 
    for digraph in splitCipherArray:
        if digraph in frequencyCounter:
            frequencyCounter[digraph] += 1
        else: 
            frequencyCounter[digraph] = 0

    # Sort and print the frequency of the two characters. 
    def dictValue(count):
        return count[1]
    print("Cipher Text" + str(i+1) + '\n' + str(sorted(frequencyCounter.items(), key=dictValue)) + '\n')