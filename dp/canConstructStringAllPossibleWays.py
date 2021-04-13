class solution:
    
    def canConstructAllPossibleWays(self, string, sArray, mem={}):
        if string == "":
            return [[]]

        res = []
        for s in sArray:
            index = string.find(s)
            if index == 0:
                new = string[index+len(s):]
                val = self.canConstructAllPossibleWays(new,sArray)
                for e in val:
                    e.insert(0,s)
                res += val
        mem[string] = res
        return res


c = solution()

# print(c.canConstructStringFromArray("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeeef"]))
# print(c.canConstructCountWays("abcde f",["ab","abc","cd","def","abcd"]))
print(c.canConstructAllPossibleWays("purple",["purp","p","ur","le","purpl"]))
print(c.canConstructAllPossibleWays("enterapotentpot",["a","p","ent","enter","ot","o","t"]))