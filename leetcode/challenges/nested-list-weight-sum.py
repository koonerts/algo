# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self._list = None
        self._integer = None
        if value is not None:
            if type(value) == int:
                self._integer = value
            else:
                self._list = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self._integer is not None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if not self._list:
            self._list = []
        self._list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self._integer = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self._integer

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self._list


class Solution:

    def depthSum(self, nestedList: list[NestedInteger]) -> int:

        def helper(ni_obj, depth):
            if ni_obj.isInteger():
                curr_val = depth * ni_obj.getInteger()
                return curr_val
            else:
                nested_sum = 0
                for nested_ni_obj in ni_obj.getList():
                    nested_sum += helper(nested_ni_obj, depth+1)
                return nested_sum


        depth_sum = 0
        for obj in nestedList:
            depth_sum += helper(obj, 1)
        return depth_sum


ni_list = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
print(Solution().depthSum(ni_list))