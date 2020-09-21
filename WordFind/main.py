from collections import Counter


def find(min_len, max_len, letters):

    result = []

    with open('words-da.txt') as word_list:
        for word in word_list:
            word = word.strip()
            cond = all(i in letters for i in word)
            if min_len <= len(word) <= max_len and cond:
                result.append(word)
    #print(result)

    indexes = []

    for index, word in enumerate(result):
        frequency = Counter(word)

        for key in frequency.keys():
            if frequency.get(key) > 1:
                #print(f'word: {word} + index: {index}, {key}+{frequency.get(key)}')
                indexes.append(index)

    indexes = list(dict.fromkeys(indexes))

    for x in sorted(indexes, reverse=True):
        del result[x]

    return result


if __name__ == '__main__':

    try:

        print('## WORD FIND CHEAT V1.0 ##')

        while True:

            characters = []

            while True:

                char = input('enter character: ')

                if char == '':
                    break
                else:
                    characters.append(char)

            min_lenght = int(input('enter min length of word: '))
            max_lenght = int(input('enter max length of word: '))

            print(f'\n'
                  f'# Characters chosen: {characters}\n'
                  f'# Min length of word: {min_lenght}\n'
                  f'# Max length of word: {max_lenght}\n')

            words = find(min_lenght, max_lenght, characters)

            print(f'Usable words: {words}')

            input()

            print('## Next Round! ##')

    except KeyboardInterrupt:
        pass