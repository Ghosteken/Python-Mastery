def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities based on their finish times
    selected_activities = []
    prev_finish_time = -1

    for activity in activities:
        start_time, finish_time = activity
        if start_time >= prev_finish_time:
            selected_activities.append(activity)
            prev_finish_time = finish_time

    return selected_activities

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(activity_selection(activities))
# Output: [(1, 4), (5, 7), (8, 11), (12, 16)]
