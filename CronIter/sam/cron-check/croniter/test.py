
from croniter import croniter
from datetime import datetime
import pytz
tz = pytz.timezone("Japan")
today = datetime.now()
local_date = tz.localize(today)

print(local_date.date())
print(today.date())

cron  = "0 0 * * wed"
iter  = croniter(cron, today)

# Check if a cron logic matches today
if iter.get_prev(datetime).date() == today.date():
    print("OK")
else:
    print("NOK")