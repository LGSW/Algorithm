class Trie:
    def __init__(self):
        self.trie = {}
        self.size = 0

    def add(self, word):
        p = self.trie
        word = word.strip()
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        if word != '':
            p[''] = ''

    def search(self, word):
        p = self.trie
        word = word.lstrip()
        for c in word:
            if not c in p:
                return False
            p = p[c]
        if '' in p:
            return True
        return False

    def output(self):
        print('{')
        print(self.trie)
        print('}')

if __name__ == '__main__':
    trie_obj = Trie()
    trie_obj.add('hello')
    trie_obj.add('help')
    trie_obj.add('world')
    trie_obj.add('abc')
    #打印构建的Trie树
    trie_obj.output()
    #查找单词
    if trie_obj.search('hello'): print('Yes')
    else: print('No')
    if trie_obj.search('China'): print('Yes')
    else:print ('No')

