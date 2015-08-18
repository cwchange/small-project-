import random
class game:
        def __init__(self):
                self.comp_score=0
                self.player_score=0
                self.draw=0
                self.move=['rock', 'paper', 'scissors']

        def game_on(self, player_move):
                comp_move=random.choice(self.move)
                if (player_move == comp_move):
                        self.draw += 1
                elif (player_move == 'rock' and  comp_move != 'paper') or (player_move == 'paper' and comp_move != 'scissors') or (player_move == 'scissors' and comp_move != 'rock'):
                        self.player_score += 1
                else:
                        self.comp_score +=1
                print "Your move: %s / Computer move: %s" %(player_move, comp_move)

if __name__ == '__main__':
        temp=game()
        while True:
                move=raw_input("Please choice your move: r=rock, p=paper, s=scissors, e=end game: ")
                if (move == 'e'):
                        break;
                elif (move == 'r'):
                        temp.game_on('rock')
                elif (move == 'p'):
                        temp.game_on('paper')
                elif (move == 's'):
                        temp.game_on('scissors')
                else:
                        print "Please enter only r, p, s, or e to play"
                        continue
                print "Player: %s / Computer: %s / Draw: %s" %(temp.player_score, temp.comp_score, temp.draw)
