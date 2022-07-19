def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Rassokha"))
print(are_you_playing_banjo("rassokha"))
print(are_you_playing_banjo("Zassokha"))