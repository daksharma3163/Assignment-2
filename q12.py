from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

word_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagram_groups = group_anagrams(word_list)


for group in anagram_groups:
    print(group)
