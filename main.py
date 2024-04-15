user_input = input("Indtast sætningen: ")  # Getting the sentence
sentence = user_input.split()  # Making it into a list
sentence_length = len(sentence)
checked = 0  # How many letters it has checked
point = 0  # to keep track of how many times it matched
biggest_point = 0  # The number of points the next word needs to beat before it is a better match
biggest_match = ""



def getLetter(checked, point):
    global biggest_point, biggest_match
    with open("data.txt", "r") as file:
        content = file.readlines()
        while checked < len(content):
            data_line = content[checked].strip()
            print("Comparing with line:", data_line)
            for word, data_word in zip(sentence, data_line.split()):
                for letter, data_letter in zip(word, data_word):
                    if letter == data_letter:
                        print("match", letter, data_letter)
                        point += 1
                        print("adding point ", point)
            if point > biggest_point:
                biggest_point = point
                biggest_match = data_line
                print("Current best match:", biggest_match)
                point = 0
                checked += 1
            else:
                checked += 1
                point = 0


getLetter(checked, point)

print("Matched ", biggest_match, "with ", biggest_point)
