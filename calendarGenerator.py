from icalendar import Calendar, Event
import os
from datetime import datetime, timedelta
from typing import Tuple
import json
import os


def build_event_duration(
    summary, description, start, duration, location, freq_of_recurrence, until
) -> Event:
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

def generate_calendar(request:dict) -> dict:
    cal = Calendar()
    cal.add("version", "4.0.7")
    cal.add("x-wr-timezone", "Asia/Kolkata")
    cal.add("x-wr-calname", request["regno"])
    slotfile = open("./slotinfofile.json", "r")
    slotinfo = json.load(slotfile)
    for course in request["courses"]:
        summary = f'{course["course_code"]}({course["course_type"]})'
        description = course["course_name"]
        slots = course["slots"].split('+')
        year = 2021
        month = 8
        duration = timedelta(minutes=45)
        until = datetime(2021, 12, 13)
        location = f'{course["location"]}({course["teacher_name"]})'
        for slot in slots:
            for clas in slotinfo[slot]:
                clas[1]-=20
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
    # output = {"calendar": cal.to_ical().decode("UTF-8"), "reg_no": reg_no}
    filename = './icsfiles/'+request["regno"]+'_'+request["semnumber"]+'.ics'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename,'wb') as ics:
        ics.write(cal.to_ical())
    print(f'{filename} succesfully generated')
    output = {
        "filename":filename,
        "link":("vitcalapi.tech"+filename[1:-4]).replace('icsfiles','download')
    }
    return output
