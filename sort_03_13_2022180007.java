import java.util.Arrays;
import java.util.Comparator;

public class Main {
  public static class City implements Comparable<City> {
    String name; 
    int x, y;
    
    public City(String name, int x, int y) {
      this.name = name;
      this.x = x;
      this.y = y;
    }

    public String toString() {
      return name + '(' + x + ',' + y + ')';
    }

    // Compare cities by name (already implemented for name sorting)
    public int compareTo(City other) {
      return this.name.compareTo(other.name);
    }
  }

  // Implementing quicksort to sort cities by x coordinate
  public static void quickSort(City[] cities, int low, int high) {
    if (low < high) {
      int pi = partition(cities, low, high);
      quickSort(cities, low, pi - 1);  // Recursively sort elements before partition
      quickSort(cities, pi + 1, high); // Recursively sort elements after partition
    }
  }

  public static int partition(City[] cities, int low, int high) {
    City pivot = cities[high];  // Pivot element is the last element
    int i = (low - 1);  // Index of smaller element

    for (int j = low; j < high; j++) {
      if (cities[j].x < pivot.x) { // Comparing based on x coordinate
        i++;
        // Swap cities[i] and cities[j]
        City temp = cities[i];
        cities[i] = cities[j];
        cities[j] = temp;
      }
    }
    // Swap cities[i+1] and cities[high] (or pivot)
    City temp = cities[i + 1];
    cities[i + 1] = cities[high];
    cities[high] = temp;

    return i + 1;
  }

  static City[] cities = new City[] {
    new City("Clean", 1336, 536),    new City("Prosy", 977, 860),
    new City("Rabbi", 6, 758),       new City("Addle", 222, 261),
    new City("Smell", 1494, 836),    new City("Quite", 905, 345),
    new City("Lives", 72, 714),      new City("Cross", 23, 680),
    new City("Synth", 1529, 785),    new City("Tweak", 1046, 426),
    new City("Medic", 1485, 514),    new City("Glade", 660, 476),
    new City("Breve", 1586, 448),    new City("Hotel", 1269, 576),
    new City("Toing", 398, 561),     new City("Scorn", 617, 373),
    new City("Tweet", 1253, 403),    new City("Zilch", 1289, 29),
    new City("React", 296, 659),     new City("Fiche", 787, 278),
  };

  public static void main(String args[]) {
    System.out.println("Before sorting by name:");
    System.out.println(Arrays.toString(cities));
    
    // Sort by name (default behavior)
    Arrays.sort(cities);
    System.out.println("\nAfter sorting by name:");
    System.out.println(Arrays.toString(cities));

    // Sort by x coordinate using quicksort
    quickSort(cities, 0, cities.length - 1);
    System.out.println("\nAfter sorting by x coordinate:");
    System.out.println(Arrays.toString(cities));
  }
}
