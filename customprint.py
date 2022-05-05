import sys
import time


class CustomPrint:

    @staticmethod
    def printC(text="", delay=0.01):
        """Method to print each character in a string individually"""
        print(delay)
        for l in str(text):
            sys.stdout.write(l)
            sys.stdout.flush()

            if delay > 0.001: time.sleep(int(delay))
        print()

    @staticmethod
    def printD(text="", delay=0.01):
        """Method to print a string with a delay"""
        print(str(text))
        time.sleep(int(delay))
