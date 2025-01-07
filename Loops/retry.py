'''Exponential Backoff
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.'''
import time
max_retry = 5
wait_time = 1
attempt = 0
while attempt < max_retry:
    print("Attempt", attempt+1,"-wait time is",wait_time)
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempt = attempt + 1