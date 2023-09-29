"""
Create a Python file named lab_3-5.py

Import the time and math modules.

Calculate 22 using math.pow and again using the ** operator.

Record the time using time.process_time before and after each calculation (Hint: you may need to store the result of time.process_time in a variable)

Add a statement that prints the elapsed time after each statement is processed. Run the program. What do you notice? Write it as a comment.

Change each statement that records the time to use time.perf_counter instead of time.process_time.

Run the program again. What do you notice? Write it as a comment.
"""

import time
import math

start_time = time.process_time()
result_pow = math.pow(2, 2)
end_time = time.process_time()
elapsed_time_pow = end_time - start_time

start_time = time.process_time()
result_operator = 2 ** 2
end_time = time.process_time()
elapsed_time_operator = end_time - start_time

print(f"Using math.pow: Result = {result_pow}, Elapsed Time: {elapsed_time_pow} seconds")
print(f"Using ** operator: Result = {result_operator}, Elapsed Time: {elapsed_time_operator} seconds")

#shows elapsed time as always being 0 seconds

start_time = time.perf_counter()
result_pow = math.pow(2, 2)
end_time = time.perf_counter()
elapsed_time_pow = end_time - start_time

start_time = time.perf_counter()
result_operator = 2 ** 2
end_time = time.perf_counter()
elapsed_time_operator = end_time - start_time

print(f"Using math.pow with perf_counter: Result = {result_pow}, Elapsed Time: {elapsed_time_pow} seconds")
print(f"Using ** operator with perf_counter: Result = {result_operator}, Elapsed Time: {elapsed_time_operator} seconds")

#shows elapsed time that changes every time I run the program, not always at 0 seconds like before. 
