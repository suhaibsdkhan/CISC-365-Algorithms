def activity_selection(activities):
    """
    Given a list of activities, each represented as (start_time, finish_time),
    select the maximum number of activities that do not overlap.

    The algorithm:
      1. Sort activities by their finish time (ascending).
      2. Pick the first activity (earliest finish).
      3. For each subsequent activity in sorted order, if it starts on or after
         the finish time of the last selected activity, select it.

    :param activities: List of (start, finish) pairs
    :return: A list of selected (start, finish) pairs
    """

    # Step 1: Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # Keep track of the selected activities
    selected = []

    # The finish time of the last selected activity
    current_finish = None

    for (start, finish) in sorted_activities:
        # If this is the first activity or it doesn't overlap the last selected one
        if current_finish is None or start >= current_finish:
            selected.append((start, finish))
            current_finish = finish  # Update the finish time

    return selected


# Example usage:
if __name__ == "__main__":
    # Suppose we have these activities, each with a start_time and finish_time
    activities = [
        (1, 3),
        (2, 5),
        (0, 6),
        (5, 7),
        (8, 9),
        (5, 9)
    ]
    
    chosen = activity_selection(activities)
    print("Selected activities:", chosen)
