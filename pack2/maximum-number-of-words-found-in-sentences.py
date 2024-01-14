class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mi=0
        for i in range (len(sentences)):
            mi=max(sentences[i].count(" "),mi)
        return mi+1
    