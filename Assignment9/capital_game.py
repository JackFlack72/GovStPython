import random

def main():
    # Dictionary mapping states to their capitals (15 states included)
    capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis'
    }
    
    correct_count = 0
    incorrect_count = 0
    
    # Get a list of the states from the dictionary keys
    states = list(capitals.keys())
    
    while True:
        # Randomly select a state
        state = random.choice(states)
        correct_capital = capitals[state]
        
        # Prompt the user for the capital
        user_answer = input(f"What is the capital of {state}? (or enter 0 to quit): ")
        
        if user_answer == '0':
            break
            
        # Check if the user's answer matches (case-insensitive)
        if user_answer.strip().lower() == correct_capital.lower():
            print("That is correct.")
            correct_count += 1
        else:
            print("That is incorrect.")
            incorrect_count += 1
            
    # Print final summary
    print(f"You had {correct_count} correct responses and {incorrect_count} incorrect responses.")

if __name__ == '__main__':
    main()