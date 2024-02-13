user_input = input()  # Getting the sentence
sentence = user_input.split()  # Making it into a list
sentence_length = len(sentence)
checked = 0  # How many letters it has checked
point = 0 # to keep track of how many times it matched
biggest_point = 0 #The number of points the next word needs to beat before it is a better match
biggest_match = ""
def getLetter(checked, point):
    global data_line, biggest_point, biggest_match
    for word in sentence:
        checked = getLine(checked)

        for letter, data_letter in zip(word, data_line):
            if letter == data_letter:
                print("match", letter, data_letter)
                point += 1
                if point >= biggest_point:
                    print("Line ", data_line)
                    biggest_match = data_line
                    biggest_point = point
                    


def getLine(checked):
    global data_line
    with open("data.txt", "r") as file:
        content = file.readlines()
        data_line = content[checked]
        print(data_line)
        return checked + 1


getLetter(checked, point)

print("Matched ", biggest_match, "with ", biggest_point)
