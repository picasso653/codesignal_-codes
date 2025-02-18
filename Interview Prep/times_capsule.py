def add_seconds_to_times(timePoints, seconds):
    new_times = []
    for timePoint in timePoints:
        timeParts = [int(part) for part in timePoint.split(":")]
        total_secods_prev = timeParts[0] * 3600 + timeParts[1] * 60 + timeParts[2]
        total_secods_curr = (total_secods_prev + seconds) % (24 * 3600)
        hours, remainder = divmod(total_secods_curr, 3600)
        minutes, tseconds = divmod(remainder, 60)
        new_times.append(f"{hours:02d}:{minutes:02d}:{tseconds:02d}")
    return new_times
    pass