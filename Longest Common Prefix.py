class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        s =""
        #strs.sort()

        same = True
        for i in range(len(strs[0])):
            
            for j in range(1,len(strs)):
                if i < len(strs[j]):
                    if strs[0][i] != strs[j][i]:
                        same = False
                        return s

                else:
                    same = False
            if same :
                s+=strs[0][i]
        return s                

