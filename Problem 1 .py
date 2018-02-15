def find_last(ss,ts):
    current_location=ss.find(ts,0)
    next_location=ss.find(ts,current_location+1)
    while  next_location >= 0:
        current_location=ss.find(ts,next_location)
        next_location=ss.find(ts,current_location+1)
    return current_location



print find_last("aaaa","a")
print find_last("zeez","ez")
