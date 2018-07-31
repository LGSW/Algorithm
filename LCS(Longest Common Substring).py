# 最长公共子串（连续）
class solution(object):
    def LCS(self, str1, str2):
        if str1 == '' and str2 == '':
            return 0
        l1 = len(str1); l2 = len(str2)
        vec = [[0 for i in range(l2+1)] for i in range(l1+1)]
        result = 0
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if (str1[i-1] == str2[j-1]):
                    vec[i][j] = vec[i-1][j-1] + 1
                    result = max(vec[i][j], result)
                else:
                    vec[i][j] = 0

        return result

a = solution()
print(a.LCS('ABCBDAB','BDCABA'))