# Eurovision Song Contest Voting Calculator

A project that calculates final results of the Eurovision Song Contest based on potential alternative voting systems. Currently supports the years 2024, 2023 and 2022.

Special thanks to Reddit user [u/LdyLdn](https://www.reddit.com/user/LdyLdn/) for providing the voting results in JSON format [on their post here](https://www.reddit.com/r/eurovision/comments/1dcth40/i_created_a_eurovision_results_breakdown_website/)

## Purpose  

The main reasons I decided to do this project are two:

* I need to practice Python more therefore I was looking for a project to do
* I am a Eurovision nerd and Eurovision nerds always find reasons to complain about how the voting system sucks because their favourite did not win

The initial idea I had was to test how the results would be if, while we kept the 12 point system for both juries and the public, points were awarded to more countries. Specifically:

```text
1st gets 12
2nd gets 10
3rd gets 8
4th gets 7
5th gets 6
6th to 8th get 5
9th to 11th get 4
12th to 14th get 3
15th to 17th get 2
18th to 20th get 1
21th and below get 0
```

Of course no sane person would calculate this by hand. So I decided to try make a command-line program that can do it. At the same time, I tried to make it in a way that everyone can try their own system.

As I explain later, the Rest of the World vote is not taken into consideration at the moment.

## How it works

In the data folder you will find detailed results for the contest results for the years 2024, 2023 and 2022, meaning the full ranking of each country in the contest (how they ranked the countries that participated in the final, both jury and televote).

In the systems folder you will find the systems we are testing in JSON format. Each JSON object contains a point system for the jury and a point system for the televote (will explain later), including the current system in place (points 1-8, 10, 12 for the first 10 countries). Based on the available systems, the results are calculated. The current system exists here for reference (and as an initial test)

## How to run it

**The current version is a bit early so some things should be fixed in order to accomodate for extra systems to be able to be added, will fix in a later version**

At the current moment it is a command-line Python program. So first of all you need to download and install the latest version of Python from [here](https://www.python.org/downloads/). After that, you of course need to download the program files. After extracting the files, you go to the parent folder, open the command line/terminal and type ```main.py```  

After that, you see a few messages about files being loaded and you are informed about the voting systems that are available (the name of the system, a small description and the filename that contains the voting system inside the systems folder). By selecting a number between 1 and 4 you select the appropriate system (the number displayed at the left) by typing the number. Then you select one of the three years available (2022, 2023 and 2024) by typing the year's number. Then you are asked regarding the name of the file with the exported results (if you choose not to select a filename, the results will be exported in the results.txt file).

After that, the total results and the RoW top 10 (if the year is 2023 or 2024) are printed in the console. The results exported in the text file also include both jury and televote rankings.  

At the moment no detailed results regarding how many points each country got from each country, but it's currently on my plans for the next update.

## The Rest of the World votes issue

All results regarding the rankings can be found in the official Eurovision website, except for the RoW vote, which is televote-only. There are no official detailed results for the Rest of the World vote in 2023 and 2024 (the years where it was introduced), which means the only official results we have is the top 10.

For now I decided to omit the RoW vote. I could not think of any way that felt right. My original reason for making this project was to calculate results based on more countries getting points. And, to be honest, I do not think that the RoW results will make a significant difference to the final results. The RoW vote is mostly a symbolic vote whose purpose is ~~EBU making more money~~ to make Eurovision fans from non-participating countries feel included.

In the results I calculated for 2024 (to-do: calculate 2023) with the current system, the only difference I noticed in placements was that Ukraine and France both scored 443 points. The tiebreak rules state:

```text
The winner of a tie is the country that received more points from the televoting, then the country that received points from more countries in the televoting, then the country that received more 12 points in the televoting, then 10 points, all the way down to 1. If the tie cannot be broken in this way, the country that performed earlier wins the tie. 
```

And with Ukraine getting more points from the televote than France, Ukraine would still be ahead of France on 3rd place.

In the final result returned, I present the top 10 of the RoW vote (as part of the year data) so that if you wish to calculate the results you can do it on your own.

## Important notes

* The systems provided take into consideration that 26 countries are participating in the final, which is the maximum amount (the Big 5, the host/winner from the previous year and 10 countries from each semifinal). However, out of the cases we examine:

  * Due to Italy (a member of the Big 5) winning and thus hosting the 2022 contest, 25 countries are participating in the final.
  * In 2024, the Netherlands were disqualified from the final due to an EBU decision regarding an incident involving the Dutch singer Joost Klein, therefore we have 25 countries participating in the final. With results from the juries existing for the Netherlands due to their participation in the jury show the day before the final (through their semifinal performance), it should be noted that the code regarding the 2024 jury calculations is also slightly different in order to not include the Netherlands.  

  Therefore in years with 25 countries, the 26th place result in each system is excluded

## To-Do List

* Add detailed voting results in the exported results (how many points each country got from each country)
* Create Python notebooks to compare results with the current system
* Export results (probably to JSON or CSV/TSV)
* Take into consideration the tie-breakers
* Create a GUI version that is more user-friendly
* Add future years (as long as I have detailed results for them)
* Add reverse ranking  
In the reverse ranking system, the countries that had the worst positions get points based on the current system (12 points to last, 10 to second-from-last, etc). Due to what I mention in Important Note #2, just making a JSON file with reverse results would not work, therefore calculation will be dealt with differently
* Netherlands 2024 jury results  
Although I mentioned that for year 2024 the Netherlands are ignored due to their disqualification, I might consider making an option to calculate their jury points under the different systems provided

## Things I am not planning to do

* Support other years (other than the future ones)  
Creating the data files for previous years would require either a lot of time to do so manually or research to find out how it would be. You are free to provide the data if you want and you will be included in the special thanks message at the start of this README file.

* Support for the semi-finals  
Although the data for the semifinals is provided, I do not intend to use it for any calculations. There hasn't been any case yet where I am personally interested in making calculations for the semis under different systems.

* "Can you test a x/y jury/televote split?"  
I do not like how the conversation regarding a different televote split is done. The current system is 50/50 (with a bit of televote favour due to the extra set of 12 points given by the RoW vote). The majority of times people calculate the results under different splits they just adjust the final points. This is an easy calculation that you can do yourself. This tool is designed for more sophisticated calculations regarding potential televote systems. But you are free to create your own voting system by creating a new JSON file in they systems folder and adjusting the points given by jury and televote as you wish.

* "Can you calculate results if x country had sent y song instead of z?"  
I am not Dr. Strange or anyone with similar powers, therefore I cannot calculate how results would be in another parallel universe where your fav from a national final that failed to win actually managed to win.
