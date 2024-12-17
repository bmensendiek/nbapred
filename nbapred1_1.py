"""data: https://www.basketball-reference.com
   12/17/2024 3:44PM
"""

offensive_rtg = {
    "Atlanta Hawks": 116.2,
    "Boston Celtics": 119.9,
    "Brooklyn Nets": 110.4,
    "Charlotte Hornets": 106.6,
    "Chicago Bulls": 118.7,
    "Cleveland Cavaliers": 121.2,
    "Dallas Mavericks": 119.5,
    "Denver Nuggets": 118.7,
    "Detroit Pistons": 110.1,
    "Golden State Warriors": 113.9,
    "Houston Rockets": 112.1,
    "Indiana Pacers": 114.4,
    "Los Angeles Clippers": 108.3,
    "Los Angeles Lakers": 111.3,
    "Memphis Grizzlies": 122.1,
    "Miami Heat": 112.3,
    "Milwaukee Bucks": 113.3,
    "Minnesota Timberwolves": 109.8,
    "New Orleans Pelicans": 105.1,
    "New York Knicks": 116.4,
    "Oklahoma City Thunder": 115.6,
    "Orlando Magic": 107.1,
    "Philadelphia 76ers": 105.3,
    "Phoenix Suns": 114,
    "Portland Trail Blazers": 106.9,
    "Sacramento Kings": 116.2,
    "San Antonio Spurs": 110.9,
    "Toronto Raptors": 112,
    "Utah Jazz": 109.9,
    "Washington Wizards": 107.1
}

defensive_rtg = {
    "Atlanta Hawks": 118.7,
    "Boston Celtics": 109.8,
    "Brooklyn Nets": 114.7,
    "Charlotte Hornets": 112.4,
    "Chicago Bulls": 121.9,
    "Cleveland Cavaliers": 111.2,
    "Dallas Mavericks": 112.5,
    "Denver Nuggets": 116,
    "Detroit Pistons": 113.4,
    "Golden State Warriors": 109.8,
    "Houston Rockets": 106.1,
    "Indiana Pacers": 117.3,
    "Los Angeles Clippers": 107.8,
    "Los Angeles Lakers": 114.8,
    "Memphis Grizzlies": 113.7,
    "Miami Heat": 109,
    "Milwaukee Bucks": 111.9,
    "Minnesota Timberwolves": 105.6,
    "New Orleans Pelicans": 116.6,
    "New York Knicks": 110.1,
    "Oklahoma City Thunder": 103.5,
    "Orlando Magic": 103.5,
    "Philadelphia 76ers": 110.6,
    "Phoenix Suns": 114.2,
    "Portland Trail Blazers": 116.1,
    "Sacramento Kings": 113,
    "San Antonio Spurs": 112.9,
    "Toronto Raptors": 117.1,
    "Utah Jazz": 119.3,
    "Washington Wizards": 123
}

def predict_score(team1, team2):
  """Predicts the score of a game between two NBA teams.

  Args:
    team1: The name of the first team.
    team2: The name of the second team.

  Returns:
    A tuple containing the predicted scores for each team.
  """

  if team1 not in offensive_rtg or team2 not in defensive_rtg:
    return "Invalid team name"

  score1 = (offensive_rtg[team1] + defensive_rtg[team2])/2
  score2 = (offensive_rtg[team2] + defensive_rtg[team1])/2

  if round(score1) == round(score2):
    return score1, score2
  else:
    return round(score1), round(score2)