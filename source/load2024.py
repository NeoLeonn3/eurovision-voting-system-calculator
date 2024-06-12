import json
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

def loadRankings(countryCheck, detailedFinalResults):
  for x in detailedFinalResults:
    if x["country"] == countryCheck.country:
      # print(countryCheck.country)
      breakdown = x["votingBreakdown"]
      for y in breakdown:
        tempCountry = y["country"]
        tempJuryRank = y["juryRank"]
        tempTelevoteRank = y["televotingRank"]
        countryCheck.juryRank.append((tempCountry, tempJuryRank))
        countryCheck.televoteRank.append((tempCountry, tempTelevoteRank))

def data2024(entries, countriesResults):

  entriesFile = open('./data/2024/entries.json',)
  resultsFile = open('./data/2024/results.json',)
  detailedResultsFile = open('./data/2024/detailed_results.json',)

  entriesImport = json.load(entriesFile)
  resultsImport = json.load(resultsFile)
  detailedResultsImport = json.load(detailedResultsFile)

  finalsResults = resultsImport["final"]
  detailedFinalResults = detailedResultsImport["final"]
  # print(finalsResults)

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

  # loadRankings(countriesResults[0], detailedFinalResults)
  print(countriesResults[0].televoteRank)
  # for i in countriesResults:
  #   print("Country: " + i.country + " | In Final: " + str(i.inFinal))

  entriesFile.close()
  resultsFile.close()