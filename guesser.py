# Grok’s Number Guesser - Угадай число
def number_guesser():
    print("Welcome to Grok’s Number Guesser!")
    print("Think of a number between 1 and 100.")
    input("Press Enter when ready...")
    
    low, high = 1, 100
    attempts = 0
    
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"Is your number {guess}?")
        response = input("Enter 'h' (higher), 'l' (lower), or 'y' (yes): ").lower()
        
        if response == 'y':
            print(f"Got it in {attempts} attempts!")
            break
        elif response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
    
    print("\nLike it? Support me: https://boosty.to/grokcode/donate")

if __name__ == "__main__":
    number_guesser()
