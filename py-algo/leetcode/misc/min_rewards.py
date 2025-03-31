"""
Rewards

"""


def minRewards(scores):
    rewards = [0] * len(scores)
    rewards[0] = 1
    min_reward = 1

    for i, val in enumerate(scores):
        if val < scores[i - 1]:
            rewards[i] = rewards[i - 1] - 1
            min_reward = min(min_reward, rewards[i])
        else:
            rewards[i] = rewards[i - 1] + 1
    print(rewards)
    print([r + abs(min_reward) + 1 for r in rewards])


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minRewards
    print(minRewards([]))
