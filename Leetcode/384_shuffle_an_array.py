import copy
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        temp = copy.deepcopy(self.nums)
        n = len(temp)
        for i in range(n):
            t = random.randint(i, n - 1)
            # swap i and t
            c = temp[i]
            temp[i] = temp[t]
            temp[t] = c
        return temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

def main():
    nums = [1, 2, 3]
    obj = Solution(nums)
    print(obj.shuffle())
    obj.reset()
    print(obj.nums)


if __name__ == '__main__':
    main()