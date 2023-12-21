class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        for i in range(n):
            image[i].reverse()
        for r in range(n):
            for c in range(n):
                if image[r][c]==1:
                    image[r][c]=0
                else:
                    image[r][c]=1
        return image