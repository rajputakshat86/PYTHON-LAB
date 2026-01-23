total_seconds = 5000

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours)
print(minutes)
print(seconds)
