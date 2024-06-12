# This class describes the results by each country.

class CountryResults:
  
  def __init__(self, country, inFinal):
    
    # The name of the country and whether they participate in the final or not
    self.country = country
    self.inFinal = inFinal
    
    # Two lists that describe the jury and televote ranks
    self.juryRank = []
    self.televoteRank = []