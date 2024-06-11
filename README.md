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

## How it works

In the data folder you will find detailed results for the contest results for the years 2024, 2023 and 2022, meaning the full ranking of each country in the contest (how they ranked the countries that participated in the final, both jury and televote).

In the systems folder you will find the systems we are testing in JSON format. Each JSON object contains a point system for the jury and a point system for the televote (will explain later), including the current system in place (points 1-8, 10, 12 for the first 10 countries). Based on the available systems, the results are calculated. The current system exists here for reference (and as an initial test)

You run the program through the command line (to-do: instructions), you select one of the supported years and then you select one of the available systems.

## Important notes

* There are no official detailed results for the Rest of the World vote in 2023 and 2024 (the years where it was introduced), therefore any calculation is done with RoW points given under the current system.

## To-Do List

* Build the actual program
* Create Python notebooks to compare results with the current system
* Create a GUI version that is more user-friendly
* Add future years (as long as I have detailed results for them)

## Things I am not planning to do

* Support other years (other than the future ones)  
Creating the data files for previous years would require either a lot of time to do so manually or research to find out how it would be. You are free to provide the data if you want and you will be included in the special thanks message at the start of this README file.

* Support for the semi-finals  
Although the data for the semifinals is provided, I do not intend to use it for any calculations. There hasn't been any case yet where I am personally interested in making calculations for the semis under different systems.

* "Can you test a x/y jury/televote split?"  
I do not like how the conversation regarding a different televote split is done. The current system is 50/50 (with a bit of televote favour due to the extra set of 12 points given by the RoW vote). The majority of times people calculate the results under different splits they just adjust the final points. This is an easy calculation that you can do yourself. This tool is designed for more sophisticated calculations regarding potential televote systems. But you are free to create your own voting system by creating a new JSON file in they systems folder and adjusting the points given by jury and televote as you wish.
