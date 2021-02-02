import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals: list[Interval]) -> list[Interval]:
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
    """
    intervals.sort(key=lambda x: x.start)
    merged_intervals = []

    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:  # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:  # non-overlapping interval, add the previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    merged_intervals.append(Interval(start, end))
    return merged_intervals


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Given a list of non-overlapping intervals sorted by their start time, insert a given interval at
    the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

    Example 2:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
    Output: [[1,3], [4,12]]
    Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

    Example 3:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
    """
    merged_intervals = []
    start, end = 0, 1
    inserted = False

    for interval in intervals:
        if interval[end] < new_interval[start]:
            merged_intervals.append(interval)
        elif interval[start] > new_interval[end]:
            if not inserted:
                merged_intervals.append(new_interval)
                inserted = True
            merged_intervals.append(interval)
        else:
            new_interval[end] = max(new_interval[end], interval[end])

    if not inserted:
        merged_intervals.append(new_interval)

    return merged_intervals


def merge_intervals(intervals_a: list[list[int]], intervals_b: list[list[int]]) -> list[list[int]]:
    """
    Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.

    Example 1:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.

    Example 2:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.
    """
    result = []
    start, end = 0, 1
    index_a, index_b = 0, 0

    while index_a < len(intervals_a) and index_b < len(intervals_b):
        iv_a, iv_b = intervals_a[index_a], intervals_b[index_b]
        if iv_b[start] <= iv_a[start] <= iv_b[end] or iv_a[start] <= iv_b[start] <= iv_a[end]:
            result.append([max(iv_a[start], iv_b[start]), min(iv_a[end], iv_b[end])])

        if iv_a[end] == iv_b[end]:
            index_a += 1
            index_b += 1
        elif iv_a[end] < iv_b[end]:
            index_a += 1
        else:
            index_b += 1
    return result


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings: list[Meeting]):
    if not meetings: return 0

    max_rooms = 0
    meetings.sort(key=lambda x: x.start)
    end_times = []

    for meeting in meetings:
        while end_times and end_times[0] <= meeting.start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, meeting.end)
        max_rooms = max(max_rooms, len(end_times))
    return max_rooms


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other_job):
        return self.end < other_job.end


def find_max_cpu_load(jobs: list[Job]):
    """
    We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
    Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

    Example 1:
    Jobs: [[1,4,3], [2,5,4], [7,9,6]]
    Output: 7
    Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
    jobs are running at the same time i.e., during the time interval (2,4).

    Example 2:
    Jobs: [[6,7,10], [2,4,11], [8,12,15]]
    Output: 15
    Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

    Example 3:
    Jobs: [[1,4,2], [2,4,1], [3,6,5]]
    Output: 8
    Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4]. 
    """
    curr_cpu_load, max_cpu_load, running_jobs = 0, 0, []
    jobs.sort(key=lambda x: x.start)

    for job in jobs:
        while running_jobs and running_jobs[0].end <= job.start:
            curr_cpu_load -= heapq.heappop(running_jobs).cpu_load

        curr_cpu_load += job.cpu_load
        heapq.heappush(running_jobs, job)
        max_cpu_load = max(max_cpu_load, curr_cpu_load)
    return max_cpu_load


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule: list[list[Interval]]):
    """
    Employee Free Time (hard) #
    For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
    Our goal is to find out if there is a free interval that is common to all employees.
    You can assume that each list of employee working hours is sorted on the start time.

    Example 1:
    Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
    Output: [3,5]
    Explanation: Both the employees are free between [3,5].

    Example 2:
    Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
    Output: [4,6], [8,9]
    Explanation: All employees are free between [4,6] and [8,9].

    Example 3:
    Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
    Output: [5,7]
    Explanation: All employees are free between [5,7].
    """
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heapq.heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heapq.heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heapq.heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                                     queueTop.intervalIndex + 1))

    return result


def main():
    # input = [[Interval(1, 3), Interval(5, 6)], [
    #     Interval(2, 3), Interval(6, 8)]]
    # print("Free intervals: ", end='')
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()
    #
    # input = [[Interval(1, 3), Interval(9, 12)], [
    #     Interval(2, 4)], [Interval(6, 8)]]
    # print("Free intervals: ", end='')
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)], [Interval(5, 6)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
