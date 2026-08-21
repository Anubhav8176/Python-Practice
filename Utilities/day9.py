import time
import winsound

# Tasks for implementing the countdown timer:
# Task 1: Take the user input in proper and workable format. Done
# Task 2: Build a countdown timer in the background. Done
# Task 3: Displaying the countdown on the screen (Properly not just a new line every time). Done
# Task 4: Format the timer that is displaying on the screen. Done
# Task 5: Add a beep sound when the timer stopped. Done

def countdown_timer(timer_seconds: int):
	while timer_seconds >= 0:
		minutes = timer_seconds//60
		seconds = timer_seconds%60
		
		print(f"{minutes:02d}:{seconds:02d}", end="\r")
		if timer_seconds == 0:
			print("Time's Up! You can stop now.")
			winsound.Beep(frequency=500, duration=1000)
		
		time.sleep(1)
		timer_seconds -= 1


def main():
	timer_seconds = int(input("Enter the time in seconds: "))
	countdown_timer(timer_seconds)

if __name__ == "__main__":
	main()