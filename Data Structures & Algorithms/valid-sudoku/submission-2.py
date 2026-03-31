class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        check_rows = defaultdict(list)
        check_columns = defaultdict(list)
        check_square = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j].isalnum():
                    int_value = int(board[i][j])
                    if int_value <= 9:
                    
                        #check_rows
                        if int_value  in check_rows[i]:
                            return False
                        else:
                            check_rows[i].append(int_value)
                        #Check_columns
                        if int_value  in check_columns[j]:
                            return False
                        else:
                            check_columns[j].append(int_value)

                        #check square (3*3)
                        if int_value in check_square[i//3+((j//3)*3)]:
                            return False
                        else:
                            check_square[i//3+(j//3)*3].append(int_value)

        return True
