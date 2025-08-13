def file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_chars, num_words, num_lines

filename = "example.txt"
chars, words, lines = file_stats(filename)
print(f"Characters: {chars}, Words: {words}, Lines: {lines}")
