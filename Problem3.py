def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return -1
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
        return -1

print(count_words_in_file("test.txt"))

