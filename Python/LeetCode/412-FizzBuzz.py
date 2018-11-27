class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [self.helper(i + 1) for i in range(n)]

    def helper(self, n):
        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 5 == 0:
            return "Buzz"
        elif n % 3 == 0:
            return "Fizz"
        return str(n)
