class Solution(object):
    def frequencySort(self, s):
        ans  = ""

        freq = Counter(s)
        for i in sorted(freq, key = freq.get,reverse = True):
            ans += i*freq[i]
        return ans
        