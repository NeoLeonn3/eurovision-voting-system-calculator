# This class describes an Entry, with each Entry being an entry to the contest, with some details and their scores

class Entry:
  
  def __init__(self, country, song, participant):
    
    # Some identifying details
    self.country = country
    self.song = song
    self.participant = participant
    
    # Entry's jury score, both the total and a list of the scores received from each country
    self.jury = []
    self.juryTotal = 0
    
    # Entry's televote score, both the total and a list of the scores received from each country
    self.televote = []
    self.televoteTotal = 0