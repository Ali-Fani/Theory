time = int(input("Enter Time"))


def convert(seconds):
    hour = seconds // 3600
    print(hour)
    seconds %= 3600
    print(seconds)
    minutes = seconds // 60
    print(minutes)
    seconds %= 60
    print(seconds)

    return "%d:%02d:%02d" % (hour, minutes, seconds)


print(convert(time))
