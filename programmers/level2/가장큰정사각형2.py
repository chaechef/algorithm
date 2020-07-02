def solution(board):
   allsum = sum([sum(line) for line in board])
   if allsum == 0:
      return 0

   msize = 0
   for i in range(1, len(board)):
      for j in range(1, len(board[0])):
         if board[i][j] == 0:
            continue
         board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
         if msize < board[i][j]:
            msize = board[i][j]

   if msize == 0:
      return 1

   return msize * msize





print(solution([[0,0]]))