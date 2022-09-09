import datetime
from time import time
import main


repeat = 100000
t0 = time()
for _ in range(repeat):
	main.main()

print((time() - t0)/repeat, time() - t0)


print(str(datetime.time(8)))
