import json
import base64
import io
import re
from PIL import Image
import sys
sys.setrecursionlimit(15000)


def decode_76(data, altchars=b'+/'):
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


def codeget(chanses: list, codeList: list, L, R):
    if R - L > 1:
        sum0 = 0
        sum1 = 0
        counter = 0

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


def decodeLZSS(dlen, file_path):
    with open(file_path, 'r') as f:
        compstr = json.load(f)
    dic = list("$" * dlen)
    outdec = ""

    for i in range(len(compstr)):
        if compstr[i][0] == 0:
            dic.append(compstr[i][1])
            dic.pop(0)
            outdec += str(dic[len(dic)-1])
        elif compstr[i][0] == 1:
            curdic = dic[compstr[i][1]:]
            curdic = curdic[:compstr[i][2]]
            for j in range(len(curdic)):
                outdec += curdic[j]
                dic.pop(0)
                dic.append(curdic[j])
    return outdec


def decodeFano(dtext):
    for i in range(len(dtext)):
        if dtext[i] == '@':
            chance = i

    let_chance_temp = []
    let_code = []
    let_chance_list = []
    reader = chance + 1
    while reader < len(dtext):
        temp_toAp = []
        temp_toAp.append(dtext[reader])
        reader += 1
        tmp = ''
        for i in range(9):
            tmp += dtext[reader]
            reader += 1
        temp_toAp.append(tmp)
        let_chance_temp.append(temp_toAp)

    for i in let_chance_temp:
        if i[1].isnumeric() == True:
            let_chance_list.append([float('0.' + i[1]), i[0]])
        else:
            let_chance_list.append([float(i[1]), i[0]])

    for i in range(len(let_chance_list)):
        let_code.append([let_chance_list[i][1], ''])

    codeget(let_chance_list, let_code, 0, len(let_code))

    final_out = ''
    buf = ''
    for i in range(len(dtext)):
        buf += dtext[i]
        for j in let_code:
            if buf == j[1]:
                final_out += j[0]
                buf = ''
    return final_out


if __name__ == "__main__":
    # decoding a picture
    # dictSize = 280
    # dec = decompressFano(LZSS(dictSize))
    #
    # b = decode_76(dec.encode("UTF-8"))
    #
    # imag = Image.open(io.BytesIO(b))
    # imag.show()


    # decoding MyMy
    # dictSize = 400
    # dec = decompressFano(LZSS(dictSize))
    #
    # b = decode_76(dec.encode("UTF-8"))
    # with open("../files/text_decoded.txt","wb") as f:
    #     f.write(b)


    # testing
    dictSize = 400
    file_name = "../files/message_encoded.json"
    dec = decodeFano(decodeLZSS(dictSize, file_name))

    b = decode_76(dec.encode("UTF-8"))
    with open("../files/text_decoded.txt","wb") as f:
        f.write(b)