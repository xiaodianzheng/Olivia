import itertools
import q4a


def get_seating_arrangement(female_list, male_list, must_list, cannot_list):
    female_permutations = list(itertools.permutations(female_list))
    male_permutations = list(itertools.permutations(male_list))
    arrangements_list = []
    for f_perm in female_permutations:
        for m_perm in male_permutations:
            cur_arrangement1 = []
            cur_arrangement2 = []
            for i in range(3):
                cur_arrangement1.extend([f_perm[i], m_perm[i]])
                cur_arrangement2.extend([m_perm[i], f_perm[i]])
            arrangements_list.extend([cur_arrangement1, cur_arrangement2])
    for arrangement in arrangements_list:
        if q4a.check_seating_arrangement(arrangement, must_list, cannot_list):
            return arrangement
