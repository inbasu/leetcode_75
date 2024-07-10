class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            str1, str2 = (str2, str1) if str1 > str2 else (str1, str2)
            return str1[: self.gcd(len(str1), len(str2))]
            # gcd(1, 2)
        return ""

    def gcd(self, num1: int, num2: int) -> int:
        if num2:
            return self.gcd(num2, num1 % num2)
        return num1


if __name__ == "__main__":
    test = Solution()
    assert test.gcd_of_strings("a", "aaa") == "a"
    assert test.gcd_of_strings("ab", "abab") == "ab"
    assert test.gcd_of_strings("abab", "ababab") == "ab"
    assert test.gcd_of_strings("ab", "ba") == ""
    assert test.gcd_of_strings("", "") == ""
    assert test.gcd_of_strings("a", "") == ""
    print("All test passed!")
