#write a program where target sum is possible or not
class solution:
    def targetSum(self, target, arr, mem={}):
        if target in mem:
            return mem[target]
        if target == 0:
            return True
        
        if target < 0:
            return False

        for i in arr:
            val = self.targetSum(target - i, arr, mem)
            if val :
                mem[target-i] = val
                return mem[target-i]
        mem[target] = False   
        return mem[target]
    def targetSumThenReturnArray(self, target, arr, mem={}):
        if target in mem:
            return mem[target]
        if target == 0:
            return []
        
        if target < 0:
            return None

        for i in arr:
            val = self.targetSumThenReturnArray(target - i, arr, mem)
            if val != None:
                mem[target-i] = val + [i]
                return mem[target-i]
        mem[target] = None   
        return mem[target]



    def helper(self, target, arr, mem):
        if target in mem:
            return mem[target]
        if target == 0:
            return []
        
        if target < 0:
            return None
        
        comb = None
        for i in arr:
            val = self.helper(target - i, arr, mem)
            if val != None:
                val.append(i)
                if comb == None or len(comb) > len(val):
                    comb = val
                # mem[target] = mem[target] + mem[target-i]
        
        mem[target] = comb
        return mem[target]
    def bestComination(self, target, arr):
        mem = {}
        self.helper(target, arr, mem)
        return mem[target]

c = solution()
# print(c.targetSum(301, [7,14]))
# print(c.targetSumThenReturnArray(8, [2,3,5]))
print(c.bestComination(8, [2,3,5]))