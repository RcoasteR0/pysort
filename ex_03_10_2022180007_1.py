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

def mergeSort(arr, start, end):
    size = end - start + 1
    if size <= 5:
        insertionSort(arr, start, end)
        return

    last_left = (start + end) // 2
    first_right = last_left + 1

    mergeSort(arr, start, last_left)
    mergeSort(arr, first_right, end)
    merge(arr, start, first_right, end)

def merge(arr, start, first_right, end):
    #left_array = arr[start:first_right]
    #right_array = arr[first_right:end+1]
    merged = [] #임시 저장할 결과 목록
    l = start
    r = first_right
    while l < first_right and r <= end:
        if arr[l] < arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    while l < first_right:
        merged.append(arr[l])
        l += 1
    while r <= end:
        merged.append(arr[r])
        r += 1

    arr[start:end + 1] = merged

mergeSort(words, 0, len(words)-1)
print(words)