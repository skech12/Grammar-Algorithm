# Define the main function that starts the program.
def start():
    # Take input from the user, split it into words, and convert each word to lowercase.
    prompt = [p.lower() for p in input("Type: ").split()]
    
    # Define a list of words to remove from the input (common filler words).
    listToRemove = ["how", "can", "i"]
    for x in listToRemove:
        if x in prompt:
            prompt.remove(x)
    
    # Initialize an empty list to store the best matching words.
    best_matches = []

    # Open the file "Stories.txt" and read its content. Then split it into a list of words.
    with open("Stories.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
    
    # Convert all words in the content to lowercase for case-insensitive comparison.
    content = [word.lower() for word in content]

    # Iterate over each word in the user input prompt.
    for pword in prompt:
        best_score = float('inf')  # Initialize the best score as infinity.
        best_match = None  # Initialize the best match as None.
        
        # Compare the user word with each word in the file content.
        for word in content:
            # Only compare words that have the same length.
            if len(word) != len(pword):
                continue
            
            # Calculate the number of matching letters at the same position.
            points = sum(1 for letter, letter2 in zip(word, pword) if letter == letter2)
            
            # Compute the score as the total length minus the number of matching letters.
            # Lower score means a closer match.
            score = len(word) - points
            
            # Update the best match if the current score is lower than the previous best.
            if score < best_score:
                best_score = score
                best_match = word
        
        # Append the best matching word for this prompt word to the list.
        best_matches.append(best_match)
    
    # Print out the best matches found.
    print("Best matches:", best_matches)
    
    # Call the function 'findPrompt' with the list of best matches.
    # Note: 'findPrompt' should be defined elsewhere in your code.
    findPrompt(best_matches)

# Start the program by calling the 'start' function.
start()
