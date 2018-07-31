# 最长公共子序列（不连续）
class solution(object):
    def LCS(self, str1, str2):
        if str1 == '' and str2 == '':
            return 0
        l1 = len(str1); l2 = len(str2)
        vec = [[0 for i in range(l2+1)] for i in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if (str1[i-1] == str2[j-1]):
                    vec[i][j] = vec[i-1][j-1] + 1
                else:
                    if vec[i - 1][j] >= vec[i][j - 1]:
                        vec[i][j] = vec[i - 1][j]
                    else:
                        vec[i][j] = vec[i][j - 1]

        return vec[l1][l2]

a = solution()
print(a.LCS('ABCBDAB','BDCABA'))
