import math
class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            d = int(math.sqrt(i))
            flag = True
            for j in range(2, d+1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1 for _ in range(n+1)]
        ans = 0
        for i in range(2, n):
            if is_prime[i] == 1:
                ans += 1
                for j in range(i*i,n+1, i):
                    is_prime[j] = 0
        return ans


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        is_primes = [1 for _ in range(n)]
        for i in range(2, n):
            if is_primes[i] == 1:
                primes.append(i)
            for j in primes:
                if i * j >= n:
                    continue
                is_primes[i * j] = 0
                if i % j == 0:
                    break
        return len(primes)

class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[]
        flag=[True for _ in range(n+1)]
        for i in range(2,n):
            if flag[i]:
                prime.append(i)
            j=0
            while prime[j]*i<n:
                flag[prime[j]*i]=False
                if i%prime[j]==0:
                    break
                j+=1
        return len(prime)

