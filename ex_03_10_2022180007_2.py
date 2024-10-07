import random

words = [

  '2022180007', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'addle', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

  'quite', 'seminar', 'bloomers', 'lives', 'innocuous', 'effluent', 'cross', 'recidivist', 'wet', 'synth',

  'mantilla', 'tweak', 'lowbrow', 'aviation', 'quadruped', 'capable', 'graphic', 'barman', 'intemperate', 'mastermind',

  'submit', 'considering', 'riddance', 'polyethene', 'jim', 'varicolored', 'medic', 'ferric', 'minaret', 'capacitor',

  'pusher', 'gingerbread', 'grizzled', 'upsilon', 'km', 'glade', 'ribbon', 'parascending', 'shinty', 'breve',

  'hotel', 'similitude', 'fuddle', 'secretariat', 'silicate', 'whinchat', 'abstention', 'untrue', 'toing', 'cnd',

  'ramification', 'scorn', 'apricot', 'arnica', 'militate', 'muslim', 'homicide', 'overfeed', 'shooting', 'growth',

]

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        select = i
        while select > left:
            if arr[select] < arr[select - 1]:
                arr[select], arr[select - 1] = arr[select - 1], arr[select]
                select = select - 1
            else:
                break

def quickSort(arr, left, right):
    size = right - left + 1
    if size <= 5:
        return

    pivot_index = partition()
    quickSort(arr, left, pivot_index - 1)
    quickSort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]

    p, q = left, right

    while p < q: #선수 역전할때까지
        while : #왼쪽에서 오른쪽
            pass
        while : #오른쪽에서 왼쪽
            pass

        #swap # 두 선수 교체

    #맨 왼쪽 pivot값을 왼쪽 덩어리의 가장 오른쪽 위치로 보냄
    arr[left], arr[random_index] = arr[random_index], arr[left]

    return random_index

quickSort(words, 0, len(words)-1)
insertionSort(words, 0, len(words)-1)
print(words)