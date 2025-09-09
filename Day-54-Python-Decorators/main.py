import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
  start_time = time.time()
  function()
  end_time = time.time()
  run_speed = end_time-start_time
  print(f"{function.__name__} run speed: {run_speed}s")
  return function
  
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i