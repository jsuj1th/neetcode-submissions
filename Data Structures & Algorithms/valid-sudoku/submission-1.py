class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Checking Sqaures
        for i in range(9):
            for j in range(9):
                if (i%3==0 and j%3==0) and (i < 6 and j < 6):
                    k=[]
                    for i_x in [0,1,2,]:
                        for j_x in [0,1,2]:
                            val= board[i+i_x][j +j_x]
                            if val==".":
                                continue 
                            if int(val) in k:
                                # print(i,j)
                                # print("Failed in Sqaures")
                                return False
                            k.append(int(val))
        
        #Checking Rows
        for i in range(9):
            k=[]
            for j in range(9):
                val=board[i][j]
                if val==".":
                    continue
                if int(val) in k:
                    # print("Failed in Rows")
                    return False
                k.append(int(val))
        #Checking Columns
        for j in range(9):
            k=[]
            for i in range(9):
                val=board[i][j]
                if val==".":
                    continue
                if int(val) in k:
                    # Print("Failed in Columns")
                    return False
                k.append(int(val))
        return True

