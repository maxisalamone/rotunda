Since the exercise asked for a general approach:

1. This will be solved by a simple script running in the background
2. The script will read from the error file every minute, parsing the last 11 entries' timestamps (since it asks for MORE than 10)
3. With the timestamps, it will count if those were registered under 60 seconds
4. if so, it will execute a mail sending routine, otherwise, do nothing.
