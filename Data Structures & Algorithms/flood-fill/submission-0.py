class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(image, sr, sc, original, color):
            ROWS, COLS = len(image), len(image[0])
            if (min(sr,sc)<0 or
                sr == ROWS or sc == COLS or
                image[sr][sc] == color):
                return
            if image[sr][sc] != original:
                return
            image[sr][sc] = color
            
    
            dfs(image, sr+1, sc, original, color)
            dfs(image, sr-1, sc, original, color)
            dfs(image, sr, sc+1, original, color)
            dfs(image, sr, sc-1, original, color)

        original = image[sr][sc]
        dfs(image, sr, sc, original, color)
        return image