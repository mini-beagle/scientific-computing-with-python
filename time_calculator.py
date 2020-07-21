def add_time(start, duration, day=None):
    
    start = start.split()
    start_time = start[0].split(':')
    if start[1] == 'PM':
        start_hrs = int(start_time[0]) + 12
    else:
        start_hrs = int(start_time[0])
    start_mins = int(start_time[1])
    
    duration = duration.split(':')
    duration_hrs = int(duration[0])
    duration_mins = int(duration[1])

    result_hrs = start_hrs + duration_hrs
    result_mins = start_mins + duration_mins
    if result_mins >= 60:
        result_hrs += 1
        result_mins -= 60
    if result_mins < 10:
        result_mins = '0' + str(result_mins)
    else:
        result_mins = str(result_mins)

    days_later = 0
    if result_hrs >= 24:
        days_later = int(result_hrs / 24)

    result_hrs %= 24
    if result_hrs >= 12:
        result_period = 'PM'
    else:
        result_period = 'AM'

    if result_hrs % 12 != 0:         # not noon
        result_hrs %= 12
    else:
        if result_period == 'AM':    # adjust for midnight
            result_hrs = 12
        
    result = str(result_hrs) + ':' + result_mins + ' ' + result_period

    if day is not None:
        day = day.lower()
        if days_later > 0:
            if day == 'sunday':
                day = 1
            elif day == 'monday':
                day = 2
            elif day == 'tuesday':
                day = 3
            elif day == 'wednesday':
                day = 4
            elif day == 'thursday':
                day = 5
            elif day == 'friday':
                day = 6
            else:
                day = 7
            day += days_later
            day %= 7
            if day == 0:
                day = ', Saturday'
            elif day == 1:
                day = ', Sunday'
            elif day == 2:
                day = ', Monday'
            elif day == 3:
                day = ', Tuesday'
            elif day == 4:
                day = ', Wednesday'
            elif day == 5:
                day = ', Thursday'
            else:
                day = ', Friday'
        else:
            day = ', ' + day.capitalize()
    else:
        day = ''
    
    if days_later >= 1:
        if days_later >= 2:
            result += day + ' (' + str(days_later) + ' days later)'
        else:
            result += day + ' (next day)'
    else:
        result += day

    return result