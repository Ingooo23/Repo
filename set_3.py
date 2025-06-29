def relationship_status(from_member, to_member, social_graph):
  from_member_following = to_member in social_graph.get(from_member).get("following")
  to_member_following = from_member in social_graph.get(to_member).get("following")
  if to_member_following and from_member_following:
    return "friends"
  elif from_member_following:
    return "follower"
  elif to_member_following:
    return "followed by"
  else:
    return "no relationship"  

def tic_tac_toe(board):
  board_size = len(board)
  y = 0

  for row in range(0, board_size):
    if board[row].count(board[row][0]) == board_size:
      if board[row][0] == "":
        return "NO WINNER"
      else:
        return(board[row][0])

  for column in range(0, board_size):
    for x in range(0, board_size):
      if board[x][column] == board[x-1][column]:
        y += 1
      else:
        y = 0
      if y == board_size:
        if board[x][column] == "":
            return "NO WINNER"
        else:
          return(board[x][column])

  for i in range(0, board_size):
    if board[i][i] == board[i-1][i-1]:
      y += 1
    else:
      y = 0
    if y == board_size:
      if board[i][i] == "":
        return "NO WINNER"
      else:
        return(board[i][i])

  if y != board_size:
    y = 0

  for i in range(1, board_size):
    if board[board_size - i][i - 1] == board[board_size - i - 1][i]:
      y += 1
    else:
      y = 0
    if y == (board_size -1):
      if board[board_size-i-1][i] == "":
        return "NO WINNER"
      else:
        return(board[board_size-i-1][i])

  if y != board_size:
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    time = 0
    stop = first_stop
    while stop != second_stop:
        for (x,y), routes in route_map.items():
            if x == stop:
                time += routes["travel_time_mins"]
                stop = y
            if stop == second_stop:
                break
    return time