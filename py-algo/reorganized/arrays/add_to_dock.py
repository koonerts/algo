"""
Add_to_dock

"""
def add_to_dock(res, time_map, time, workers, direction, action):
        if workers:
            worker_idx = 0
            for i in range(len(workers)):
                if direction[workers[i]] == action:
                    worker_idx = i
                    break
            res[workers[worker_idx]] = time
            previously_used_action = (time, direction[workers[worker_idx]])
            for i, worker in enumerate(workers):
                if i != worker_idx:
                    time_map[time+1].append(worker)
            return previously_used_action
        return None, None



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to add_to_dock
    print(add_to_dock([]))
