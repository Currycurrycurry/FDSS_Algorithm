class Solution:
    # normal recursion or dp or sliding window
    # method 1 normal recursion
    def maxScore1(self, cardPoints, k):
        def helper(cardPoints, k):
            # max(cardPoints[0] + helper(cardPoints[1:], k-1), helper(cardPoints[:-1], k-1))
            if len(cardPoints) == 0 or k == 0:
                return 0
            return max(cardPoints[0] + helper(cardPoints[1:], k-1), helper(cardPoints[:-1], k-1))
        return helper(cardPoints, k)
    
    # method 2 dp
    def maxScore2(self, cardPoints, k):
        # cannot be dped
        pass

    # method 3 sliding window function
    def maxScore3(self, cardPoints, k):
        tmp = ans = sum(cardPoints[:k])
        for i in range(k):
            tmp += cardPoints[-1-i] - cardPoints[k-1-i]
            ans = max(ans, tmp)
        return ans
    




