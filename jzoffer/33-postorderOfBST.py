    def verifyPostorder(postorder):
            if len(postorder) <= 1:
                return True
            root = postorder[-1]
            left_index = 0
            while left_index < len(postorder) - 1:
                if postorder[left_index] < root:
                    left_index += 1
                else:
                    break
            right_index = left_index
            while right_index < len(postorder) - 1:
                if postorder[right_index] > root:
                    right_index += 1
                else:
                    return False
            return self.verifyPostorder(postorder[:left_index]) and self.verifyPostorder(postorder[left_index:right_index])