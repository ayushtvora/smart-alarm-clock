# smart-alarm-clock
I want to make an app-controlled alarm clock. I don't know how. 

## The Goals
### Tech Stack
- The clock will use a Raspberry Pi connected to a display and speaker. Depending on functionality, we can add more if needed.
- The clock will be connected to the Internet, which takes in data from an API created using FastAPI.
- The app will be created in React Native, which will also talk to the API.
- The API will talk to the DB that will store user data, such as what alarms they have and any user settings.
- All of this will be stored in Docker somewhere
### Features
- Clock can display time, next alarm, internet connectivity, etc.
- Add alarms to the clock through the app.
- The alarm should go off when it is time.
- Snoozing (but let the user choose if they want to snooze).
- Scheduled alarms based on sunrise for weekends.
- Play notifications about weather, daily tasks, and any reminders when waking up.
- Notify when it is bedtime.