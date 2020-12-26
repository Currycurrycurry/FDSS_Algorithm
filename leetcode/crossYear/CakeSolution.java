import java.util.Set;
import java.util.Map;


public class CakeSolution{
    private Map<Integer, Set<Integer>> map = new HashMap<Integer, Set<Integer>>();
    private boolean[] used;
    private boolean found = false;

    private class Answer {
        private int minCount;
        private List<Integer> permutation;

        public Answer(int minCount, List<Integer> permutation) {
            this.minCount = minCount;
            this.permutation = permutation;
        }

        public int getMinCount() {
            return minCount;
        }

        public List<Integer> getOrder() {
            return permutation;
        }
    }

    public static Answer minimalFruitPie() {
        int n = 1;
        map.put(1, new HashSet<Integer>());
        List<Integer> permutation = new ArrayList<Integer>();
        while (!found) {
            n++;
            Set<Integer> set = new HashSet<Integer>();
            for (int sqrt = 1; sqrt * sqrt < n * 2; sqrt++) {
                int remain = sqrt * sqrt - n;
                if (remain > 0) {
                    Set<Integer> prevSet = map.get(remain);
                    set.add(remain);
                    prevSet.add(n);
                }
            }
            map.put(n, set);
            used = new boolean[n+1];
            backtrack(0, n, permutation);
        }
        return new Anwer(n, permutation);
    }

    public static void backtrack(int index, int n, List<Integer> permutation) {
        if (index == n) {
            int first = permutation.get(0);
            int last = permutation.get(permutation.size() - 1);
            if (map.get(first).contains(last)) {
                found = true;
            }
        } else if (index == 0) {
            used[1] = true;
            permutation.add(1);
            backtrack(index+1, n, permutation);
            if (!found) {
                used[1] = false;
                permutation.remove(index);
            }
        } else {
            Set<Integer> set = map.get(permutation.get(index-1));
            for (int num: set) {
                if (!used[num]) {
                    used[num] = true;
                    permutation.add(num);
                    backtrack(index+1, n, permutation);
                    if (!found) {
                        used[num] = false;
                        permutation.remove(index);
                    }
                }
            }
        }

    }

    public static void main(String[] args) {
        CakeSolution solution = new CakeSolution();
        System.out.println(solution.minimalFruitPie());
    }
}



