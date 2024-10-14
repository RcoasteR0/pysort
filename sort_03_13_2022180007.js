class City {
  constructor(name, x, y) {
    this.name = name;
    this.x = x;
    this.y = y;
  }

  toString() {
    return `${this.name}(${this.x},${this.y})`;
  }
}

let cities = [
  new City("Clean", 1336, 536),  new City("Prosy", 977, 860),
  new City("Rabbi", 6, 758),     new City("Addle", 222, 261),
  new City("Smell", 1494, 836),  new City("Quite", 905, 345),
  new City("Lives", 72, 714),    new City("Cross", 23, 680),
  new City("Synth", 1529, 785),  new City("Tweak", 1046, 426),
  new City("Medic", 1485, 514),  new City("Glade", 660, 476),
  new City("Breve", 1586, 448),  new City("Hotel", 1269, 576),
  new City("Toing", 398, 561),   new City("Scorn", 617, 373),
  new City("Tweet", 1253, 403),  new City("Zilch", 1289, 29),
  new City("React", 296, 659),   new City("Fiche", 787, 278),
];

console.log("Before sorting:");
console.log(cities.map(city => city.toString()));

// 퀵 정렬 구현
function quickSort(arr, low, high, compare) {
  if (low < high) {
    let pi = partition(arr, low, high, compare);
    quickSort(arr, low, pi - 1, compare);  // 피벗보다 작은 부분 정렬
    quickSort(arr, pi + 1, high, compare); // 피벗보다 큰 부분 정렬
  }
}

function partition(arr, low, high, compare) {
  let pivot = arr[high];
  let i = low - 1;

  for (let j = low; j < high; j++) {
    if (compare(arr[j], pivot) < 0) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]]; // 요소 교환
    }
  }
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

// 이름 기준으로 정렬 (알파벳 순)
quickSort(cities, 0, cities.length - 1, (a, b) => {
  if (a.name < b.name) return -1;
  if (a.name > b.name) return 1;
  return 0;
});

console.log("\nAfter sorting by name:");
console.log(cities.map(city => city.toString()));

// x 좌표 기준으로 정렬 (오름차순)
quickSort(cities, 0, cities.length - 1, (a, b) => a.x - b.x);

console.log("\nAfter sorting by x coordinate:");
console.log(cities.map(city => city.toString()));
