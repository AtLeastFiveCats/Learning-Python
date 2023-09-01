import time
#gmtime is zulu time
print(time.gmtime())
#time() is the seconds since the epoch, default is midnight on Jan 1 1970
print(time.time())
#time_ns() is like time() but in nanoseconds
print(time.time_ns())
#ctime() is the current time and data in an easily readable format
print(time.ctime())
#ctime() can also take arguments in seconds to store the time/date before current date
print(time.ctime(time.time()))

print(time.ctime(10000))

print(time.ctime(1000000))
#Tuple is storing the time as a more readable form.
time_tuple = (2023, 8, 29, 10, 52, 2, 2, 0, 1)
#struct_time converts time_tuple to an easier to read format
time_object = time.struct_time(time_tuple)
print(time_object)
#With struct_time I am able to pull certain values out of time_tuple by name.
print(time_object.tm_mon)
#localtime() produces a struct_time for the current time/date
print(time.localtime())

time_zone = time.localtime()
#.tm_zone tells what local time zone the program is in
print(time_zone.tm_zone)
#.tm_gmtoff tells how far from GMT in seconds local time is
print(time_zone.tm_gmtoff)
#mktime() must use local time, it converts struct_time objects into seconds since epoch
print(time.mktime(time.localtime()))
#asctime() needs a struct_time object and turns it into a string, a struct_time argument can be passed to it. Without an argument however it will use localtime()
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
#strftime() is similar to asctime() but can be formated, it can take two arguments, one for formatting and the other is an optional time argument.
print(time.strftime("The current date is: %m-%d-%y", time.localtime()))
#strptime() is the inverse of strftime(), it turns a timestamp into a struct_time() object
print(time.strptime("9-24-2002", "%m-%d-%Y"))
#sleep() suspends the code excution for X amount of seconds, the seconds could also be fractional
time.sleep(1)
#perf_counter() is placed at the start and end of the code and counts how long the code took to excute.
start = time.perf_counter()
end = time.perf_counter()
print(start - end)
