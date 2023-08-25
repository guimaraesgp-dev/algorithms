def study_schedule(permanence_period, target_time):
    time_valid = 0
    if not target_time:
        return None
    for start, out in permanence_period:
        if not isinstance(start, int) or not isinstance(out, int):
            return None
        if start <= target_time <= out:
            time_valid += 1
    return time_valid
