#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
from datetime import datetime, timedelta

schedule_minutes = [525, 575, 630, 695, 745, 795, 845, 895]
text_space_count = 0
rjust = True


def get_next_hour_minutes(hours_minutes, now_minutes):
    for minutes in schedule_minutes:
        differs = minutes - now_minutes
        if differs > 0:
            minutes_to_end = differs
            return minutes_to_end


def get_now_in_minutes():
  # Geting now time in minutes
  now_minutes = time.localtime().tm_hour * 60 + time.localtime().tm_min
  return now_minutes


def opposite_boolean(bool):
    return not bool

def shutdown_computer(shutdown_info):
  if shutdown_info == 'y':
    print('The end, shutting down')
    os.system('shutdown /s /t 1')

  if shutdown_info == 'n':
    exit()

if __name__ == '__main__':
        

def set_argparse():
	parser = argparse.ArgumentParser(description='Shows time to the end of period.')
	parser.add_argument('--shutdown', '-s', action='store_true', default=False, help='Will shutdown the computer at end.')

	return parser.parse_args()


def main():
  # Sets the Argpars and runs the timer
  args = set_argparse()
  shutdown_info = "y" if args.shutdown is not None else "n"
  end_setting = "y"   
	
  next_hour_time = 0

  if end_setting == "y":
    # Geting now time in minutes
    now_minutes = get_now_in_minutes()

    # Getting minutes to the next hour
    minutes_to_end = get_next_hour_minutes(schedule_minutes, now_minutes)
    next_hour_time = datetime.now() + timedelta(minutes=minutes_to_end)

  if end_setting == "n":
    # User wants to enter end time manually
    print("lol")
    
    # Geting now time in minutes
    now_minutes = get_now_in_minutes()

    to_end = input("Minutes to end: ")

    # Getting minutes to the next hour
    minutes_to_end = get_next_hour_minutes(int(to_end), now_minutes)
    next_hour_time = datetime.now() + timedelta(minutes=minutes_to_end)

  # Getting formated time when hours end
  ends = datetime.strptime(next_hour_time.strftime('%H:%M:%S'), '%H:%M:%S')

  while True:
    # Getting now time
    now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')

    # Printing the time
    timer = str(ends - now)
    s = " "
    spaced_time = timer.rjust(len(timer) + text_space_count)
    timer_text = spaced_time + spaced_time + spaced_time

    print(timer_text)

    # Slow downing print
    time.sleep(0.08)

    if timer[0] == '-':
        shutdown_computer(shutdown_info)
    
    if text_space_count > 50:
     rjust = opposite_boolean(rjust)

    if text_space_count == 0:
     rjust = True

    # Reseting spaces
    if rjust:
     text_space_count += 2
    else:
     text_space_count -= 2
