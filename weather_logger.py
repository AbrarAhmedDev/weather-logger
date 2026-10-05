# weather_logger.py

temps = []

while True:
    value = input("Enter daily temperature (or 'done' to stop): ")

    if value.lower() == "done":
        break

    temps.append(float(value))


def summarize(temps):
    result = {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }

    return result


summary = summarize(temps)

print(summary)