import base64
import json


def encodeLZSS(dlen, blen, inp):
    check = 0
    dic = list("$" * dlen)
    buff = list(inp[:blen])
    inp = list(inp[blen:])
    out = []
    while inp:
        for i in range(len(dic)+1):
            if len(buff) > 0 and i < len(dic) and dic[i] == buff[0]:
                bufftemp = i
                curdic = bufftemp
                leng = 1
                for j in range(1, len(buff)):
                    curdic = curdic + 1
                    if curdic < len(dic) and buff[j] == dic[curdic]:
                        leng += 1
                    else:
                        break
                out.append([1,i,leng])
                for j in range(leng):
                    if len(dic) > 0:
                        dic.pop(0)
                    if len(buff) > 0:
                        dic.append(buff[0])
                        buff.pop(0)
                    if len(inp) > 0:
                        buff.append(inp[0])
                        inp.pop(0)
                check = 1
            if check == 1:
                check = 0
            else:
                if len(dic) > 0:
                    dic.pop(0)
                if len(buff) > 0:
                    out.append([0, buff[0]])
                    dic.append(buff[0])
                    buff.pop(0)
                if len(inp) > 0:
                    buff.append(inp[0])
                    inp.pop(0)

    mess = ""
    for tuple in out:
        mess += str(tuple[1])
    return mess


# recursively encoding the characters using Shannon-Fano method
def codeget(chanses: list, codeList: list, L, R):
    if R - L > 1:
        sum0 = 0
        sum1 = 0
        counter = 0

        # dividing them in groups according to their probability
        # One group has nulls and the other has ones
        for i in range(L, R):
            sum1 += chanses[i][0]

        for i in range(L, R):
            el = chanses[i][0]
            if sum0 < sum1:
                sum0 = sum0 + el
                sum1 = sum1 - el
                counter += 1
            else:
                break

        for i in range(L, L + counter):
            codeList[i][1] = codeList[i][1] + '0'

        for i in range(L + counter, R):
            codeList[i][1] = codeList[i][1] + '1'
        codeget(chanses, codeList, L, L + counter)
        codeget(chanses, codeList, L + counter, R)

    if R - L == 0:
        if L != len(codeList):
            codeList[L][1] = codeList[L][1] + '0'


def encodeFano(file):

    # counting how many times each character appears
    letCounter = {}
    countlet = 0
    text = []

    for lines in file:
        for i in lines:
            text.append(i)
            if set(i) <= set(letCounter.keys()):
                letCounter[i] += 1
            else:
                letCounter.update({f'{i}': 1})
            countlet += 1


    # counting the probability of each character
    letChance = {}
    for key in letCounter.keys():
        letChance.update({f'{key}': letCounter.get(key) / countlet})


    # rounding the probability of each character
    letChanceList = []
    for key in letChance.keys():
        letChanceList.append((round(letChance.get(key), 8), key))


    # sorting the list of probabilities
    letChanceList.sort()
    letChanceList.reverse()


    for tuple in letChanceList:
        print(tuple)


    # adding the characters to a new list
    letCodes = []
    for i in range(len(letChanceList)):
        letCodes.append([letChanceList[i][1], ''])


    # generating codes
    codeget(letChanceList, letCodes, 0, len(letCodes))

    # stopped here
    firstCodedText = ''
    for i in text:
        for j in letCodes:
            if i == j[0]:
                firstCodedText = firstCodedText + j[1]

    firstCodedText = firstCodedText + '@'

    for i in letChanceList:
        tmp = str(i[0]).replace('0.', '')
        if len(tmp) < 9:
            for j in range(9 - len(tmp)):
                tmp += '0'
        firstCodedText = firstCodedText + i[1] + tmp
    return firstCodedText


# converting the string into bits
def b_encode(file):
    with open(file, 'rb') as f:
        binar = base64.b64encode(f.read())
        f.close()
    return binar


if __name__ == "__main__":
    # encoding a picture
    # dictSize = 280
    # bufferSize = 100
    # bibib = b_encode("../files/pic.bmp")
    # b = bibib.decode("UTF-8")


    # encoding MyMy
    dictSize = 400
    bufferSize = 200
    text_bits = b_encode("../files/MyMy.txt")
    text_utf = text_bits.decode("UTF-8")


    # with open("../files/message_encoded.json", 'w') as f:
    #     compStr = LZSS(dictSize, bufferSize, Fano(text_utf))
    #     # compStr = LZSS(dictSize, bufferSize, Fano(b))
    #     json.dump(compStr, f)


    with open("../files/message_encoded.json", 'w') as f:
        compStr = encodeLZSS(dictSize, bufferSize, text_utf)
        str_fano = encodeFano(text_utf)
        # compStr = LZSS(dictSize, bufferSize, Fano(b))
        json.dump(str_fano, f)
