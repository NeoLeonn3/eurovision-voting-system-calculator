# Imports
import json
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

def awardPoints(yearData, systemUsed, wantedResults):
  
  # Load the voting system used
  systemPath = "systems/" + systemUsed
  votingSystemFile = open(systemPath,)
  
  votingSystemImport = json.load(votingSystemFile)
  jurySystem = votingSystemImport["jury"]
  televoteSystem = votingSystemImport["televote"]
  
  # for i in range(0, len(jurySystem)):
  #   print(jurySystem[str(i+1)])
  
  # Get the points
  for x in yearData.countriesResults:  
    # Get the jury ranks
    for i in range(0, len(x.juryRank)):
      # print(x.juryRank)
      if jurySystem[str(i+1)] != 0:
        juryTuple = (x.country, jurySystem[str(i+1)])
        for j in yearData.entries:
          if j.country == x.juryRank[i][0]:
            j.jury.append(juryTuple)
            j.juryTotal += jurySystem[str(i+1)]
        # print(juryTuple)
    
    # Get the televote results.
    for i in range(0, len(x.televoteRank)):
      # print(x.televoteRank)
      if televoteSystem[str(i+1)] != 0:
        televoteTuple = (x.country, televoteSystem[str(i+1)])
        for j in yearData.entries:
          if j.country == x.televoteRank[i][0]:
            j.televote.append(televoteTuple)
            j.televoteTotal += televoteSystem[str(i+1)]
        # print(televoteTuple)
  
  # Make the list we return, contains countries and their total points  
  for x in yearData.entries:
    # Get the total score
    x.totalScore = x.juryTotal + x.televoteTotal
    entryTuple = (x.country, x.totalScore)
    wantedResults.append(entryTuple)
  
  # wantedResults = sorted(wantedResults, key=lambda x: x[1], reverse=True)
  
  # for i in wantedResults:
  #   print("Country: " + i[0] + " | Jury score: " + str(i[1]))
  
  # Close the file
  votingSystemFile.close()
  