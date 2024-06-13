# Imports
import json
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

def awardPoints(yearData, systemUsed):
  
  # Load the voting system used
  systemPath = "systems/" + systemUsed
  votingSystemFile = open(systemPath,)
  
  votingSystemImport = json.load(votingSystemFile)
  jurySystem = votingSystemImport["jury"]
  televoteSystem = votingSystemImport["televote"]
  
  # for i in range(0, len(jurySystem)):
  #   print(jurySystem[str(i+1)])
  
  for x in yearData.countriesResults:
    # Get the jury ranks
    for i in range(0, len(x.juryRank)):
      # print(x.juryRank)
      if jurySystem[str(i+1)] != 0:
        juryTuple = (x.country, jurySystem[str(i+1)])
        
        # print(yearData.entries[index].country)
        
      
    
  
  votingSystemFile.close()
  