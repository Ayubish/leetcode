class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for a in b] for b in img]
        for i in range(len(img)):
            for j in range(len(img[i])):
                sum = img[i][j]
                neigbours_count = 1
                if j>0:
                    sum += img[i][j-1]
                    neigbours_count += 1
                if j<len(img[i])-1:
                    sum += img[i][j+1]
                    neigbours_count += 1
                if i>0:
                    sum += img[i-1][j]
                    neigbours_count += 1
                    if j>0:
                        sum += img[i-1][j-1]
                        neigbours_count += 1
                    if j<len(img[i])-1:
                        sum += img[i-1][j+1]
                        neigbours_count += 1
                if i<len(img)-1:
                    sum += img[i+1][j]
                    neigbours_count += 1
                    if j>0:
                        sum += img[i+1][j-1]
                        neigbours_count += 1
                    if j<len(img[i])-1:
                        sum += img[i+1][j+1]
                        neigbours_count += 1
                matrix[i][j] = sum//neigbours_count
        return matrix
                