import sys
import threading
sys.setrecursionlimit(1000000000)
threading.stack_size(200000000)


Code = []
file = open("../files/MyMy.txt", encoding='utf8')
text = file.read().lower()
file.close()
d = {}
for i in text:
    if i not in '!—,.-?...()—:;«»\nъь':
        d[i] = d.get(i, 0) + 1
sum_sim = sum(d.values())
for i in d:
    d[i] = round(d[i] / sum_sim, 5)
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(d)
arr = []
for i in d:
    arr.append(list(i) + [''])
print(arr)
def func(arr):
    half = sum(map(lambda x: x[1], arr))
    sum1 = 0
    for i, j in enumerate(arr):
        sum1 += j[1]
        if sum1 * 2 >= half:
            index = i + (abs(2 * sum1 - half) < abs(2 * (sum1 - j[1]) - half))
            break

    arr0, arr1 = [], []
    for i in arr[:index]:
        i[2] += '0'
        arr0.append(i)
    for i in arr[index:]:
        i[2] += '1'
        arr1.append(i)

    if len(arr1) == 1:
        Code.append(arr1)
    else:
        func(arr1)
    if len(arr0) == 1:
        Code.append(arr0)
    else:
        func(arr0)


func(arr)
STR = ''
for i in Code:
    print(i)
    STR +=str(i) + ' '
print(STR)

f = open('text2.txt', 'w', encoding ='utf-8')
f.write(STR)
f.close()


def LZ78(phraseA):
    lofKod = [0]
    phraseA = list(phraseA)
    # print(phraseA)
    phraseA.insert(0,0)
    phrase=[]
    j = 1
    k = 0
    while(k < len(phraseA)):
        i = phraseA[k]
        if(i == "/"):
            break

        if(i not in phrase):
            lofKod.append([0,i])
            phrase.append(i)
            k += 1
        else:
            s = i
            pos = 0

            while(s in phrase):
                while (s != phrase[pos]):
                    pos += 1
                k += 1
                if(k == len(phraseA)): break
                i = phraseA[k]
                s += i
            k+=1
            if (k > len(phraseA)): break
            lofKod.append([pos,i])
            phrase.append(s)
            # print(phrase)

    del lofKod[1]
    return lofKod
v = open('C:\\Users\\Admin\PycharmProjects\pythonProject10\\venv\coding\\codonSh.txt','r', encoding='utf-8')
vr = v.read()
v.close()
# print(vr)
test1 = LZ78(vr+' ')
# print(test1)
fus = open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\ls78.txt', 'w',encoding='utf-8')
fus.write(str(test1))
fus.close()
# exit()

def LZ78_Dec_math(z='', i=1, b='', level=0):
    global test1
    # print(level, len(z))
    if(test1[i][0] == 0):
        z += test1[i][1]
        i += 1
        z += b[::-1]
        return z
    else:
        b += test1[i][1]
        return LZ78_Dec_math(z, test1[i][0], b, level + 1)

def LZ78_Dec():
    global test1
    z = ''
    count = len(test1)

    for i in range(1, count):
        z += LZ78_Dec_math(i=i)

    return z
z = LZ78_Dec()

with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\back.txt','w', encoding = 'utf-8') as f2:
     f2.write(z)
print(z)
# print(len(z))

with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\back.txt', 'r', encoding='utf-8') as fp:
    s = (sum(1 for _ in fp))

with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\back.txt', 'r', encoding='utf-8') as fp:
    print(s)
    line = fp.readlines()[1: s]
    listofD = []
    # print(line)
    for i in line:
        c = i[1:len(i)-2]
        c1 = c.split(',')
        buff = c1[0]
        c1[0] = buff[1:len(buff)-1]
        buff2 = c1[2]
        c1[2] = buff2[2:len(buff2)-1]
        if len(c1) == 4:
            c1 = c1[1:len(c1)]
            c1[0] = ','
            buff2 = c1[2]
            c1[2] = buff2[2:len(buff2) - 1]
        listofD.append(c1)


# print(listofD[1][1])

with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\back.txt', 'r', encoding='utf-8') as fp:
    lenofdoc = fp.readlines()[0:1]
    lenofdoc = lenofdoc[0]
    lenofdoc = list(lenofdoc)
    del lenofdoc[len(lenofdoc)-1]
    # print(lenofdoc)

blu = ''
FINAL =''
j = 0
for i in lenofdoc:
    blu += i
    for j in range(len(listofD)):
        so = listofD[j][0]
        if blu == listofD[j][2]:
            if listofD[j][0] =='\\n':
                FINAL += '\n'
            else:
                FINAL += so
            blu =''
f = open('C:\\Users\\Admin\\PycharmProjects\\pythonProject10\\venv\\coding\\final.txt','w',encoding='utf-8')
f.write(FINAL)
f.close
print(FINAL)