import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(2*60)
    webbrowser.open("https://www.youtube.com/watch?v=twZODj0yERs")
    break_count = break_count + 1
