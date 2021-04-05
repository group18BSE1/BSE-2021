# input section for hours and rates
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    extra_hours = (hours - 40) * rate * 1.5
    if hours > 40:
        pay = extra_hours + (40 * rate)
    else:
        pay = hours * rate
    print(f"Pay: {pay}")


except ValueError:
    print("Error please enter numerical input")
