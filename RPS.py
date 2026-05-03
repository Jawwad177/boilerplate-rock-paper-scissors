def player(prev_play, opponent_history=[], my_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

   
    if len(opponent_history) < 5:
        my_move = "R"
        my_history.append(my_move)
        return my_move

    
    pattern = "".join(opponent_history[-3:])
    
  
    counts = {"R": 0, "P": 0, "S": 0}
    for i in range(len(opponent_history) - 3):
        if "".join(opponent_history[i:i+3]) == pattern:
            next_move = opponent_history[i+3]
            counts[next_move] += 1

    
    predicted = max(counts, key=counts.get)

   
    counter = {"R": "P", "P": "S", "S": "R"}
    my_move = counter[predicted]

    my_history.append(my_move)
    return my_move