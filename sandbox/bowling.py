class Bowling:

    def __init__(self, game):
        self.game = game
        self.score = 0

    def process_frame(self, frame):
        self.frame_score = 0
        if self.strike:
            self.frame_score = 1
        if self.spare:

        self.strike = True if 'X' in frame else False
        self.spare = True if '/' in frame else False
        if not self.strike and not self.spare:
            if frame[0] != '-':
                self.frame_score += frame[0]
            if frame[1] != '-':
                self.frame_score += frame[1]
            self.score += self.frame_score



if __name__ == '__main__':

    bowl = Bowling()
    # (12 rolls: 12 strikes) = 10 frames * 30 points = 300
    game = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    calc_bowling(game)
    # (20 rolls: 10 pairs of 9 and miss) = 10 frames * 9 points = 90
    game = ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-']
    calc_bowling(game)
    # (21 rolls: 10 pairs of 5 and spare, with a final 5) = 10 frames * 15 points = 150
    game = ['5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5']
    calc_bowling(game)
