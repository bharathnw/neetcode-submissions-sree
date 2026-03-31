class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashMap = defaultdict(int)
        res = []
        for num in nums:
            hashMap[num] += 1
            if len(hashMap) == 3:
                new_ins = defaultdict(int)
                for key in hashMap.keys():
                    hashMap[key] -= 1
                    if hashMap[key] > 0:
                        new_ins[key] = hashMap[key]
                hashMap = new_ins
        
        for num in hashMap:
            if nums.count(num) > (len(nums)//3):
                res.append(num)
        return res



