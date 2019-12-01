class LeaderBoard:
    def __init__(self):
        self.leader_board_path = ".../resources/LeaderBoard.txt"
        self.leader_board = open(self.leader_board_path, 'r')
        self.leader_board.close()
    def board_input_result(self,nickname='NoName', score=0):
        global #import the global score here
        leader_board_name = str(nickname).rjust(20)
        leader_board_score = str(score).rjust(10)
        #the content we for one line we put into the screen is leader_board_result
        leader_board_result = leader_board_name+'   '+leader_board_score+'\n'
        #open the file and write the result into txt file
        with self.leader_board as in_file:
            contents = in_file.readlines()
        with open(self.leader_board_path, 'w') as out_file:
            for line in contents:
                if int(line[22:32]) <= score:
                    line = leader_board_result + line
                out_file.write(line)
    def draw_leader_board(self):
        contents=self.leader_board.readlines()
        for line in contents:
            screen



