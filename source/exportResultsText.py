# Deprecated, changed with exportResultsCSV.py

# Imports
from source.load2024 import *
from source.loadYear import *
from source.loadSystems import *
from source.inputSelectors import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *

def exportToFile(filename, yearData, results, yearNumber, systemUsed):
  
  file = open(filename, 'w', encoding='utf-8')
  
  # First line of the file
  file.write("Results for year + " + str(yearNumber) + " by using the \'" + systemUsed + "\' voting system")
  file.write("\n")
  
  file.write("\n")
  file.write("\n")
  
  # Print the jury results
  file.write("Jury Results:")
  file.write("\n")
  file.write("Place | Country | Song Name | Song Performer | Points")
  file.write("\n")
  for x in results.juryRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        file.write(str(results.juryRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]) + "\n")
  
  file.write("\n")
  file.write("\n")
  file.write("\n") 
  
  # Print the televote results
  file.write("Televote Results:")
  file.write("\n")
  file.write("Place | Country | Song Name | Song Performer | Points")
  file.write("\n")
  for x in results.televoteRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        file.write(str(results.televoteRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]) + "\n")
  
  file.write("\n")
  file.write("\n") 
  file.write("\n") 
  
  # Print the total results
  file.write("Total Results:")
  file.write("\n") 
  file.write("Place | Country | Song Name | Song Performer | Points")
  file.write("\n") 
  for x in results.totalRanking:
    for y in yearData.entries:
      if x[0] == y.country:
        file.write(str(results.totalRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]) + "\n")
  
  file.write("\n")
  file.write("\n")
  file.write("\n") 
       
  # Print the rest of the world top 10 (just like above but without the points) if the yearNumber is 2023 or 2024
  if yearNumber == 2023 or yearNumber == 2024:
    file.write("Rest of the World Top 10:")
    file.write("\n")
    file.write("Place | Country | Song Name | Song Performer")
    file.write("\n")
    for x in yearData.rowVoteRanking:
      for y in yearData.entries:
        if x[0] == y.country:
          file.write(str(yearData.rowVoteRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + "\n")
  
  file.write("\n")
  file.write("\n")
  file.write("\n") 
  
