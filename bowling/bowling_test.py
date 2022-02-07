import unittest

from bowling import (
    BowlingGame,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class BowlingTest(unittest.TestCase):
    def roll_new_game(self, rolls):
        game = BowlingGame()
        for roll in rolls:
            game.roll(roll)
        return game

    def test_should_be_able_to_score_a_game_with_all_zeros(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 0)

    def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
        #           1     2     3     4     5     6     7     8     9    10
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 90)

    def test_a_spare_followed_by_zeros_is_worth_ten_points(self):
        #       spare
        #           1     2     3     4     5     6     7     8     9    10
        rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward - score at 2nd frame is 0
        #            score at 1st frame is 10 + 0
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 10)

    def test_points_scored_in_the_roll_after_a_spare_are_counted_twice(self):
        #       spare
        #           1     2     3     4     5     6     7     8     9    10
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward - score at 2nd frame is 3
        #            score at 1st frame is 10 + 3
        # total 16
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 16)

    def test_consecutive_spares_each_get_a_one_roll_bonus(self):
        #           1     2     3     4     5     6     7     8     9    10
        rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward: at frame 3 = 4
        # at frame 2           = 10 + 4 = 14
        # at frame 1           = 10 + 3 = 13
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 31)

    # this one
    def test_a_spare_in_the_last_frame_gets_a_one_roll_bonus_that_is_counted_once(self):
        #           1     2     3     4     5     6     7     8     9    10
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]
        # backward: one roll bonus => 7
        # at frame 10   = 10 + 7  = 17
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 17)

    def test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll(self):
        #         1     2     3     4     5     6     7     8     9    10
        rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward: all frame but first = 0
        # 1st frame 10 == 10
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 10)

    def test_points_scored_in_the_two_rolls_after_a_strike_are_counted_twice_as_a_bonus(
        self,
    ):
        #         1     2     3     4     5     6     7     8     9    10
        rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward: all frames but 2nd and 1st == 0
        # 2nd frame == 8
        # 1st (strike) 10 + 5 + 3 = 18
        # total == 26
        # another way: 10 + 2x5 + 2x3 = 26
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 26)

    def test_consecutive_strikes_each_get_the_two_roll_bonus(self):
        #         1   2   3     4     5     6     7     8     9    10
        rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # backward: all frames but 4th, 3rd 2nd adn 1st == 0
        # frame 4 ==  5+3         ==  8
        # frame 3 == 10 + 5+3     == 18
        # frame 2 == 10 + 10 + 5  == 25
        # frame 1 == 10 + 10 + 10 == 30
        # tot 81
        game = self.roll_new_game(rolls)
        #      (5 + 3)   ==  8
        # (10 + 5 + 3)   == 18
        # (10 + 10 + 5)  == 25
        # (10 + 10 + 10) == 30
        #
        self.assertEqual(game.score(), 81)

    def test_a_strike_in_the_last_frame_gets_a_two_roll_bonus_that_is_counted_once(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 1]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 18)

    # looks like a strike scenario?
    def test_rolling_a_spare_with_the_two_roll_bonus_does_not_get_a_bonus_roll(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 3]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 20)

    def test_strikes_with_the_two_roll_bonus_do_not_get_bonus_rolls(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 30)

    def test_a_strike_with_the_one_roll_bonus_after_a_spare_in_the_last_frame_does_not_get_a_bonus(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 10]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 20)

    def test_all_strikes_is_a_perfect_game(self):
        #         1   2   3   4   5   6   7   8   9  10  <fill>
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # len == 12
        game = self.roll_new_game(rolls)
        # 10 x (10 + 10 +_10)
        self.assertEqual(game.score(), 300)

    def test_rolls_cannot_score_negative_points(self):
        rolls = []
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(-1)

    def test_a_roll_cannot_score_more_than_10_points(self):
        rolls = []
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(11)

    def test_two_rolls_in_a_frame_cannot_score_more_than_10_points(self):
        rolls = [5]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(6)

    def test_bonus_roll_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points(
        self,
    ):
        #           1     2     3     4     5     6     7     8     9  10
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(11)

    def test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 5]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(6)

    def test_two_bonus_rolls_after_a_strike_in_the_last_frame_can_score_more_than_10_points_if_one_is_a_strike(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 6]
        game = self.roll_new_game(rolls)
        self.assertEqual(game.score(), 26)

    def test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike(
        self,
    ):
        #           1     2     3     4     5     6     7     8     9  10
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(10)

    def test_second_bonus_roll_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points(
        self,
    ):
        #                                  10                              20 impossible all pins are already down
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(11)

    def test_an_unstarted_game_cannot_be_scored(self):
        rolls = []
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.score()

    def test_an_incomplete_game_cannot_be_scored(self):
        rolls = [0, 0]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.score()

    def test_cannot_roll_if_game_already_has_ten_frames(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(0)

    def test_bonus_rolls_for_a_strike_in_the_last_frame_must_be_rolled_before_score_can_be_calculated(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.score()

    def test_both_bonus_rolls_for_a_strike_in_the_last_frame_must_be_rolled_before_score_can_be_calculated(
        self,
    ):
        #           1     2     3     4     5     6     7     8     9  10  11 # missing fill
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.score()

    def test_bonus_roll_for_a_spare_in_the_last_frame_must_be_rolled_before_score_can_be_calculated(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.score()

    def test_cannot_roll_after_bonus_roll_for_spare(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 2]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(2)

    def test_cannot_roll_after_bonus_rolls_for_strike(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 2]
        game = self.roll_new_game(rolls)
        with self.assertRaisesWithMessage(Exception):
            game.roll(2)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
