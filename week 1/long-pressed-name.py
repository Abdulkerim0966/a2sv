class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointer1=0
        pointer2=0
        while pointer2<len(typed) or pointer1<len(name):
            if pointer2<len(typed) and pointer1<len(name) and name[pointer1]==typed[pointer2]:
                pointer1+=1
                pointer2+=1
            elif pointer1>0 and pointer2<len(typed)and typed[pointer2]==name[pointer1-1]:
                pointer2+=1
            else:
                return False
        return True

        