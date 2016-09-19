import webbrowser
import time

total_breaks = 3
breaks_count = 0

print("Take a break program start on", time.ctime())
while(breaks_count < total_breaks):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=Obsu1v9NvEc")
    breaks_count += 1
print("Take a break program stop on", time.ctime())