class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = dict()
        for a in arr1:
            if a in arr1_dict:
                arr1_dict[a] += 1
            else:
                arr1_dict[a] = 1
        res = []
        for a in arr2:
            if a in arr1_dict:
                while arr1_dict[a] > 0:
                    res.append(a)
                    arr1_dict[a] -= 1
        remains = []
        for ele in arr1_dict:
            while arr1_dict[ele] > 0:
                remains.append(ele)
                arr1_dict[ele] -= 1
        return res + sorted(remains)
    
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1) - set(arr2))
        arr1.sort(key=arr2.index)
        return arr1

