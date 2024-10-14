import ex_03_10_2022180007_2 as qs

def selection(arr, start, end, nth):
    pi = qs.partition(arr, start, end)
    ss = pi - start
    if ss == nth - 1:
        return arr[pi]
    elif ss > nth - 1:
        return selection(arr, start, pi - 1, nth)
    elif ss < nth - 1:
        return selection(arr, pi + 1, end, nth - ss - 1)

def main():
    print(qs.words)
    print(qs.partition)

    ranks = [ 5, 12, 63, 77, 93 ]
    last_word_index = len(qs.words) - 1
    for rank in ranks:
        words = qs.words[:]
        word = selection(words, 0, last_word_index, rank)
        print(f'{rank=} {word=}')

if __name__ == '__main__':
    main()