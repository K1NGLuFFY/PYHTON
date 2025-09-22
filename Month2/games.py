"""
A class to represent different types of games.
"""

class Games:
    def __init__(self, name_of_sport, no_of_teams, no_in_a_team):

        self.name_of_sport = name_of_sport
        self.no_of_teams = no_of_teams
        self.no_in_a_team = no_in_a_team

    def __str__(self):
        return (f"Sport: {self.name_of_sport}, "
                f"Number of Teams: {self.no_of_teams}, "
                f"Players per Team: {self.no_in_a_team}")


football = Games("Football", 2, 11)
basketball = Games("Basketball", 2, 5)
rugby = Games("Rugby", 2, 15)
table_tennis = Games("Table Tennis", 2, 1)

print(football)
print(basketball)
print(rugby)
print(table_tennis)

