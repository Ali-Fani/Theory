def timeConvert(rawTime):

    hour, min, sec = rawTime.split(":")
    if hour.isnumeric() and min.isnumeric() and sec.isnumeric():
        print((int(hour)*3600)+(int(min)*60)+int(sec))
    else:
        print("enter time with numeric format!")
        timeConvert(input("enter time with numeric format!"))
        sys.exit()


timeConvert(input("Enter Time: "))
