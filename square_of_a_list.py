class Solution:
    def solve(self, nums):
        squares = list(map(lambda x: x**2, nums))
        squares.sort()
        return squares


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([1, 2, 3, 4, 5]))
