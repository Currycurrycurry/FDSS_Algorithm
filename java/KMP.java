public class KMP {
    private int[][] dp;
    private String pat;

    public KMP(String pat) {
        this.pat = pat;
        int M = pat.length();
        dp = new int[M][256];
        dp[0][pat.charAt(0)] = 1;
        int X = 0;
        for (int j = 1; j < M; j ++) {
            for (int c = 0; c < 256; c++) {
                dp[j][c] = dp[X][c];
            }
            dp[j][pat.charAt(j)] = j + 1;
            X = dp[X][pat.charAt(j)];
        }
    }

    public int search(String txt) {
        int M = pat.length();
        int N = txt.length();
        int j = 0;
        for (int i = 0; i < N; i ++) {
            j = dp[j][txt.charAt(i)];
            if (j == M) {
                return i - M + 1;
            }
        }
        return -1;
    }

    public static brute_search(String pat, String txt) {
        int M = pat.length;
        int N = txt.length;
        for (int i = 0;i < N - M; i ++) {
            int j;
            for (j = 0;j < M; j++) {
                if (txt.charAt(i+j) != pat.charAt(j)) {
                    break;
                }
            }
            if (j == M) {
                return i;
            }
        }
        return -1;
    }
}