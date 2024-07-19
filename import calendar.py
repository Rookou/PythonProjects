import calendar
import time
import datetime
class Event:
    def __init__(self, date, name, description):
        self.date = date
        self.name = name
        self.description = description
events = []
def choose_calendar():
    global yy, mm
    while True:
        yy = input("Enter a year: ")
        if len(yy) != 4:
            print("Invalid Year, Please try again")
        else:
            break

    while True:
        month_input = input("Enter a month: ").strip().lower()
        if month_input.isdigit() and 1 <= int(month_input) <= 12:
            mm = month_input.zfill(2)
            break
        elif month_input.title() in calendar.month_name:
            mm = str(list(calendar.month_name).index(month_input.title())).zfill(2)
            break
        else:
            print("Invalid Month, Please try again")

    print(calendar.month(int(yy), int(mm)))
    time.sleep(1.5)
    print("----------------------")
    main()
def get_day():
    while True:
        date_input = input("Enter the date (e.g. 1st March 2023 or in dd/mm/yyyy format): ").strip().lower()
        if "of" in date_input:
            date_input = date_input.rstrip("of", "")
        if '/' in date_input:
            parts = date_input.split('/')
            if len(parts) == 3:
                dd, mm, yy = parts
                if dd.isdigit() and mm.isdigit() and yy.isdigit():
                    if 1 <= int(mm) <= 12 and 1 <= int(dd) <= calendar.monthrange(int(yy), int(mm))[1]:
                        day_of_week = calendar.weekday(int(yy), int(mm), int(dd))
                        print(f"The day of the week for {dd}/{mm}/{yy} is {calendar.day_name[day_of_week]}")
                        break
                    else:
                        print("Invalid date, Please try again")
                else:
                    print("Invalid date, Please try again")
            else:
                print("Invalid date, Please try again")
        else:
            day_parts = date_input.split()
            day = day_parts[0]
            month = day_parts[1]
            year = day_parts[2]
            if month.isdigit() and 1 <= int(month) <= 12:
                mm = month.zfill(2)
            elif len(month) == 3 and month.capitalize() in calendar.month_abbr:
                mm = str(list(calendar.month_abbr).index(month.capitalize())).zfill(2)
            elif month.capitalize() in calendar.month_name:
                mm = str(list(calendar.month_name).index(month.capitalize())).zfill(2)
            else:
                print("Invalid month, Please try again")
                continue

            day = day.rstrip("st").rstrip("nd").rstrip("rd").rstrip("th")
            if day.isdigit():
                day = int(day)
                if 1 <= day <= 31 and year.isdigit():
                    yy = year
                    day_of_week = calendar.weekday(int(yy), int(mm), day)
                    print(f"The day of the week for {day} {calendar.month_name[int(mm)]}, {yy} is {calendar.day_name[day_of_week]}")
                    break
                else:
                    print("Invalid Day or Year, Please try again")
            else:
                print("Invalid input, Please try again")
    time.sleep(1.5)
    print("----------------------")
    main()

def create_event():
    while True:
        date_input = input("Enter the date of the event (e.g. 1st March 2023 or in dd/mm/yyyy format): ").strip().lower()
        if "of" in date_input:
            date_input = date_input.replace("of", "")
        if '/' in date_input:
            parts = date_input.split('/')
            if len(parts) == 3:
                dd, mm, yy = parts
                if dd.isdigit() and mm.isdigit() and yy.isdigit():
                    if 1 <= int(mm) <= 12 and 1 <= int(dd) <= calendar.monthrange(int(yy), int(mm))[1]:
                        event_name = input("Enter the name of the event: ")
                        event_description = input("Enter the description of the event: ")
                        # Converting to dd/mm/yyyy format because I enjoy suffering
                        event_date = f"{dd.zfill(2)}/{mm.zfill(2)}/{yy}"
                        event = Event(event_date, event_name, event_description)
                        Event.events.append(event)  # Append to the class attribute
                        print("Event created successfully.")
                        main()
                        break
                    else:
                        print("Invalid date, Please try again")
                else:
                    print("Invalid date, Please try again")
            else:
                print("Invalid date, Please try again")
        else:
            day_parts = date_input.split()
            day = day_parts[0]
            day = day.rstrip("st").rstrip("nd").rstrip("rd").rstrip("th")
            month = day_parts[1]
            year = day_parts[2]
            if month.isdigit() and 1 <= int(month) <= 12:
                mm = month.zfill(2)
            elif len(month) == 3 and month.capitalize() in calendar.month_abbr:
                mm = str(list(calendar.month_abbr).index(month.capitalize())).zfill(2)
            elif month.capitalize() in calendar.month_name:
                mm = str(list(calendar.month_name).index(month.capitalize())).zfill(2)
            else:
                print("Invalid month, Please try again")
                continue

            if day.isdigit():
                day = str(day).zfill(2)
                if 1 <= int(mm) <= 12 and 1 <= int(day) <= calendar.monthrange(int(year), int(mm))[1]:
                    event_name = input("Enter the name of the event: ")
                    event_description = input("Enter the description of the event: ")
                    event_date = f"{day}/{mm}/{year}"
                    event = Event(event_date, event_name, event_description)
                    Event.events.append(event)  # Append to the class attribute
                    print("Event created successfully.")
                    time.sleep(1.5)
                    print("----------------------")
                    main()
                    break
                else:
                    print("Invalid date, Please try again")

def get_days_until_events(events):
    # today's date
    today = datetime.date.today()

    # Array
    event_details_with_days = []

    # Loop through events
    for event in events:
        event_date = datetime.datetime.strptime(event.date, "%d/%m/%Y").date()
        # Calculate days until the event
        days_until_event = (event_date - today).days
        # Append event details along with days until the event to the list
        event_details_with_days.append([event.name, event.date, days_until_event])

    # Sort events
    event_details_with_days.sort(key=lambda x: x[2])

    # Display the sorted events along with days until the event
    print("Events and Days Until the Event:")
    for event in event_details_with_days:
        print(f"{event[0]}, {event[1]}: {event[2]} days until the event")
    time.sleep(1.5)
    print("----------------------")
    main()

class Event:
    events = []

    def __init__(self, date, name, description):
        self.date = date
        self.name = name
        self.description = description

    @classmethod
    def create_preset_events(cls):
        preset_events = [
            {"date": "25/12/2024", "name": "Christmas🎄", "description": "Celebration of Christmas Day"},
            {"date": "01/01/2025", "name": "New Year's Day", "description": "Celebration of New Year's Day"},
            {"date": "04/07/2025", "name": "Independence Day", "description": "Celebration of Independence Day"},
            # Add more preset events as needed
        ]

        for preset_event in preset_events:
            event = cls(preset_event["date"], preset_event["name"], preset_event["description"])
            cls.events.append(event)

        print("Preset events created successfully.")
        time.sleep(1.5)
        print("----------------------")
        main()

def view_events():
    if Event.events:
        print("Events:")
        # Convert date strings to datetime objects for proper sorting
        sorted_events = sorted(Event.events, key=lambda event: datetime.datetime.strptime(event.date, '%d/%m/%Y').date())
        for event in sorted_events:
            print(f"Date: {event.date} Name: {event.name} Description: {event.description}")
            time.sleep(0.5)  # Consider if this delay is necessary
    else:
        print("No events found.")
    
    time.sleep(1.5)  # Consider if this delay is necessary
    print("----------------------")
    main()

def main():
    print("")
    print("Main Menu:")
    print("1. Choose Calendar")
    print("2. Get Day of the Week")
    print("3. Create Event")
    print("4. View Events")
    print("5. Get Days Until Events")
    print("6. Automatically Create Preset Events")
    print("7. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        choose_calendar()
    elif option == "2":
        get_day()
    elif option == "3":
        create_event()
    elif option == "4":
        view_events()
    elif option == "5":
        get_days_until_events(Event.events)  # Pass the events list to the function
    elif option == "6":
        code = input("Enter the code to automatically create preset events: ")
        if code == "X5FCY3":
            Event.create_preset_events()  # Call the class method
        else:
            print("Invalid code. Please try again.")
    elif option == "7":
        print("Exiting the program.")
    else:
        print("Invalid option. Please try again.")
        main()


main()