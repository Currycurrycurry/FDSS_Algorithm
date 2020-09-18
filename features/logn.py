def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums_len = len(nums)

        def findKthNumber(k):
            v = partition(0, nums_len-1)
            while v != k:
                if v < k:
                    v = partition(v+1, nums_len-1)
                else:
                    v = partition(0, v-1)
            return nums[k]

        def partition(left, right):
            pivot = left
            left += 1
            while True:
                while left < right and nums[left] < nums[pivot]:
                    left += 1
                while right < left and nums[right] > nums[pivot]:
                    right -= 1
                if left > right:
                    break
                nums[left], nums[right] = nums[right], nums[left]
            nums[pivot], nums[left] = nums[left], nums[pivot]
            return pivot

        if nums_len % 2 == 0:
            return findKthNumber(nums_len // 2) + findKthNumber(nums_len // 2 - 1)
        else:
            return findKthNumber(nums_len // 2)

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(arr1,arr2,k):
            len1,len2 = len(arr1),len(arr2)
            if len1 > len2:
                return findKthElement(arr2,arr1,k)
            if not arr1:
                return arr2[k-1]
            if k == 1:
                return min(arr1[0],arr2[0])
            i,j = min(k//2,len1)-1,min(k//2,len2)-1
            if arr1[i] > arr2[j]:
                return findKthElement(arr1,arr2[j+1:],k-j-1)
            else:
                return findKthElement(arr1[i+1:],arr2,k-i-1)
        l1,l2 = len(nums1),len(nums2)
        left,right = (l1+l2+1)//2,(l1+l2+2)//2
        return (findKthElement(nums1,nums2,left)+findKthElement(nums1,nums2,right))/2