class Solution:
    # naive brute force
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        for i in range(N):
            can_flag = True
            if cost[i] <= gas[i]:
                start = i
                remain_gas = gas[i]
                for j in range(start+1, N):
                    if remain_gas < cost[j-1]:
                        can_flag = False
                        break
                    remain_gas += (gas[j] - cost[j-1])
                if can_flag:
                    for k in range(0, i+1):
                        if remain_gas < cost[k-1]:
                            can_flag = False
                            break
                        remain_gas += (gas[k] - cost[k-1])
            else:
                can_flag = False
            if can_flag:
                return i
        return -1

    # smart 
    


