#--------------------------
#Name:Aybüke YALÇINER.
#--------------------------
import sys



file=open(sys.argv[1],"r")
sozluk={}


for line in file.readlines():
    line=line.rstrip('\n')
    sozluk_items=line.split(' ')
    sozluk[sozluk_items[0]]=sozluk_items[1:]


file2=open(sys.argv[2],"r")
file3=open("binarian_message.txt","w")
binarian_to_english_text=file2.readlines()


liste=[]
liste2=[]
def binarian_to_english(binarian_to_english_text):
    for i in binarian_to_english_text:
        i=i.rstrip('\n')
        i=i.split(',')
        for j in i:
            j=j.split(' ')
        liste.append(j)


    for k in liste:
        if k[0]!="+" and k[0][0]!="#":
            liste2.append(k)

    for listex in liste2:

        for w in listex:
            if w in sozluk:
                print(sozluk[w][0],end=' ',sep=' ')
                file3.write(sozluk[w][0]+' ')
            elif not w in sozluk:
                print(w,end=' ',sep=' ')
                file3.write(w+' ')
        print(end='\n')
        file3.write('\n')

binarian_to_english(binarian_to_english_text)



print( )

def format_e(n):
    a = '%e' % n
    return a.split('e')[0].rstrip('0').rstrip('.') + 'e' + a.split('e')[1]



a="Data about Binarian planet:"
distance=0
decimal1=0
decimal2=0

for i in liste:
    if i[0]=="+":
        for k in i:
            if not k in sozluk:
                pass
            elif sozluk[k]==['distance', '(n)']:
                binary = i[2]
                decimal=0
                for digit in binary:
                    decimal = decimal*2 + int(digit)
                ly=9.4607e+12
                distance=decimal*ly
                distance=format_e(distance)




            elif sozluk[k]==['temperature', '(n)']:
                binary = i[2]

                for digit in binary:
                    decimal1 = decimal1*2 + int(digit)

            elif sozluk[k]==['orbital-speed', '(n)']:
                binary = i[2]

                for digit in binary:
                    decimal2 = decimal2*2 + int(digit)
            else:
                pass
x="Distance from the Earth: {} km".format(distance)
y="Planet temperature: {} degrees Celsius".format(float(decimal1))
z="Orbital speed: {} km/s".format(float(decimal2))
print(a)
print(x)
print(y)
print(z)
file4=open("computations.txt","w")
file4.write(a+'\n' + x+'\n' +y+'\n'+z)
print( )
reverse_sozluk={}
for key, value in sozluk.items():
    key1=value[0]
    value1=key
    reverse_sozluk[key1]=value1

file5=open(sys.argv[3],"r")
file6=open("message.txt","w")
english_to_binarian_text=file5.readlines()

high_character=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","W"]

binstr2=""
liste3=[]
liste4=[]
bin=[]
def dec_to_bin(n):
    bits = []

    bits.append(str(0 if n%2 == 0 else 1))
    while n > 1:
        n = n // 2
        bits.append(str(0 if n%2 == 0 else 1))

    bits.reverse()
    return ''.join(bits)
def english_to_binarian(english_to_binarian_text):
    for line in english_to_binarian_text:
        line=line.rstrip('\n')
        line=line.rstrip(' ')
        line=line.rstrip(',')

        if ',' or '.' or '?' or '!'in line:
            line=line.replace(',','')
            line=line.replace('.','')
            line=line.replace('?','')
            line=line.replace('!','')
        liste3.append(line)

    for word in liste3:
        word=word.split(' ')
        liste4.append(word)




    for listex in liste4:

        for w in listex:
            if not w.isalpha():
                w=dec_to_bin(int(w))
                print(w,end=' ')
                file6.write(str(w) +' ')
            else:
                if w[0] in high_character:
                    if w.lower() in reverse_sozluk:
                        print(reverse_sozluk[w.lower()],end=' ',sep=' ')
                        file6.write(reverse_sozluk[w.lower()]+' ')
                    else:
                        print(w,end=' ',sep=' ')
                        file6.write(w+' ')
                elif not w in reverse_sozluk:
                    print(w,end=' ',sep=' ')
                    file6.write(w+' ')
                elif w in reverse_sozluk:
                    print(reverse_sozluk[w],end=' ',sep=' ')
                    file6.write(reverse_sozluk[w]+' ')

                else:
                    pass
        print(end='\n')
        file6.write('\n')
english_to_binarian(english_to_binarian_text)









file.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
