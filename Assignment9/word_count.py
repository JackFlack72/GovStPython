import os

def main():
    # Automatically get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Prompt user for the filename
    filename = input('Enter the name of the input file (e.g., text.txt): ')
    
    # Join the script's directory with the filename
    file_path = os.path.join(script_dir, filename)
    
    try:
        infile = open(file_path, 'r')
        text = infile.read()
        infile.close()
    except FileNotFoundError:
        print(f"The file '{filename}' was not found in {script_dir}.")
        return

    # Split the text into a list of words based on whitespace
    words = text.split()
    
    # Create a dictionary to store word occurrences
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    # Print formatted output table
    print(f"\n{'Word':<15} | {'Occurrences'}")
    print("-" * 30)
    
    for word, count in word_counts.items():
        print(f"{word:<15} | {count}")

if __name__ == '__main__':
    main()