# This class describes a year in Eurovision, as in the entries and the results given by each country (check entry.py and countryResults.py for more info)
class Year:
  
  def __init__(self, entries, countriesResults, rowRanking):
    
    # Some identifying details
    self.entries = []
    self.countriesResults = []
    self.rowVoteRanking = []