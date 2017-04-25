import progressbar
import string
import time
iterations = 100

values = string.ascii_lowercase

pb = progressbar.ProgressBar(max_value=len(values), redirect_stdout=True)

# Enumerating a range
for index, value in enumerate(values):
    print value
    pb.update(index)
    time.sleep(0.1)
pb.finish()

pb2 = progressbar.ProgressBar(max_value=len(values), redirect_stdout=True)
for value in values:
    print value
    pb2.update(pb2.value+1)
    time.sleep(0.1)
pb2.finish()
