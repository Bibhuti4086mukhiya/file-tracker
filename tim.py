from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')
    return current_time
print(time())

