# this module will, in the future, be a pomodoro timer included in the application
from datetime import time

class PomodoroTimer:
    def __init__(
        self,
        concentration_timer: float=25,
        break_timer: float=5,
        break_cadence:int=4,
        long_break_timer:float=25,
    ):
        self.concentration_timer = concentration_timer
        self.break_timer = break_timer
        self.break_cadence = break_cadence
        self.long_break_timer = long_break_timer

    def __str__(self):
        return f"Concentration time: {self.concentration_timer} minute(s). \n Break time: {self.break_timer} minute(s). \n Small breaks before long break: {self.break_cadence}. \n Long break time: {self.long_break_timer} minute(s). \n"

    def set_time_blocks(self):
        incoming_work_timer = input(
            "Please input the length of your concentration period, in minutes."
        )
        self.concentration_timer = incoming_work_timer

        incoming_break_timer = input(
            "Please input the length of your break period, in minutes."
        )
        self.break_timer = incoming_break_timer

        incoming_break_cadence = input(
            "Please input the number of regular breaks you would like before starting a long break. If you do not want to include long breaks, press Enter:"
        )
        if incoming_break_cadence:
            self.break_cadence = incoming_break_cadence
            incoming_long_break_timer = input(
                "Please input the length of the long break:"
            )
            self.long_break_timer = incoming_long_break_timer
        else:
            self.break_cadence = None
            self.long_break_timer = None


# test pomodoro logic
"""test_pomodoro = PomodoroTimer()
print(test_pomodoro)
test_pomodoro.set_time_blocks()
print(test_pomodoro)"""
