# Imports

import json
from classes.entry import *
from classes.countryResults import *

entriesFile = open('./data/2024/entries.json',)
resultsFile = open('./data/2024/results.json',)
detailedResultsFile = open('./data/2024/detailed_results.json',)

entriesImport = json.load(entriesFile)
resultsImport = json.load(resultsFile)

finalsResults = resultsImport["final"]
# print(finalsResults)
entries = []
countriesResults = []

for x in entriesImport:
  index = -1
  for y in finalsResults:
    if x["country"] == y["country"]:
      entries.append(Entry(x["country"], x["song"], x["participant"]))
      countriesResults.append(CountryResults(x["country"], True))
      index = finalsResults.index(y)
  if index != -1:
    finalsResults.pop(index)
  else:
    countriesResults.append(CountryResults(x["country"], False))

for i in countriesResults:
  print("Country: " + i.country + " | In Final: " + str(i.inFinal))

# temp = Entry(entriesImport[1]["country"], entriesImport[1]["song"], entriesImport[1]["participant"])

# print(temp.participant)

entriesFile.close()
resultsFile.close()