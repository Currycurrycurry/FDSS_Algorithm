package BFS;

import java.util.ArrayList;

public class Matrix {

    private static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + " , " + y + ")";
        }
    }



    public static int sum(int x) {
        int sum = 0;
        while (x != 0) {
            sum += (x % 10);
            x = x / 10;
        }
        return sum;
    }

    public static int getSum(int x, int y) {
        return sum(x) + sum(y);
    }

    public static boolean canEnter(int threshold, int rows, int cols, int x, int y, boolean[][] visited) {
        return (x >= 0) && (x < rows) && (y >= 0) && (y < cols) && (getSum(x,y) <= threshold) && !visited[x][y];
    }




    public static void allPath(int threshold, int rows, int cols) {
        if (rows == 0 || cols == 0 || threshold <= 0) {
            return;
        }

        boolean[][] visited = new boolean[rows][cols];

         ArrayList<Integer> maxSum = new ArrayList<>();
         allPathRecursively(threshold, rows, cols, 0, 0, visited, 0, maxSum);

        for (int i: maxSum) {
            System.out.println(i);
        }
    }

    public static void maxPath(int threshold, int rows, int cols) {
        if (rows == 0 || cols == 0 || threshold <= 0) {
            return;
        }

        boolean[][] visited = new boolean[rows][cols];

        int[] maxSum = new int[1];
        maxSum[0] = Integer.MIN_VALUE;
        maxPathRecursively(threshold, rows, cols, 0, 0, visited, 0, maxSum);

        System.out.println(maxSum[0]);
    }

    public static void kPath(int threshold, int rows, int cols, int k) {
        if (rows == 0 || cols == 0 || threshold <= 0) {
            return;
        }

        boolean[][] visited = new boolean[rows][cols];

        ArrayList<ArrayList<Point>> result = new ArrayList<>();
        ArrayList<Point> tmp = new ArrayList<>();
        kPathRecursively(threshold, rows, cols, 0, 0, visited, 0, k, tmp, result);


        for (int i = 0; i < result.size() ; i++) {
            for (int j = 0; j < result.get(i).size() ; j++) {
                System.out.print(result.get(i).get(j));
            }
            System.out.println();
        }

    }

    public static boolean check(int threshold, int rows, int cols, int x, int y, boolean[][] visited, int sum, int k) {
        return (x >= 0) && (x < rows) && (y >= 0) && (y < cols) && (getSum(x,y) <= threshold) && !visited[x][y] && sum < k;
    }

    public static void kPathRecursively(int threshold, int rows, int cols, int x, int y, boolean[][] visited, int sum, int k, ArrayList<Point> tmp, ArrayList<ArrayList<Point>> result) {

        if (!check(threshold, rows, cols, x, y, visited, sum, k) ) {
            if (sum == k) {
                result.add(tmp);
            }
            return;
        }

        visited[x][y] = true;

        tmp.add(new Point(x,y));
        kPathRecursively(threshold, rows, cols, x + 1, y, visited, sum + 1, k, tmp, result);
        kPathRecursively(threshold, rows, cols, x - 1, y, visited, sum + 1, k, tmp, result);
        kPathRecursively(threshold, rows, cols, x, y + 1, visited, sum + 1, k, tmp, result);
        kPathRecursively(threshold, rows, cols, x, y - 1, visited, sum + 1, k, tmp, result);


    }

    public static void maxPathRecursively(int threshold, int rows, int cols, int x, int y, boolean[][] visited, int sum, int[] maxSum) {
        if (!canEnter(threshold, rows, cols, x, y, visited)) {
            if (sum > maxSum[0]) {
                maxSum[0] = sum;
            }
            return;
        }

        visited[x][y] = true;
        maxPathRecursively(threshold, rows, cols, x + 1, y, visited, sum + 1, maxSum);
        maxPathRecursively(threshold, rows, cols, x - 1, y, visited, sum + 1, maxSum);
        maxPathRecursively(threshold, rows, cols, x, y + 1, visited, sum + 1, maxSum);
        maxPathRecursively(threshold, rows, cols, x, y - 1, visited, sum + 1, maxSum);

    }


    public static void allPathRecursively(int threshold, int rows, int cols, int x, int y, boolean[][] visited, int sum, ArrayList<Integer> maxSum) {
        if (!canEnter(threshold, rows, cols, x, y, visited)) {
            maxSum.add(sum);
            return;
        }

        visited[x][y] = true;
        allPathRecursively(threshold, rows, cols, x + 1, y, visited, sum + 1, maxSum);
        allPathRecursively(threshold, rows, cols, x - 1, y, visited, sum + 1, maxSum);
        allPathRecursively(threshold, rows, cols, x, y + 1, visited, sum + 1, maxSum);
        allPathRecursively(threshold, rows, cols, x, y - 1, visited, sum + 1, maxSum);

    }

    public static int movingCountRecursively(int threshold, int rows, int cols, int x, int y, boolean[][] visited) {
        int cnt = 0;
        if (canEnter(threshold, rows, cols, x, y, visited)) {
            visited[x][y] = true;
            cnt = 1  + movingCountRecursively(threshold, rows, cols, x + 1, y, visited)
                    + movingCountRecursively(threshold, rows, cols, x - 1, y, visited)
                    + movingCountRecursively(threshold, rows, cols, x, y + 1, visited)
                    + movingCountRecursively(threshold, rows, cols, x, y - 1, visited);
        }
        return cnt;
    }



    public static int movingCount(int threshold, int rows, int cols) {
        // 12 ： 48
        if (rows == 0 || cols == 0 || threshold <= 0) {
            return 0;
        }

        boolean[][] visited = new boolean[rows][cols];

        return movingCountRecursively(threshold, rows, cols, 0, 0, visited);

    }

    public static int minSteps(char[][] matrix,int x_row,int x_col,int y_row, int y_col){

//        int rows = matrix.length;
//        int cols = matrix[0].length;
//
//        if(x_row < 0 || x_row > rows || y_row < 0 || y_col > cols ){
//            throw new IllegalArgumentException("illegal position");
//        }
//
//        if(matrix[x_col][x_col] == '#' || matrix[y_row][y_col] == '#'){
//            throw new RuntimeException("wrong initial position");
//        }
//
//
//
//        boolean[][] visited = new boolean[rows][cols];
//
//        for(int i = 0; i < rows; i++){
//            for(int j = 0;j < cols;j++){
//                visited[i][j] = false;
//            }
//        }
//
//        visited[x_row][x_col] = true;
        return 0;

    }


    public static void main(String[] args){
//        char[][] matrix = new char[3][3];
//        for(int i = 0;i < matrix.length;i++){
//            for(int j = 0;j < matrix[0].length;j++){
//                matrix[i][j] = ' ';
//            }
//        }
//
//        for(int k = 0;k < matrix.length;k++){
//            matrix[k][k] = '#';
//        }
//
//        System.out.println("min step num " + minSteps(matrix,2,0,0,2));
        System.out.println(movingCount(3,4,5));
//        allPath(3,4,5);
        maxPath(3,4,5);

        kPath(3,4,5, 5);

        String s = "1!#2!#3!####";
        String[] ss = s.split("!");
        for(String i: ss) {
            System.out.println(i);
        }







    }
}
