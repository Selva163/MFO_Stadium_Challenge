# MFO_Stadium_Challenge

Objective is to allocate stadiums for each of the matches for the given constraints

following are the inputs we may need to adjust as per our requirements ( from line 5 to line 20 in MFO_Stadium_Challenge.py file)

#number of teams

n = 7

#number of matches

m = 11

#number of stadiums available to host

k = 3

#amount of money MFO will earn for each team

mfo_earning = [4,7,8,10,10,9,3]

#the teams that can play the 𝑖-th game

matches_played = [(6,2), (6,1), (7,6), (4,3), (4,6), (3,1), (5,3), (7,5), (7,3), (4,2), (1,4)]

#difference between max and min of a team played in the available stadiums

max_min_difference = 2

once the parameters are adjusted, then run the following command (python 3):

python.exe .\MFO_Stadium_Challenge.py

the output will be the matches and stadium assigned for each matches

Problem Solved Status: Optimal

Matches and stadiums

(6, 2) 3

(6, 1) 2

(7, 6) 3

(4, 3) 3

(4, 6) 2

(3, 1) 2

(5, 3) 2

(7, 5) 1

(7, 3) 3

(4, 2) 1

(1, 4) 3

Objective maximized: 163.0
