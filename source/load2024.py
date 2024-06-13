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

  # Jury sort: We sort the countries based on their jury ranking
  # Remove Netherlands (Sorry Joost :( )
  countryCheck.juryRank = [entry for entry in countryCheck.juryRank if entry[0] != "Netherlands"]
  # Sort the remaining tuples based on the second element
  sorted_eurovision_results1 = sorted(countryCheck.juryRank, key=lambda x: x[1])
  # Reassign rankings to ensure they are continuous
  countryCheck.juryRank = [(country, rank + 1) for rank, (country, _) in enumerate(sorted_eurovision_results1)]
  
  # Televote sort: Just like the jury one (Again sorry Joost :( )
  countryCheck.televoteRank = [entry for entry in countryCheck.televoteRank if entry[0] != "Netherlands"]
  sorted_eurovision_results2 = sorted(countryCheck.televoteRank, key=lambda x: x[1])
  countryCheck.televoteRank = [(country, rank + 1) for rank, (country, _) in enumerate(sorted_eurovision_results2)]

# The function we call in order to load the entries of the final and each participating country's rankings
def data2024(entries, countriesResults):

  # Load the JSON files and save the data needed
  entriesFile = open('./data/2024/entries.json',)
  resultsFile = open('./data/2024/results.json',)
  detailedResultsFile = open('./data/2024/detailed_results.json',)
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
  
  # Close the files
  entriesFile.close()
  resultsFile.close()