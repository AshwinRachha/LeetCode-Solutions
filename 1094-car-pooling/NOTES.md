trips.sort(key = lambda x : x[1] - x[2])
prev, start_prev, end_prev = None, None, None
for trip in trips:
passangers, start, end = trip
if not prev or start >= end:
prev, start_prev, end_prev = passangers, start, end
else:
if start < end_prev and prev + passangers > capacity:
return False
else:
prev += passangers
end_prev = end
return True