"""Demonstration: Why __iter__ is needed"""

print("=" * 70)
print("EXAMPLE 1: Team WITHOUT __iter__ (fails)")
print("=" * 70)


class TeamWithoutIter:
    def __init__(self, team_name, members):
        self.team_name = team_name
        self.members = members  # Contains a list, but Team is NOT iterable


my_team = TeamWithoutIter("Developers", ["Alice", "Bob", "Charlie"])
all_teams = [my_team]

print(f"all_teams = {all_teams}")
print(f"all_teams[0] = {all_teams[0]}")
print(f"all_teams[0].members = {all_teams[0].members}")
print()

# This works (iterating over the list):
print("Iterating over all_teams (the list itself):")
for team in all_teams:
    print(f"  {team}")
print()

# Try to iterate over the Team object:
print("Trying to iterate over all_teams[0] (the Team object):")
try:
    for member in all_teams[0]:
        print(f"  {member}")
except TypeError as e:
    print(f"  ❌ TypeError: {e}")
print()

# You CAN iterate over .members directly:
print("But you CAN iterate over all_teams[0].members (the list attribute):")
for member in all_teams[0].members:
    print(f"  {member}")
print()

print("=" * 70)
print("EXAMPLE 2: Team WITH __iter__ (works)")
print("=" * 70)


class TeamWithIter:
    def __init__(self, team_name, members):
        self.team_name = team_name
        self.members = members

    def __iter__(self):
        """Makes Team iterable by delegating to self.members"""
        return iter(self.members)


my_team2 = TeamWithIter("Champions", ["Diana", "Eve", "Frank"])
all_teams2 = [my_team2]

print(f"all_teams2 = {all_teams2}")
print(f"all_teams2[0] = {all_teams2[0]}")
print()

# Now THIS works:
print("Iterating over all_teams2[0] (the Team object with __iter__):")
for member in all_teams2[0]:
    print(f"  {member}")
print()

print("=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print(
    """
- Python doesn't automatically know how to iterate over custom objects
- Just because Team CONTAINS a list doesn't make Team iterable
- __iter__ explicitly tells Python: "iterate over self.members when 
  someone tries to iterate over me"
- Without __iter__, you'd have to always use .members:
  
  ❌ for member in all_teams[0]:          # Fails without __iter__
  ✓  for member in all_teams[0].members:  # Always works
  ✓  for member in all_teams[0]:          # Works WITH __iter__
"""
)
