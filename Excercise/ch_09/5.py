class Team:
    def __init__(self, name: str, wins: int, loss: int, draws: int, scored: int, conceded: int):
        self.name: str = name
        self.wins: int = int(wins)
        self.loss: int = int(loss)
        self.draws: int = int(draws)
        self.scored: int = int(scored)
        self.conceded: int = int(conceded)

    def __str__(self):
        return str([self.name, {'points': self.score}, {'gd': self.gd}])

    @property
    def score(self):
        return 3*self.wins + self.draws
    
    @property
    def gd(self):
        return self.scored - self.conceded

teams = []
teams_input = input("Enter Input : ").split('/')

for team in teams_input:
    name, wins, loss, draws, scored, conceded = team.split(',')
    # print(f'{name} {wins} {loss} {draws} {scored} {conceded}')
    new_team = Team(
        name,
        wins,
        loss,
        draws,
        scored,
        conceded
    )
    teams.append(new_team)

def sort_teams(teams):
    n = len(teams)
    for i in range(n):
        for j in range(0, n-i-1):
            if (teams[j].score < teams[j+1].score) or (teams[j].score == teams[j+1].score and teams[j].gd < teams[j+1].gd):
                teams[j], teams[j+1] = teams[j+1], teams[j]
    return teams

print("== results ==")
[print(team) for team in sort_teams(teams)]
