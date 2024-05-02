#transforming seconds in hours and minutes and also seconds
time = int(input("How many seconds does it take to do the task in seconds?: "))
print(f"\nHours: {time // 3600}\nMinutes: {(time % 3600) // 60}\nSeconds: {(time % 3600) % 60}")