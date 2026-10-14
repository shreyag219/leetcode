class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":  # Any number times 0 is 0
            return "0"

        m, n = len(num1), len(num2)  # Lengths of both numbers
        result = [0] * (m + n)  # Product has at most m+n digits

        for i in range(m - 1, -1, -1):  # num1 from right to left
            for j in range(n - 1, -1, -1):  # num2 from right to left
                total = int(num1[i]) * int(num2[j]) + result[i + j + 1]  # Product plus what is already in this column
                result[i + j + 1] = total % 10  # Ones digit stays in this column
                result[i + j] += total // 10  # Carry goes one column to the left

        start = 0  # Find the first non-zero digit
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(str(d) for d in result[start:])  # Join the remaining digits into the answer string
        