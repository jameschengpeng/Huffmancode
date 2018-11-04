class node:
    def __init__(self, name, pos, freq):
        self.name = name
        self.pos = pos
        self.freq = freq
        self.left = None
        self.right = None

def stat(freqbook, filename): #freqbook is a dict that stores all characters from filename and their frequencies
    istream = open(filename, "r")
    for line in istream:
        for ch in line:
            if ch in freqbook:
                freqbook[ch] += 1
            else:
                freqbook.update({ch:1})
    istream.close()

def put_in_list(freqbook, nodelist): # put every character in the freqbook into nodelist
    for item in freqbook:
        character = node(item,"0",1)
        nodelist.append(character)

def huff(nodelist,hufflist): #nodelist contains all "leaves", hufflist contains the huffman tree
    nodelist = sorted(nodelist, key=lambda node: node.freq) #nodelist is sorted by freq in ascending order
    while (len(nodelist) != 1):
        L = nodelist[0]
        R = nodelist[1]
        R.pos = "1"
        bond = node((L.name+R.name),"0",(L.freq+R.freq))
        bond.left = L
        bond.right = R
        if L not in hufflist:
            hufflist.append(L)
        if R not in hufflist:
            hufflist.append(R)
        if bond not in hufflist:
            hufflist.append(bond)
        del nodelist[0]
        del nodelist[0]
        nodelist.append(bond)
        nodelist = sorted(nodelist, key=lambda node: node.freq)

def encodemsg(hufflist,msgbook,freqbook): #msgbook is a dict to store the huffman code of all characters
    sorted(freqbook)
    hufflist = sorted(hufflist, key=lambda node: len(node.name))#sort the hufflist by length of the "name"
    for char in freqbook:
        root = hufflist[-1]  # root must be the last element of hufflist
        msgbook[char] = ""
        while char in root.name:
            msgbook[char] += root.pos
            if root.left == None:
                break
            elif char in root.left.name:
                root = root.left
            else:
                root = root.right
    istream = open("encodemsg.txt", "w")
    prev = ""
    sum = 0
    for item in msgbook:
        sum += len(msgbook[item])
        if ((prev < "a") and (item >= "a")) or ((prev < "A") and (item >= "A")):
            istream.write("..............." + '\n')
        istream.write(item + ": " + msgbook[item] + '\n')
        prev = item
    num = len(freqbook)
    istream.write("Ave = " + str(float(sum/num)) + " bits per symbol" + '\n')
    istream.close()

def encode(msgbook):
    ostream = open("code.txt", "w")
    fin = open("input_file.txt", "r")
    str = ""
    for line in fin:
        for ch in line:
            str += msgbook[ch]
    counter = 0
    for i in str:
        if counter <= 79:
            ostream.write(i)
            counter += 1
        else:
            counter = 0
            ostream.write('\n')
            ostream.write(i)
            counter += 1
    fin.close()
    ostream.close()



freqbook = {}
filename = input("Enter the file name: ")
stat(freqbook,filename)
nodelist = []
hufflist = []
put_in_list(freqbook,nodelist)
huff(nodelist,hufflist)
msgbook = {}
encodemsg(hufflist,msgbook,freqbook)
encode(msgbook)


