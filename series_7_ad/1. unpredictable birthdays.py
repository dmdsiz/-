from datetime import date, timedelta


def birthday(a, b):  # every birthday should be same date
    if a.month == b.month and a.day == b.day: # every birthday should be same date
        return True
    else:
        return False


def sameweekday(a, b): # it should be at same weekday and day
    if a.weekday() == b.weekday() and a.day == b.day:
        return True
    else:
        return False


def hundredday(a, b): # days of b-a should be multiple of 100
    A = b - a
    if A.days % 100 == 0:
        return True
    else:
        return False


def unbirthday(a, b): # every date except birthday
    if a.month == b.month and a.day == b.day:
        return False
    else:
        return True


def birthdays(a, start=None, end=None, birthday=None):
    x = 0
    c = []                  # default value of end and start
    if start == None:
        start = a
    if end == None:
        end = date.today()
    if birthday != None:
        b = end - start
        for i in range(b.days + 1):
            b = start + timedelta(days=i) # adding a day to start date
            if birthday(a, b) is True:
                c.append(b)
    if birthday == None:
        if (start.month, start.day) <= (a.month, a.day):# when (month and day of start is smaller or same than date'month and day)
            while date(year=start.year + x, month=a.month, day=a.day) < end:
                b = date(year=start.year + x, month=a.month, day=a.day)
                if b >= start:
                    c.append(b)
                    x += 1
        else:
            if start.year == a.year:# when year of start and date are same
                start = date(start.year + 1, start.month, start.day)
                while date(year=start.year + x, month=a.month, day=a.day) < end:
                    b = date(year=start.year + x, month=a.month, day=a.day)
                    x += 1
                    c.append(b)
            else:
                while date(year=start.year + x, month=a.month, day=a.day) < end:
                    b = date(year=start.year + x, month=a.month, day=a.day)
                    x += 1
                    if b >= start:
                        c.append(b)

    return tuple(c)