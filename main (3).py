class Player:
  def play(self):
    print("The Player is playing cricket.")

class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The Bowler is bowling.")

#creating objects of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()

#calling the play() method for each object
batsman.play()
bowler.play()
    