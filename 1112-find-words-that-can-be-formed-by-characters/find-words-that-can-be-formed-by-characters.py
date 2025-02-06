class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        for word in words:
            charsCount = Counter(chars)
            for char in word:
                if charsCount[char]<1:
                    break
                else:
                    charsCount[char] -= 1
            else:
                ans.append(len(word))
        return sum(ans)
