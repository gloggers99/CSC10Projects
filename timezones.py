import datetime
import pytz

zones_file = open("zones.csv", "r")
zones_file_content = zones_file.read()
zones_file.close()

timezones: [str, datetime.datetime] = {}
time_format = "%A %B %d, %X %p, %Y"

for line in zones_file_content.splitlines():
    timezones[line.split(',')[2]] = datetime.datetime.now(pytz.timezone(line.split(',')[2]))

print('*'*10+"Current Time"+'*'*10)
print(timezones["America/Los_Angeles"].strftime(time_format))

user_timezone_choice = input("Enter another timezone name: ").replace(' ', '_')

final_timezone = None
for name, timezone in timezones.items():
    if name != user_timezone_choice:
        if name.split('/')[1] == user_timezone_choice:
            final_timezone = timezone
            break
        elif name.casefold() == user_timezone_choice.casefold():
            final_timezone = timezone
            break
        elif name.split('/')[1].casefold() == user_timezone_choice.casefold():
            final_timezone = timezone
            break

if final_timezone is None:
    print("There is no timezone under that name!")
    exit(1)

print(final_timezone.strftime(time_format))

difference = 0
if timezones["America/Los_Angeles"].day > final_timezone.day:
    difference += 24
elif timezones["America/Los_Angeles"].day < final_timezone.day:
    difference -= 24

if timezones["America/Los_Angeles"].hour > final_timezone.hour:
    difference = difference + (timezones["America/Los_Angeles"].hour - final_timezone.hour)
if timezones["America/Los_Angeles"].hour < final_timezone.hour:
    difference = difference - (final_timezone.hour - timezones["America/Los_Angeles"].hour)

if difference < 0:
    print("Los Angeles is behind by " + str(abs(difference)) + " hours.")
elif difference > 0:
    print("Los Angeles is ahead by " + str(abs(difference)) + " hours.")
else:
    print("Los Angeles is exactly the same as that timezone somehow!")
