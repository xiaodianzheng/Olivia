def check_seating_arrangement(arrangement, must_list, cannot_list):
    arrangement_set = set()
    for i in range(len(arrangement)):
        if i == len(arrangement) - 1:
            arrangement_set.add((arrangement[i], arrangement[i - 1]))
            arrangement_set.add((arrangement[i], arrangement[0]))
        else:
            arrangement_set.add((arrangement[i], arrangement[i - 1]))
            arrangement_set.add((arrangement[i], arrangement[i + 1]))
    must_set = set(must_list)
    cannot_set = set(cannot_list)
    if must_set.issubset(arrangement_set) and cannot_set.isdisjoint(arrangement_set):
        return True
    else:
        return False
