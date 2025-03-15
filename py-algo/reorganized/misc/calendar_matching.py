"""
Matching

"""
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
def convert_to_minutes(lst_intervals):
        for intervals in lst_intervals:
            for i in range(len(intervals)):
                start, end = intervals[i]
                start_hrs, start_mins = start.split(':')
                end_hrs, end_mins = end.split(':')

                intervals[i][0] = 60*int(start_hrs) + int(start_mins)
                intervals[i][1] = 60*int(end_hrs) + int(end_mins)
def convert_to_military(lst_intervals):
        for intervals in lst_intervals:
            for i in range(len(intervals)):
                start_hrs, start_mins = intervals[i][0]//60, "00" if intervals[i][0] % 60 == 0 else intervals[i][0] % 60
                end_hrs, end_mins = intervals[i][1]//60, "00" if intervals[i][1] % 60 == 0 else intervals[i][1] % 60

                intervals[i][0] = f'{start_hrs}:{start_mins}'
                intervals[i][1] = f'{end_hrs}:{end_mins}'
def merge_overlaps(intervals):
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                result.append(intervals[i])
            else:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
        return result
def get_free_openings(booked_times):
        bounds = [max(dailyBounds1[0], dailyBounds2[0]), min(dailyBounds1[1], dailyBounds2[1])]
        if not booked_times:
            return [bounds]

        openings = []
        if bounds[0] < booked_times[0][0] and booked_times[0][0] - bounds[0] >= meetingDuration:
            openings.append([bounds[0], booked_times[0]])

        prev = booked_times[0]
        for i in range(1, len(booked_times)):
            open_slot = [prev[1], booked_times[i][0]]
            if open_slot[0] >= bounds[0] and open_slot[1] <= bounds[1] and \
                    open_slot[1]-open_slot[0] >= meetingDuration:
                openings.append(open_slot)
            prev = booked_times[i]

        if bounds[1] > booked_times[-1][1] and bounds[1] - booked_times[-1][1] >= meetingDuration:
            openings.append([booked_times[-1][1], bounds[1]])
        return openings

    convert_to_minutes([calendar1, [dailyBounds1], calendar2, [dailyBounds2]])
    booked_times = sorted(calendar1 + calendar2, key=lambda x:x[0])
    booked_times = merge_overlaps(booked_times)
    openings = get_free_openings(booked_times)
    convert_to_military([openings])
    return openings


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to calendarMatching
    print(calendarMatching([]))
