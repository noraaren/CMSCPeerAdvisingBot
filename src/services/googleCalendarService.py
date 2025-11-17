from datetime import datetime, timedelta, timezone

from googleapiclient.discovery import build

def get_upcoming_events(credentials): 
    service = build("calendar", "v3", credentials=credentials)

    # Call the Calendar API
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    events_result = (
        service.events()
        .list(
            calendarId="aren1@terpmail.umd.edu",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    return events

def get_listrange_events(credentials, start_date, end_date):
    service = build("calendar", "v3", credentials=credentials)

    # If start_date / end_date are timezone-aware:
    time_min = start_date.isoformat()
    time_max = end_date.isoformat()

    events_result = (
        service.events()
        .list(
            calendarId="aren1@terpmail.umd.edu",
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    return events_result.get("items", [])



def get_lastTwoWeeksEvents(credentials):
    service = build("calendar", "v3", credentials=credentials)

    now = datetime.now(timezone.utc)   # or use local timezone if preferred
    two_weeks_ago = now - timedelta(weeks=2)

    events_result = (
        service.events()
        .list(
            calendarId="aren1@terpmail.umd.edu",
            timeMin=two_weeks_ago.isoformat(),
            timeMax=now.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    return events_result.get("items", [])
