# 加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                carry = 0
                break
            else:
                digits[i] = 0
        if carry != 0:
            digits.insert(0,1)
        return digits
