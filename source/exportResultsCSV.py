import csv
import datetime
import os

from source.load2024 import *
from source.display import clearScreen
from source.loadYear import *
from source.loadSystems import *
from source.inputSelectors import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *


def exportResultsCSV(yearData, results, yearNumber, systemName):
  
  # create folder exports if it doesn't exist
  if not os.path.exists("exports"):
    os.makedirs("exports")
    
  systemUsed = os.path.splitext(systemName)[0]
  
  juryFilename = f"exports/{systemUsed}_{yearNumber}_jury_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
  televoteFilename = f"exports/{systemUsed}_{yearNumber}_televote_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
  totalFilename = f"exports/{systemUsed}_{yearNumber}_total_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
  if yearNumber > 2022:
      rowFilename = f"exports/{systemUsed}_{yearNumber}_row_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
  
  juryFile = open(juryFilename, "w", encoding='utf-8', newline='')
  televoteFile = open(televoteFilename, "w", encoding='utf-8', newline='')
  totalFile = open(totalFilename, "w", encoding='utf-8', newline='')
  if yearNumber > 2022:
    rowFile = open(rowFilename, "w", encoding='utf-8', newline='')
  
  # Jury results
  juryWriter = csv.writer(juryFile)
  juryWriter.writerow(["place", "country", "songName", "songPerformer", "points"])
  for x in results.juryRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        juryWriter.writerow([str(results.juryRanking.index(x) + 1), y.country, y.song, y.participant, str(x[1])])

  # Televote results
  televoteWriter = csv.writer(televoteFile)
  televoteWriter.writerow(["place", "country", "songName", "songPerformer", "points"])
  for x in results.televoteRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        televoteWriter.writerow([str(results.televoteRanking.index(x) + 1), y.country, y.song, y.participant, str(x[1])])

  # Total results
  totalWriter = csv.writer(totalFile)
  totalWriter.writerow(["place", "country", "songName", "songPerformer", "points"])
  for x in results.totalRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        totalWriter.writerow([str(results.totalRanking.index(x) + 1), y.country, y.song, y.participant, str(x[1])])

  if yearNumber > 2022:
      # Row results
      rowWriter = csv.writer(rowFile)
      rowWriter.writerow(["place", "country", "songName", "songPerformer"])
      for x in yearData.rowVoteRanking:
        for y in yearData.entries:
          if x[0] == y.country:
            rowWriter.writerow([str(yearData.rowVoteRanking.index(x) + 1), y.country, y.song, y.participant])

  juryFile.close()
  televoteFile.close()
  totalFile.close()
  if yearNumber > 2022:
    rowFile.close()
    
  clearScreen()
  print("+----------------------------------------------------+")
  print("|     Eurovision Song Contest Voting Calculator      |")
  print("+----------------------------------------------------+")
  print("Results exported to the following files:")
  print("Jury results: "+juryFilename)
  print("Televote results: "+televoteFilename)
  print("Total results: "+totalFilename)
  if yearNumber > 2022:
    print("Rest of the World results: "+rowFilename)
  input("Press Enter to continue...")
  
  
  
    