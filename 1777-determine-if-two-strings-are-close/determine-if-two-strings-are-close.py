class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Count, word2Count = Counter(word1), Counter(word2)
        word1Set, word2Set = set(word1Count.values()), set(word2Count.values())
        
        if len(word1) != len(word2): return False

        for n in word1:
            if n not in word2:
                return False

        if word1Set != word2Set:
            return False


        return sorted(word1Count.values()) == sorted(word2Count.values())
