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

count = len(words)

def downheap(root, size):
    lchild = root * 2 + 1
    rchild = root * 2 + 2
    if lchild >= size:
        return
    child = lchild
    if rchild < size:
        if words[rchild] > words[lchild]:
            child = rchild
    if words[root] < words[child]:
        words[root], words[child] = words[child], words[root]
        downheap(child, size)

print(f'before: {words}')

parent_idx = count // 2 - 1
for i in range(parent, -1, -1):
    downheap(i, count)

last_idx = count - 1
while last_idx > 0:
    words[0], words[last_idx] = words[last_idx], words[0]
    downheap(0, last_idx)
    last_idx -= 1

print(f'after: {words}')
    