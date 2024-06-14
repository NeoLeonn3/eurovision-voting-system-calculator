# Imports
import json
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

# Helper function called by the data2024() function in order to load the rankings of each participating country
def loadRankings(countryCheck, detailedFinalResults):
  for x in detailedFinalResults:
    if x["country"] == countryCheck.country:
      # print(countryCheck.country)
      breakdown = x["votingBreakdown"]
      for y in breakdown:
        tempCountry = y["country"]
        
        # Get and sort Jury Rank
        tempJuryRank = y["juryRank"]
        tempTelevoteRank = y["televotingRank"]
        countryCheck.juryRank.append((tempCountry, tempJuryRank))
        countryCheck.televoteRank.append((tempCountry, tempTelevoteRank))

  # Jury sort
  countryCheck.juryRank = sorted(countryCheck.juryRank, key=lambda x: x[1])

  # Televote sort
  countryCheck.televoteRank = sorted(countryCheck.televoteRank, key=lambda x: x[1])
  

# The function we call in order to load the entries of the final and each participating country's rankings
def loadYearData(entries, countriesResults, rowRanking, year):
  
  entriesString = "./data/" + year + "/entries.json"
  resultsString = "./data/" + year + "/results.json"
  detailedResultsString = "./data/" + year + "/detailed_results.json"

  # Load the JSON files and save the data needed
  entriesFile = open(entriesString, encoding='UTF-8')
  resultsFile = open(resultsString, encoding='UTF-8')
  detailedResultsFile = open(detailedResultsString, encoding='UTF-8')
  entriesImport = json.load(entriesFile)
  resultsImport = json.load(resultsFile)
  detailedResultsImport = json.load(detailedResultsFile)
  finalsResults = resultsImport["final"]
  detailedFinalResults = detailedResultsImport["final"]

  # Load the countries and save the ones that participate in the final
  for x in entriesImport:
    index = -1
    for y in finalsResults:
      if x["country"] == y["country"]:
        entries.append(Entry(x["country"], x["song"], x["participant"]))
        countriesResults.append(CountryResults(x["country"], True))
        loadRankings(countriesResults[-1], detailedFinalResults)
        index = finalsResults.index(y)
    if index != -1:
      finalsResults.pop(index)
    else:
      countriesResults.append(CountryResults(x["country"], False))
      loadRankings(countriesResults[-1], detailedFinalResults)
  
  # Find the Rest of the World ranking, the last on the detailedFinalResults (buto nly if the year is 2023)
  if year == "2023":
    rowResults =  detailedFinalResults[-1]["votingBreakdown"]
    for x in rowResults:
      if x["televotingRank"] != -1 and x["televotingRank"] != None:
        rowRanking.append((x["country"], x["televotingRank"]))
  
  # Close the files
  entriesFile.close()
  resultsFile.close()
  detailedResultsFile.close()