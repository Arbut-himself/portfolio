from datetime import datetime, timedelta

def digital_detox(logs: list) -> bool:
    """
    This function is horrible. It needs to be broken down into multiple ones.
    However, I am too lazy to do it now and will just leave refactoring for later.
    For now it works and that's the main goal of this excercise: to just commit.
    """
    logs.sort()
    for i in range(1, len(logs)):
        start_date = datetime.fromisoformat(logs[i-1])
        end_date = datetime.fromisoformat(logs[i])
        counter = end_date - start_date
        if counter < timedelta(hours=4):
            return False
        else:
            if i > 1:
                prev_date = datetime.fromisoformat(logs[i-2])
                if prev_date.date() == end_date.date() == start_date.date():
                    return False
    return True