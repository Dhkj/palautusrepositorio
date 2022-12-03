class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.won_point_by_player1()
        elif player_name == "player2":
            self.won_point_by_player2()

    def won_point_by_player1(self):
        self.player1_score = self.player1_score + 1

    def won_point_by_player2(self):
        self.player2_score = self.player2_score + 1

    def scores_are_equal(self):
        return self.player1_score == self.player2_score

    def either_player_scored_over_forty(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def get_difference_in_scores_as_player1_lead(self):
        return self.player1_score - self. player2_score

    def get_score(self):
        if self.scores_are_equal():  #self.player1_score == self.player2_score:
            return self.get_even_score_as_string(self.player1_score)
        elif self.either_player_scored_over_forty():
            difference_in_scores_as_player1_lead = self.get_difference_in_scores_as_player1_lead()
            return self.get_uneven_forty_or_over_score_as_string(difference_in_scores_as_player1_lead)
        else:
            return self.get_uneven_score_under_forty_as_string()
            #self.get_player1_score_as_a_string()
    """
    def get_even_score_as_string(self, player_score):
        player_score_as_a_string = self.get_player_score_as_a_string(player_score)
        
        return player_score_as_a_string + "-All"

        #return self.get_player_score_as_a_string(player_score) + "-All"
    """
    def get_even_score_as_string(self, player_score):
        #return self.get_player_score_as_a_string(player_score)



        score_string = ""

        #if self.score == self.player2_score:

        if player_score == 0:
            score_string = "Love-All"
        elif player_score == 1:
            score_string = "Fifteen-All"
        elif player_score == 2:
            score_string = "Thirty-All"
        elif player_score == 3:
            score_string = "Forty-All"
        else:
            score_string = "Deuce"

        return score_string

    def get_uneven_forty_or_over_score_as_string(self, lead_for_player1):
        if lead_for_player1 == 1:
            return "Advantage player1"
        elif lead_for_player1 == -1:
            return "Advantage player2"
        elif lead_for_player1 >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def get_uneven_score_under_forty_as_string(self):
        return self.get_player_score_as_a_string(self.player1_score) + "-" + self.get_player_score_as_a_string(self.player2_score)


    def get_player_score_as_a_string(self, player_score):
        if player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        elif player_score == 3:
            return "Forty"





    """
    def get_even_score_as_string(self, player_score):
        #return self.get_player_score_as_a_string(player_score)



        score_string = ""

        #if self.score == self.player2_score:

        if player_score == 0:
            score_string = "Love-All"
        elif player_score == 1:
            score_string = "Fifteen-All"
        elif player_score == 2:
            score_string = "Thirty-All"
        elif player_score == 3:
            score_string = "Forty-All"
        else:
            score_string = "Deuce"

        return score_string
    """


    """
    def get_uneven_forty_or_over_score_as_string(self, lead_for_player1):
        if lead_for_player1 == 1:
            return "Advantage player1"
        elif lead_for_player1 == -1:
            return "Advantage player2"
        elif lead_for_player1 >= 2:
            return "Win for player1"
        else:
            return "Win for player2"






    def get_player_score_as_a_string(self, player_score):
        if player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        elif player_score == 3:
            return "Forty"




    def get_uneven_score_under_forty_as_string(self):
        return self.get_player_score_as_a_string(self.player1_score) + "-" + self.get_player_score_as_a_string(self.player2_score)







    def scores_are_equal(self):
        return self.player1_score == self.player2_score

    def either_player_scored_over_forty(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def get_difference_in_scores_as_player1_lead(self):
        return self.player1_score - self. player2_score





    def get_score(self):
        if self.scores_are_equal():  #self.player1_score == self.player2_score:
            return self.get_even_score_as_string(self.player1_score)
        elif self.either_player_scored_over_forty():
            difference_in_scores_as_player1_lead = self.get_difference_in_scores_as_player1_lead()
            return self.get_uneven_forty_or_over_score_as_string(difference_in_scores_as_player1_lead)
        else:
            return self.get_uneven_score_under_forty_as_string()
            #self.get_player1_score_as_a_string()
    """



"""
    def get_score(self):
        score_string = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                score_string = "Love-All"
            elif self.player1_score == 1:
                score_string = "Fifteen-All"
            elif self.player1_score == 2:
                score_string = "Thirty-All"
            elif self.player1_score == 3:
                score_string = "Forty-All"
            else:
                score_string = "Deuce"



        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score

            if minus_result == 1:
                score_string = "Advantage player1"
            elif minus_result == -1:
                score_string = "Advantage player2"
            elif minus_result >= 2:
                score_string = "Win for player1"
            else:
                score_string = "Win for player2"






        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score_string = score_string + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score_string = score_string + "Love"
                elif temp_score == 1:
                    score_string = score_string + "Fifteen"
                elif temp_score == 2:
                    score_string = score_string + "Thirty"
                elif temp_score == 3:
                    score_string = score_string + "Forty"

        return score_string
"""
"""
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.score = self.score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score_string = ""
        temp_score = 0

        if self.score == self.player2_score:
            if self.score == 0:
                score_string = "Love-All"
            elif self.score == 1:
                score_string = "Fifteen-All"
            elif self.score == 2:
                score_string = "Thirty-All"
            elif self.score == 3:
                score_string = "Forty-All"
            else:
                score_string = "Deuce"
        elif self.score >= 4 or self.player2_score >= 4:
            minus_result = self.score - self. player2_score

            if minus_result == 1:
                score_string = "Advantage player1"
            elif minus_result == -1:
                score_string = "Advantage player2"
            elif minus_result >= 2:
                score_string = "Win for player1"
            else:
                score_string = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.score
                else:
                    score_string = score_string + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score_string = score_string + "Love"
                elif temp_score == 1:
                    score_string = score_string + "Fifteen"
                elif temp_score == 2:
                    score_string = score_string + "Thirty"
                elif temp_score == 3:
                    score_string = score_string + "Forty"

        return score_string
"""