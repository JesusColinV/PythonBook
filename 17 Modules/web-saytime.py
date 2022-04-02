# This is an exercise file from Python 3 Training by Jesus Colín


import time, saytime

t = time.localtime()
print("Content-type: text/html\n")
print(
    "In Phoenix, Arizona, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
)


