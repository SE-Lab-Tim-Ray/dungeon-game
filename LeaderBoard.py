LEADER_BOARD_PATH = "./resources/LeaderBoard.txt"
class LeaderBoard:
    def __init__(self):
        self.leader_board = open(LEADER_BOARD_PATH, 'r')
        self.leader_board.close()
    def board_input_result(nickname='NoName', score=0):
        leader_board_name = str(nickname).rjust(20)
        leader_board_score = str(score).rjust(10)
        #the content we for one line we put into the screen is leader_board_result
        leader_board_result = leader_board_name+'   '+leader_board_score+'\n'
        #open the file and write the result into txt file
        with open(LEADER_BOARD_PATH, 'r') as in_file:
            contents = in_file.readlines()
        with open(LEADER_BOARD_PATH, 'w') as out_file:
            if not contents:
                out_file.write(leader_board_result)
            elif contents:
                for line in contents:
                    if int(line[22:32]) <= score:
                        line = leader_board_result + line
                    out_file.write(line)
                contents = out_file.readlines()
        #the new list of leaderboard
        return contents

