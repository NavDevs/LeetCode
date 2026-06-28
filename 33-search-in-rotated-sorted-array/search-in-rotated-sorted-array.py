class Solution(object):

    def search(self, nums, target):

        def binary(s,e,target):

            while s <= e:

                m=(s+e)//2

                if nums[m]==target:
                    return m

                elif nums[m]>target:
                    e=m-1

                else:
                    s=m+1

            return -1


        pivot = nums.index(min(nums))

        r1 = binary(0,pivot-1,target)

        r2 = binary(pivot,len(nums)-1,target)

        return max(r1,r2)