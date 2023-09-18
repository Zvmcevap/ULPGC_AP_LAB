def order_crossover(parent1: list, parent2: list, lower_bound: int, upper_bound: int):
    child1 = []

    # Copy the crossover from padre but keep it static for checking, as the elements in madre are all unique, but I am
    # unsure that will always be the case.
    p_child = parent1[lower_bound:upper_bound]
    child1 = p_child.copy()

    position = upper_bound

    for i in range(len(parent2)):
        element = parent2[(upper_bound + i) % len(parent2)]
        if element in p_child:
            # If the selected element is inside the crossover from padre continue
            continue

        if position >= upper_bound:
            child1.append(element)
        else:
            child1.insert(position, element)
        position = (position + 1) % len(parent2)

    return child1
