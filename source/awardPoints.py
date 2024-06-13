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
  
  # Make the object we return, contains countries and their points (jury, televote, total)
  for x in yearData.entries:
    
    # Get the jury score
    entryTuple = (x.country, x.juryTotal)
    wantedResults.juryRanking.append(entryTuple)
    
    # Get the televote score
    entryTuple = (x.country, x.televoteTotal)
    wantedResults.televoteRanking.append(entryTuple)
    
    # Get the total score
    x.totalScore = x.juryTotal + x.televoteTotal
    entryTuple = (x.country, x.totalScore)
    wantedResults.totalRanking.append(entryTuple)
    
  # Sort the results
  wantedResults.juryRanking = sorted(wantedResults.juryRanking, key=lambda x: x[1], reverse=True)
  wantedResults.televoteRanking = sorted(wantedResults.televoteRanking, key=lambda x: x[1], reverse=True)
  wantedResults.totalRanking = sorted(wantedResults.totalRanking, key=lambda x: x[1], reverse=True)
  # Including the RoW vote
  yearData.rowVoteRanking = sorted(yearData.rowVoteRanking, key=lambda x: x[1])
  
  # for i in wantedResults:
  #   print("Country: " + i[0] + " | Jury score: " + str(i[1]))
  
  # Close the file
  votingSystemFile.close()
  