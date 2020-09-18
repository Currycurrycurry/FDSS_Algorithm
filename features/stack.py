class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            w = 1
            left_index = i
            while left_index >= 0 and heights[left_index] >= heights[i]:
                left_index -= 1
                w += 1
            right_index = i
            while right_index <= len(heights) - 1 and heights[right_index] >= heights[i]:
                right_index += 1
                w += 1
            max_area = max(max_area, (w - 2) * heights[i])
        return max_area

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()] 
                max_area = max(max_area, h * (i - stack[-1] - 1))
            stack.append(i)
        return max_area 

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def getMaxArea(heights):
            stack = []
            heights = [0] + heights + [0]
            max_res = 0
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    max_res = max(max_res, (i - stack[-1] - 1) * h)
                stack.append(i)
            return max_res
        if not matrix:
            return 0
        row_len, col_len = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * col_len
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            max_area = max(max_area, getMaxArea(heights))
        return max_area