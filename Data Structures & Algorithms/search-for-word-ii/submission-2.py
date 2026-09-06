class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dummy = TrieNode()
        
        for word in words:
            curr = dummy
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]
            
            curr.is_end_of_word = True

        
        visited = set()
        output = []

        def dfs(r, c, curr, path):

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return

            char = board[r][c]

            if (r,c) in visited:
                return

            if char not in curr.children:
                return

            curr = curr.children[char]

            path += char

            if curr.is_end_of_word and path not in output:
                output.append(path)
            
            if (r,c) not in visited:
                visited.add((r,c))

            dfs(r+1,c,curr,path)
            dfs(r,c+1,curr,path)
            dfs(r,c-1,curr,path)
            dfs(r-1,c,curr,path)

            visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,dummy,"")

        return output

