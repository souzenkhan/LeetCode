class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #creating dictionaries for each type
        col_map = {}
        row_map = {}
        square_map = {}

        for k in range(9):
            col_map[k] = set()
            row_map[k] = set()
            square_map[k] = set()
        
        for i in range(9): #row index
            for j in range(9): #column index

                cell_value = board[i][j]

                #if the cell value is empty
                if cell_value == '.':
                    continue

                s = (i // 3) * 3 + (j // 3) #square matrix

                if cell_value in row_map[i] or cell_value in col_map[j] or cell_value in square_map[s]:
                    return False
            
                #append to the set if value doesn't already exist
                row_map[i].add(cell_value)
                col_map[j].add(cell_value)
                square_map[s].add(cell_value)

        #returns True if no duplicates found
        return True
        