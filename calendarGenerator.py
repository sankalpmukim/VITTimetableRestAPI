from icalendar import Calendar, Event
from datetime import datetime, timedelta
import json
import os


def get_relevant_data(strng: str):
    def connect_these(lst):
        strnges = []
        for i in lst:
            strnges.append(i)
        return strnges

    allTheFriggingLines = strng.split("\r\n")
    startIndex = allTheFriggingLines.index("1")
    endIndex = -19
    length = len(allTheFriggingLines)
    relevantData = [
        connect_these(allTheFriggingLines[i : i + 39])
        for i in range(startIndex, length - endIndex, 39)
    ][:-2]
    # for i in relevantData:
    #     print(i)
    return relevantData[:], allTheFriggingLines[3][15:24]


def build_event_duration(
    summary, description, start, duration, location, freq_of_recurrence, until
):
    """
    Return an event that can be added to a calendar

    summary: summary of the event
    description: description of the event
    location: self explanatory
    start, end, stamp: These are datetime.datetime objects
    freq_of_recurrence: frequency of recurrence, string which can take the
    values daily, weekly, monthly, etc.
    until: A datetime.datetime object which signifies when the recurrence will
    end
    """

    event = Event()
    event.add("summary", summary)
    event.add("description", description)
    event.add("dtstart", start)
    event.add("duration", duration)
    event.add("dtstamp", datetime.now())
    event.add("location", location)
    event.add("rrule", {"FREQ": freq_of_recurrence, "UNTIL": until})

    return event


def generate_calendar(whole_site_data: str):
    relevantData, reg_no = get_relevant_data(whole_site_data)
    cal = Calendar()
    cal.add("version", "4.0.7")
    cal.add("x-wr-timezone", "Asia/Kolkata")
    cal.add("x-wr-calname", reg_no)
    slotfile = open("./slotinfofile.json", "r")
    slotinfo = json.load(slotfile)
    print(reg_no)
    for course in relevantData:
        summary = course[6].split("-")[0][:-1] + course[6]
        description = course[6].split("-")[1][1:]
        slots = course[20][:-2].split("+")
        year = 2021
        month = 2
        duration = timedelta(minutes=45)
        until = datetime(2021, 6, 19)
        location = course[-17] + " (" + course[-14][:-2] + ")"
        for slot in slots:
            for clas in slotinfo[slot]:
                event = build_event_duration(
                    summary,
                    description,
                    datetime(year, month, clas[1], clas[0][0], clas[0][1]),
                    duration,
                    location,
                    freq_of_recurrence="weekly",
                    until=until,
                )
                if not ("roject" in summary):
                    cal.add_component(event)
    print("calendar generation complete")
    output = {"calendar": cal.to_ical().decode("UTF-8"), "reg_no": reg_no}
    return output
