from services import googleCalendarService
from services import googleAuth

def main(): 
    credentials = googleAuth.get_credentials()
    events = googleCalendarService.get_upcoming_events(credentials)
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])
        print("Event ID:", event["id"])

if __name__ == "__main__":
    main()