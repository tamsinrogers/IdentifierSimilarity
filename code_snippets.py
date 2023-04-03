# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment

# -------------------------------------------------------------------------- #
# SNIPPET 1: MOST AND LEAST HOLES IN ONE
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES (ORTHOGRAPHICAL)
def mini_golf_results(player_list, scorecard_list):
    l = len(player_list)
    most_holes = 0 # sum1
    least_holes = 1e9 # sum2
    most_holes_player = "" # player1
    least_holes_player = "" # player2
    for i in range(l):
        k = len(scorecard_list[i])
        num_hole_in_ones = 0
        for j in range(k):
            if scorecard_list[i][j] == 1:
                num_hole_in_ones += 1
        if num_hole_in_ones > most_holes:
            most_holes_player = player_list[i]
            most_holes = num_hole_in_ones
        if num_hole_in_ones < least_holes:
            least_holes_player = player_list[i]
            least_holes = num_hole_in_ones

    return most_holes_player, least_holes_player

print(
    str(
        mini_golf_results(
            ["Fred", "Ron", "Ginny", "George"],
            [
                [1, 2, 4, 3, 1, 1, 3],
                [4, 2, 1, 1, 1, 3, 1],
                [6, 2, 1, 3, 4, 3, 2],
                [1, 2, 3, 2, 3, 4, 4]
            ]    
        )
    )
    # SHOULD PRINT (Ron, Ginny)
)