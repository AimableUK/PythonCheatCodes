
import time 
from plyer import notification

def send_notification(title,message,timeout):
	notification.notify(
		title = title,
		message = message,
		timeout = timeout
		)

if __name__ == "__main__":
	while True:
		notification.notify(
			title = "get time to rest",
			message = "its too late may be you can get time to rest",
			timeout = 15)
		time.sleep(3600)