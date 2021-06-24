class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
while not line == "End":
    party.people.append(line)
    line = input()

people = ", ".join(party.people)
print(f"Going: {people}")
print(f"Total: {len(party.people)}")