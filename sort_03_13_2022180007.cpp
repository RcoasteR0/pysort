#include <iostream>
#include <algorithm>

using namespace std;

class City {
public:
    string name;
    int x, y;
    City(const char *name, int x, int y) {
        this->name = name;
        this->x = x;
        this->y = y;
    }
    ostream &print(ostream &os) const {
        os << name << '(' << x << ',' << y << ')';
        return os;
    }
};

// 출력 연산자 오버로딩
ostream &operator <<(ostream &os, const City &c) {
    return c.print(os);
}

// 도시 배열 출력 함수
void printCities(const City *p, int count) {
    for (int i = 0; i < count; i++, p++) {
        cout << *p << ' ';
    }
    cout << '\n';
}

// y 좌표 기준 비교 함수
bool compareByY(const City& a, const City& b) {
    return a.y < b.y;
}

// 이름 기준 비교 함수
bool compareByName(const City& a, const City& b) {
    return a.name < b.name;
}

// 분할 함수 (피벗을 기준으로 배열을 나눈다)
int partitionCities(City arr[], int low, int high, bool (*compare)(const City&, const City&)) {
    City pivot = arr[high];  // 마지막 요소를 피벗으로 선택
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (compare(arr[j], pivot)) {
            i++;
            swap(arr[i], arr[j]);  // 조건에 맞으면 교환
        }
    }
    swap(arr[i + 1], arr[high]);  // 피벗과 교환
    return i + 1;
}

// 퀵 정렬 함수
void quickSort(City arr[], int low, int high, bool (*compare)(const City&, const City&)) {
    if (low < high) {
        int pi = partitionCities(arr, low, high, compare);  // 분할 지점
        quickSort(arr, low, pi - 1, compare);               // 왼쪽 부분 정렬
        quickSort(arr, pi + 1, high, compare);              // 오른쪽 부분 정렬
    }
}

City cities[] = {
    City("Clean", 1336, 536), City("Prosy", 977, 860),  City("Rabbi", 6, 758),    City("Addle", 222, 261),
    City("Smell", 1494, 836), City("Quite", 905, 345),  City("Lives", 72, 714),   City("Cross", 23, 680),
    City("Synth", 1529, 785), City("Tweak", 1046, 426), City("Medic", 1485, 514), City("Glade", 660, 476),
    City("Breve", 1586, 448), City("Hotel", 1269, 576), City("Toing", 398, 561),  City("Scorn", 617, 373),
    City("Tweet", 1253, 403), City("Zilch", 1289, 29),  City("React", 296, 659),  City("Fiche", 787, 278),
};

int main(void) 
{
    int n_cities = sizeof(cities) / sizeof(cities[0]);

    // 정렬 전 도시 목록 출력
    cout << "Before sorting:\n";
    printCities(cities, n_cities);

    // 이름 기준으로 정렬
    quickSort(cities, 0, n_cities - 1, compareByName);
    cout << "\nAfter sorting by name:\n";
    printCities(cities, n_cities);

    // y 좌표 기준으로 정렬
    quickSort(cities, 0, n_cities - 1, compareByY);
    cout << "\nAfter sorting by y coordinate:\n";
    printCities(cities, n_cities);

    return 0;
}
