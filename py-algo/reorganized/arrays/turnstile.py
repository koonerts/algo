"""
Turnstile

"""
def turnstile(num_worker: int, arr_time: list[int], direction: list[int]) -> list[int]:

        time_map = {i:[] for i in range(arr_time[-1]+2)}
        LOAD, UNLOAD = 0, 1
        for i, time in enumerate(arr_time):
            time_map[time].append(i)

        previously_used_action = (None, None)
        res = [-1]*num_worker
        for time, workers in time_map.items():
            if len(workers) == 1:
                res[workers[0]] = time
                previously_used_action = (time, direction[workers[0]])
            else:
                prev_time, prev_action = previously_used_action
                if prev_time is None or time-prev_time > 1:
                    previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, UNLOAD)
                elif time-prev_time == 1:
                    if prev_action == UNLOAD:
                        previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, UNLOAD)
                    else:
                        previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, LOAD)
        return res


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to turnstile
    print(turnstile([]))
