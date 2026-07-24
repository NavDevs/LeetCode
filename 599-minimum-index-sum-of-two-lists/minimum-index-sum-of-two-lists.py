class Solution(object):
    def findRestaurant(self, list1, list2):
        f  = {}
        s = {}

        for i in range(len(list1)):
            f[list1[i]] = i
        m = float("inf")
        for i in range(len(list2)):
            if list2[i] in f:
                index_sum = i  +  f[list2[i]]
                if index_sum < m:
                    m = index_sum
                    ans = [list2[i]]
                elif index_sum == m:
                    ans.append(list2[i])
        return ans            

        
        
        