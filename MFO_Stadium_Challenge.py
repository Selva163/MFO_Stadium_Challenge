#import pulp package for optimization
from pulp import *

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

#teams available
teams = range(1, n+1)

#stadiums available
stadiums = range(1, k+1)

#match numbers
matches = range(1, m+1)

#creating the optimization problem
mfo_lp_problem = pulp.LpProblem("MFO", pulp.LpMaximize)

'''lets consider all the matches being played at all stadium. this is a binary variable. 
if 1 - then the match is played at the stadium if 0 - then the match is not played at the stadium'''
sMS = pulp.LpVariable.dicts("sMS", (matches_played,stadiums),lowBound=0,upBound=1, cat = 'Integer')

#Objective of the problem - to maximize the earnings of MFO
mfo_lp_problem += lpSum([mfo_earning[t-1] * sMS[mp][s] for s in stadiums for mp in matches_played 
                        for t in teams if t in mp])

#constraint to set the number of matches played is equal to the number of matches given.
mfo_lp_problem += lpSum([sMS[mp][s] for s in stadiums for mp in matches_played]) == m, "Maximum_number_of_matches"

#constraint to make sure a match is played at only one of the stadium
for mpp in matches_played:
    mfo_lp_problem += lpSum([sMS[mpp][s] for s in stadiums]) == 1, ""

#constraint to check for each team t, the absolute difference between the maximum and minimum matches played in stadiums <= 2 
for t in teams:
    for s1 in stadiums:
        for s2 in stadiums:
            mfo_lp_problem += (lpSum([sMS[mp][s1] for mp in matches_played if t in mp]) - 
            lpSum([sMS[mp][s2] for mp in matches_played if t in mp])) <= max_min_difference


#solve the problem for the given objective and constraints
mfo_lp_problem.solve()

#Debugging file to check objective and constraints
mfo_lp_problem.writeLP("Debug.lp")

#checking the problem solved status
print(LpStatus[mfo_lp_problem.status])

#print the match and stadium
for ms in matches_played:
    for s in stadiums:
        if sMS[ms][s].value() == 1.0:
            print(ms, s)
            
#maximized earning of MFO
print(value(mfo_lp_problem.objective))