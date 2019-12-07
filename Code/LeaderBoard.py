LEADER_BOARD_PATH = "./resources/LeaderBoard.txt"
NUMBER_LEADERS_SHOWN = 5

# Function to sort the list of tuples by its second item
def Sort_Tuple(tup):

    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

class LeaderBoard:
    def __init__(self):
        self.leader_board = open(LEADER_BOARD_PATH, 'r')
        self.leader_board.close()
    def board_input_result(nickname='NoName', score=0):
        # Create tuple for current score
        latest_score_tup = (nickname.replace(",",""), score)

        # read file contents into list
        with open(LEADER_BOARD_PATH, 'r') as in_file:
            contents_lst = in_file.readlines()
        list_of_tuples = []

        # If list not empty then write to it
        with open(LEADER_BOARD_PATH, 'w') as out_file:
            if contents_lst:
                for line in contents_lst:
                    # build list tuples
                    this_line_list = line.split(",")
                    # this_line_list[1] = this_line_list[1][:-1]
                    this_line_tuple = (str(this_line_list[0]), int(this_line_list[1]))
                    list_of_tuples.append(this_line_tuple)

            # add latest score to end of list of tuples
            list_of_tuples.append(latest_score_tup)

            # sort list into order
            list_of_tuples = Sort_Tuple(list_of_tuples)

            # remove last line
            if len(list_of_tuples) == NUMBER_LEADERS_SHOWN+1:
                list_of_tuples.pop(NUMBER_LEADERS_SHOWN)
            # Create strings with newline on end from tuples and save to file
            for tup in list_of_tuples:
                tup_as_string = str(tup[0]) + "," + str(tup[1]) + "\n"
                out_file.write(tup_as_string)

        # the new list of leaderboard line strings
        with open(LEADER_BOARD_PATH, 'r') as final_file:
            contents = final_file.readlines()

        return contents






