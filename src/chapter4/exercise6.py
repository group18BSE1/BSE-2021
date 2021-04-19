# input section for hours and rates
def computepay(hours, rate):
    extra_hours = (hours - 40)*rate*1.5
    if hours > 40:
        pay = extra_hours + (40 * rate)
    else:
        pay = hours * rate
    return pay


pay=computepay(45, 10)
print(pay)




