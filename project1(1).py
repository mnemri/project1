def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    max2 = 0
    max3 = 0
    max4 = 0
    max5 = 0
    for word in words:
        if len(word) == max_len: word1 = word
    for word in words:
        if (max2 < len(word)) and word != word1:
            max2 = len(word)
            word2 = word
        if (max3 < len(word)) and word != word1 and word != word2:
            max3 = len(word)
            word3 = word
        if (max4 < len(word)) and word != word1 and word != word2 and word != word3:
            max4 = len(word)
            word4 = word
        if (max5 < len(word)) and word != word1 and word != word2 and word != word3 and word != word4:
            max5 = len(word)




    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u''U', 'y', 'Y']

    for word in [word1, word2, word3, word4]:
        string = word;
        for x in string.lower():
            if x in vowels:
                word = word.replace(x, "")
        print(word[::-1])


longest_words('ye.txt')