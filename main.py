word_i = input("tyoe: ")
e_word = ["haj", "hej", "hejsa"]
c_word = e_word[0]
runned = 0
iw = len(c_word)
cw= len(word_i)
a_1 = 0
b_1 = 0
point = 0
n = -0
biggest =  ""
biggest_point = (0)
l_e_word = len(e_word)



def notSameRange_in():
    global runned
    global o
    global b_1
    global n
    global c_word


    b_1 = 0

    if iw <= cw:
        o = iw
    else:
        o = cw  
    runned += 1

    
    if runned <= o:
        run()
    else:
        changeText()
        return

def run():
    global a_1
    global b_1
    global point
    for x in range(o): 
        if a_1 < o:
            y = c_word[a_1]
        else:
            a_1 = 0
            changeText()
            return

        z = word_i[b_1]
        b_1 += 1
        if y == z:
            print("Match")
            point += 1
        else:
            print("notmatch")
    if a_1 <= o:
        a_1 += 1
    else:
        a_1 = 0
        changeText()
        return
    notSameRange_in()
        
        

    



def changeText():
    global biggest_point
    global runned
    global o
    global b_1
    global n
    global c_word
    global a_1
    global point
    global biggest

    if biggest_point < point:
        biggest_point = point
        print(e_word)
        print(a_1)
        biggest = e_word[n]
        print(biggest)
    u = n + 1
    if l_e_word > u:
        print("changing text")
        n += 1
        c_word = e_word[n]
        runned = 0
        iw = len(c_word)
        cw= len(word_i)
        a_1 = 0
        b_1 = 0
        point = 0

        if iw <= cw:
            o = iw 
        else:
            o = cw  

        run()
    else: print("Done")


notSameRange_in()

print("match", biggest)