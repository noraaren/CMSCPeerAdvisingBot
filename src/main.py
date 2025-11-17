from services import googleCalendarService
from services import googleAuth
from datetime import datetime, timezone

def main(): 
    credentials = googleAuth.get_credentials()
    events = googleCalendarService.get_lastTwoWeeksEvents(credentials)
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        print(f"{start} -> {end} {event.get('summary', '(no title)')}")

if __name__ == "__main__":
    main()