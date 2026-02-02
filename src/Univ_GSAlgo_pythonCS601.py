def hospital_resident_matching(hosp_prefs, stud_prefs, capacities):
    # stud_rank[s][h] = position (rank) of hospital h in student s's preference list
    # Smaller index = more preferred.
    stud_rank = {}
    for s, pref_list in stud_prefs.items():
        # For each student, build a dict: hospital -> rank index
        stud_rank[s] = {h: i for i, h in enumerate(pref_list)}

    # assigned[h] = list of students currently assigned to hospital h
    assigned = {h: [] for h in hosp_prefs}

    # assigned_hospital[s] = hospital currently assigned to student s (or None if unmatched)
    assigned_hospital = {s: None for s in stud_prefs}

    # next_index[h] = index of the next student in hosp_prefs[h] that hospital h will propose to
    next_index = {h: 0 for h in hosp_prefs}

    # Start with all hospitals as "free": they all need to fill their slots
    free_hospitals = [h for h in hosp_prefs]

    # Main loop: keep going while there is at least one hospital that still needs to propose
    while free_hospitals:
        # Take one hospital from the front of the queue
        h = free_hospitals.pop(0)
        print("hospital being checked :", h , free_hospitals)

        # If h is already full OR has no one left to propose to, skip it this round
        if len(assigned[h]) >= capacities[h] or next_index[h] >= len(hosp_prefs[h]):
            continue

        # Pick the next student on h's preference list to propose to
        s = hosp_prefs[h][next_index[h]]

        # Move h's pointer forward so it won't propose to s again in the future
        next_index[h] += 1

        # current = the hospital that s is currently matched to (if any)
        current = assigned_hospital[s]

        if current is None:
            # Case 1: s is free, so they just accept h's proposal
            assigned[h].append(s)          # add s to h's assigned list
            assigned_hospital[s] = h       # record that s is now matched to h

        else:
            # Case 2: s is already matched; decide whether to keep current or switch to h

            # If s prefers h over their current hospital (lower rank index means better)
            if stud_rank[s][h] < stud_rank[s][current]:
                # s likes h more than current -> s "trades up" to h

                # Remove s from the old hospital's assigned list
                assigned[current].remove(s)

                # Add s to h's assigned list
                assigned[h].append(s)

                # Update s's assigned hospital
                assigned_hospital[s] = h

                # The old hospital 'current' now has a free slot,
                # so put it back into the queue if it still has people to propose to
                if len(assigned[current]) < capacities[current]:

                    free_hospitals.insert(0, current) #adding the free H to start of list
                    # free_hospitals.append(current)
                    print("hospital who got free and added to free list: ", current)
            # else:
            #   s prefers their current hospital over h, so they reject h.
            #   In that case we do nothing: s stays with 'current' and h remains unmatched (for this slot).

        # After this proposal, if h still has free capacity AND still has students left to propose to,
        # then h should continue proposing later, so we put it back in the queue.
        if len(assigned[h]) < capacities[h] and next_index[h] < len(hosp_prefs[h]):

            free_hospitals.append(h)

    # When the loop finishes, 'assigned' contains each hospital's final list of students.
    return assigned


def main():
    # --- TEST CASE 1: Hospitals A–E, Students T,U,V,X,Y,Z ---

    # Each hospital has capacity 1
    capacities = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1,
        'E': 1,
    }

    # Hospital preferences
    hosp_prefs = {
        'A': ['T', 'U', 'V', 'X', 'Y', 'Z'],
        'B': ['T', 'U', 'X', 'V', 'Y', 'Z'],
        'C': ['U', 'T', 'X', 'V', 'Y', 'Z'],
        'D': ['V', 'X', 'T', 'U', 'Y', 'Z'],
        'E': ['X', 'V', 'U', 'T', 'Y', 'Z'],
    }

    # Student preferences
    stud_prefs = {
                    'T': ['B', 'A', 'C', 'D', 'E'],
                    'U': ['A', 'C', 'B', 'D', 'E'],
                    'V': ['D', 'E', 'A', 'B', 'C'],
                    'X': ['E', 'D', 'B', 'C', 'A'],
                    'Y': ['A', 'B', 'C', 'D', 'E'],
                    'Z': ['A', 'B', 'C', 'D', 'E'],
                }

    result = hospital_resident_matching(hosp_prefs, stud_prefs, capacities)

    print("Final assignment for hospitals:")

    print(result)  # ~ printing final assigned hospital results

    for h in sorted(result.keys()):
        print(f"{h} -> {result[h]}")

if __name__ == "__main__":
    main()