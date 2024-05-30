# Tournament Winner

There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named `competitions` and `results`, respectively. The `competitions` array has elements in the form of `[homeTeam, awayTeam]`, where each team is a string of at most 30 characters representing the name of the team. The `results` array contains information about the winner of each corresponding competition in the `competitions` array. Specifically, `results[i]` denotes the winner of `competitions[i]`, where a `1` in the `results` array means that the home team in the corresponding competition won and a `0` means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.

#### Sample Input

```
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]
```

#### Sample Output

```
"Python"
// C# beats HTML, Python beats C#, and Python beats HTML
// HTML - 0 points
// C# - 3 points
// Python - 6 points
```

## Hints

#### Click the arrows to see the hints

<details>
  <summary><b>Hint 1</b></summary>
Don't overcomplicate this problem. How would you solve it by hand? Consider that approach, and try to translate it into code.
</details>

<details>
  <summary><b>Hint 2</b></summary>
Use a hash table to store the total points collected by each team, with the team names as keys in the hash table. Once you know how many points each team has, how can you determine which one is the winner?
</details>

<details>
  <summary><b>Hint 3</b></summary>
Loop through all of the competitions, and update the hash table at every iteration. For each competition, consider the name of the winning team; if the name already exists in the hash table, update that entry by adding 3 points to it. If the team name doesn't exist in the hash table, add a new entry in the hash table with the key as the team name and the value as 3 (since the team won its first competition). While looping through all of the competitions, keep track of the team with the highest score, and at the end of the algorithm, return the team with the highest score.
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(n) time | O(k) space - where n is the number of competitions and k is the number of teams
</details>

## Concept Walkthrough

Let's look at an example input

![image](https://github.com/KellzCodes/python_interview/assets/19383145/e1bf1cd3-127d-4bfa-bf7a-5d93d2c6bf75)

The `competitions` array represents all of the competitions in the tournament. It simply contains pairs that contains two strings. The first string is the name of the home team and the second string is the name of the away team. It's not relevant to call this the home team or the away team. This is how we are going to differentiate which team actually won these competitions. 

The `results` array is going to be the same length as the competitions array. It's going to represent the winner of each of these competitions. 

The indices in the `results` array are going to correspond with the indices in the `competitions` array. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/ab8e39c8-6daa-4ec0-bca6-0765ad48e01f)

When you see a zero in side of the `results` array, this means the away team won the competition. So in the first case, C# is the winner of the competition. The second case, Python is the winner of the competition.

If you see a 1, this means that in the corresponding game, the home team won. So in the 3rd case, Python is the winner. 

We can see that Python won a total of 2 competitions which is the most wins. This means they won the tournament.

You are always going to be given at least two teams. That means you will always have at least one competition. 

The `competitions` array is always going to be the same length of the `results` array. This is because you need a result for every one of the competitions. You can assume you will be given valid input

## Solution Walkthrough

The solution code can be found in [tournament_winner.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Tournament-Winner/tournament_winner.py).

This solution will run in `O(n)` time | `O(k)` space - where n is the number of competitions and k is the number of teams. 

Let's look at how many points each team got in our example

![image](https://github.com/KellzCodes/python_interview/assets/19383145/92d9f28c-c6f5-4644-ad07-94430b3466c3)

All we really want to do is look through all the competitions and just keep track of how many points every single team has. 

Once we know all of the points for all of the teams then we can simply go through and figure out which team has the most amount of points then return the name of the team.

To do this, we need to create some kind of data structure that can tell us which team has what number of points. We can either initialize this data structure when we start our algorithm or we can create it as we go through.

We are going to create a data structure called `scores` that is going to be a hash table. The name of the team will be the key and the value will be the team's score. We will initialize it as an empty data structure.

Then we will loop through each of the competitions and figure out what team actually won.

To simulate us looping through the `competitions` list, we can put a green pointer that just tells us which competition we are currently on.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/e4f4a8ca-24a0-4266-a6da-6ec89e1ddc26)

We want to keep track of the actual competition itself and we want to know the index this competition is at. The reason is we need to access this index in the `results` array so we can figure out what team won. 

We are really going to loop through both the `results` and `competitions` arrays at the exact same time. Then using the value from the results array to figure out which team was the winner. 

Once we figure the winning team, we need to change their score or update their score in our scores data structure. First, we'll check to see if the winning team is already in the scores table. If they are in the scores table, all we need to do is add 3 to their score and update their score to say they won a game. If they are not in the scores table, they have not won a game yet and we need to add them into the table. We can assume that if the team is not in the scores table then their current score is zero. 

So for the first competition in our example, C# is the winner. So we can add the key "C#" and update its value to 3.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/07e1bee2-5812-46e3-9f2e-3c9f8999cf71)

Then we do the same for the next competition. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/c0924267-17a4-486e-af16-61ea9a120b55)

For the third competition, Python is the winner again. So now we check to see if Python is in the scores table. It is, so all we do is add 3 to the value beside the Python key. Now the value beside the Python key is 6. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/7d14f186-0285-4928-b8d8-3aa4e806221c)

Now that we've gone through all of our competitions and looked at all of our results, we need to figure out which team had the most number of points. So we loop through the scores table to figure out which team had the best score. 

Let's go over a quick optimization so we do not have to use two for loops. 

We can introduce a new variable that's going to keep track of the highest score that we've currently seen. It will actually keep track of the team that has the highest score. 

We can say `bestTeam = ""`. Whenever a team wins, we will compare the score of the team who just won with the current `bestTeam`. 

At first, our best team is an empty string. So what we should do when we initialize the scores table is add an empty string and say its score is zero. Just so that when we look up this `bestTeam` in our scores table we don't get an index error or something. We will actually have a score returned to us which is really going to be zero.

We have the empty string in our data structure which will give us zero at our first iteration. We can compare it to the score of the team that just won. We will see that the winning team will have the greater score than the empty string which is the current best team. So we update the best team to be the new winning team.  

So let's see what the algorithm will look like when we go through the steps again. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/13fae18f-3b9b-4e3e-ab61-c8c0a01698d3)

On the second competition, Python is the winner and its score is 3. So we compare Python's score to the winning team score. The scores are the same so we wont bother updating the `bestTeam` variable. We'll just assume that if Python is the best team, it will get updated later on because there's only ever going to be one winner. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/c87d5033-6522-474e-b21e-6811eb9fd0c5)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/be45a462-4765-4306-ac5f-bc15c53941c7)
