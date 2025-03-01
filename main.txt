def start():
    # Split the prompt into words.
    prompt = "hello there".split()
    
    # This will hold the best match for each prompt word.
    best_matches = []

    # Open and read the file "Stories.txt".
    with open("Stories.txt", "r", encoding='utf-8') as file:
        content = file.read().split()
    
    # For each word in the prompt, find the best matching word in the file.
    for pword in prompt:
        best_score = float('inf')  # Start with a very high (worst) score.
        best_match = None
        
        for word in content:
            # Only compare words with the same length as the prompt word.
            if len(word) != len(pword):
                continue
            
            # Count matching letters between the file word and the prompt word.
            points = 0
            for letter in word:
                for letter2 in pword:
                    if letter == letter2:
                        points += 1
            
            # Calculate the matching score:
            # Lower 'mn' means more matching letters (given: mn = len(word) - points - len(pword)).
            mn = len(word) - points - len(pword)
            
            # If this word has a score lower than (or equal to) our best score, update the best match.
            if mn <= best_score:
                best_score = mn
                best_match = word
        
        # Save the best matching word for this prompt word.
        best_matches.append(best_match)
    
    print("Best matches:", best_matches)

# Execute the function.
start()
