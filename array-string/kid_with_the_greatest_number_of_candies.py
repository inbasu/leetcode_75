class Solution:
    def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        greatest = max(candies)
        return [current + extra_candies >= greatest for current in candies]


if __name__ == "__main__":
    solution = Solution()
    assert solution.kids_with_candies([3, 4, 1], 2) == [True, True, False]
    assert solution.kids_with_candies([1, 1, 1], 2) == [True, True, True]
    assert solution.kids_with_candies([3, 1, 1], 1) == [True, False, False]
    assert solution.kids_with_candies([1], 2) == [True]
    print("All done!")
