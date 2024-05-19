def tournamentWinner(competitions, results):
    # declare a constant for the value that is used if home team wins tournament
    HOME_TEAM_WON = 1
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        # there are only two values in each competition
        # home team is the first element and away team is second element
        homeTeam, awayTeam = competition
        # the winning team is home team only if result is 1
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # update the scores data structure
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points