"""
Log Files

"""
def reorderLogFiles(logs: list[str]) -> list[str]:
        digit_logs = []
        letter_logs = []

        i = 0
        while i < len(logs):
            id_sep_index = str.index(logs[i], ' ')

            if logs[i][id_sep_index + 1:id_sep_index + 2].isnumeric():
                digit_logs.append(logs[i])
            else:
                if not letter_logs:
                    letter_logs.append(logs[i])
                else:
                    log_data = logs[i][id_sep_index + 1:]

                    for j in range(len(letter_logs)):
                        ll_id_sep_index = str.index(letter_logs[j], ' ')
                        ll_log_data = letter_logs[j][ll_id_sep_index + 1:]

                        if log_data < ll_log_data:
                            letter_logs.insert(j, logs[i])
                            break
                        elif log_data == ll_log_data:
                            log_id = logs[i][:id_sep_index]
                            ll_log_id = letter_logs[j][:ll_id_sep_index]

                            if log_id < ll_log_id:
                                letter_logs.insert(j, logs[i])
                                break
                        elif j == len(letter_logs) - 1:
                            letter_logs.append(logs[i])
                            break
            i += 1
        return letter_logs + digit_logs


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reorderLogFiles
    print(reorderLogFiles([]))
