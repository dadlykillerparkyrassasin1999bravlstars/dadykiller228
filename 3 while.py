import time
num = 2
while num <= 1024:
    print(num)
    time.sleep(1)
    num = (num * num)
print("BOOM")