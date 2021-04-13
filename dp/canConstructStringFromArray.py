class solution:

    def canConstructStringFromArray(self, string, sArray, mem={}):
        if string in mem:
            return mem[string]
        if string == "":
            return True
        
        for s in sArray:
            # print(string,s)
            index = string.find(s)
            if index == 0:
                val = self.canConstructStringFromArray(string[index+len(s):],sArray)
                if val:
                    mem[string] = val
                    return val
        mem[string] = False
        return False

    
    def canConstructCountWays(self, string, sArray, mem={}):
        if string in mem:
            return mem[string]
        if string == "":
            return 1
        
        sum = 0
        for s in sArray:
            # print(string,s)
            index = string.find(s)
            if index == 0:
                val = self.canConstructCountWays(string[index+len(s):],sArray)
                if val != 0:
                    sum += val
                    # mem[string] = val
                    # return val
        mem[string] = sum
        return mem[string]

c = solution()

# print(c.canConstructStringFromArray("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeeef"]))
# print(c.canConstructCountWays("abcde f",["ab","abc","cd","def","abcd"]))
print(c.canConstructCountWays("purple",["purp","p","ur","le","purpl"]))
print(c.canConstructCountWays("enterapotentpot",["a","p","ent","enter","ot","o","t"]))