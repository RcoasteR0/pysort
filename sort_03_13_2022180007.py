class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}({self.x},{self.y})"

# 도시 리스트 초기화
cities = [
    City("Clean", 1336, 536),  City("Prosy", 977, 860),
    City("Rabbi", 6, 758),     City("Addle", 222, 261),
    City("Smell", 1494, 836),  City("Quite", 905, 345),
    City("Lives", 72, 714),    City("Cross", 23, 680),
    City("Synth", 1529, 785),  City("Tweak", 1046, 426),
    City("Medic", 1485, 514),  City("Glade", 660, 476),
    City("Breve", 1586, 448),  City("Hotel", 1269, 576),
    City("Toing", 398, 561),   City("Scorn", 617, 373),
    City("Tweet", 1253, 403),  City("Zilch", 1289, 29),
    City("React", 296, 659),   City("Fiche", 787, 278),
]

def quick_sort(arr, low, high, key=lambda x: x, reverse=False):
    if low < high:
        pi = partition(arr, low, high, key, reverse)
        quick_sort(arr, low, pi - 1, key, reverse)
        quick_sort(arr, pi + 1, high, key, reverse)

def partition(arr, low, high, key, reverse):
    pivot = key(arr[high])
    i = low - 1

    for j in range(low, high):
        if reverse:
            condition = key(arr[j]) > pivot
        else:
            condition = key(arr[j]) < pivot

        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 요소 교환

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def print_cities(title, cities_list):
    print(title)
    print(", ".join(map(str, cities_list)))
    print()

# 정렬 전 도시 목록 출력
print_cities("Before sorting:", cities)

# 이름 기준으로 정렬 (알파벳 순)
quick_sort(cities, 0, len(cities) - 1, key=lambda city: city.name)
print_cities("After sorting by name:", cities)

# x 좌표 기준으로 정렬 (오름차순)
quick_sort(cities, 0, len(cities) - 1, key=lambda city: city.x)
print_cities("After sorting by x coordinate:", cities)
