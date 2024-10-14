import random

words = [
    '2022180007', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 
    'somebody', 'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 
    'prosy', 'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 
    'rabbi', 'enmity', 'loft', 'temporize', 'speedboat', 'agenda', 'delusion', 'addle', 'idolize', 'romance', 
    'overestimate', 'revive', 'smell', 'quite', 'seminar', 'bloomers', 'lives', 'innocuous', 'effluent', 
    'cross', 'recidivist', 'wet', 'synth', 'mantilla', 'tweak', 'lowbrow', 'aviation', 'quadruped', 'capable', 
    'graphic', 'barman', 'intemperate', 'mastermind', 'submit', 'considering', 'riddance', 'polyethene', 'jim', 
    'varicolored', 'medic', 'ferric', 'minaret', 'capacitor', 'pusher', 'gingerbread', 'grizzled', 'upsilon', 
    'km', 'glade', 'ribbon', 'parascending', 'shinty', 'breve', 'hotel', 'similitude', 'fuddle', 'secretariat', 
    'silicate', 'whinchat', 'abstention', 'untrue', 'toing', 'cnd', 'ramification', 'scorn', 'apricot', 
    'arnica', 'militate', 'muslim', 'homicide', 'overfeed', 'shooting', 'growth',
]

def insertionSort(arr, left, right):  # right=inclusive
    for i in range(left + 1, right + 1):
        v = arr[i]
        j = i - 1
        while j >= left and arr[j] < v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

def quickSort(arr, left, right):  # right=inclusive
    size = right - left + 1
    if size <= 1:
        # insertionSort(arr, left, right)
        return
    pivot_index = partition(arr, left, right)
    quickSort(arr, left, pivot_index - 1)
    quickSort(arr, pivot_index + 1, right)

def partition(arr, left, right):  # right=inclusive
    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]  # pivot 설정
    pivot = arr[left]
    p = left + 1
    q = right

    while True:
        while p <= right and arr[p] >= pivot:
            p += 1
        while q >= p and arr[q] <= pivot:
            q -= 1
        if p >= q:
            break
        arr[p], arr[q] = arr[q], arr[p]

    arr[left], arr[q] = arr[q], arr[left]  # pivot을 정렬된 위치로 이동
    return q

if __name__ == '__main__':
    quickSort(words, 0, len(words) - 1)
    # insertionSort(words, 0, len(words) - 1)
    print(words)