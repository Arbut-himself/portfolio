from datetime import date

weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def get_weekday(date_string: str) -> str:
    weekday = weekdays[date.fromisoformat(date_string).isoweekday()]
    return weekday

print(get_weekday("2025-11-06"))