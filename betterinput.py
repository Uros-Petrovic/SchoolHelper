class FloatInput:

    @staticmethod
    def floatInput(prompt="Enter a float: ", cancel="x"):
        """Method to safely get a float value, for convenience."""

        while True:
            try:
                val = input(prompt[:-2] + " (" + cancel + " to exit)" + prompt[-2:])
                return "0" if val == cancel else float(val)
            except ValueError:
                print("Invalid value")
                continue

    @staticmethod
    def floatInputRepeat(promptList=["Enter a float: "], cancel="x"):
        """Method to get a list of float values."""
        inputList = []
        for x in range(len(promptList)):
            inputList.append(FloatInput.floatInput(promptList[x], cancel))
        return inputList


class IntInput:

    @staticmethod
    def intInput(prompt="Enter a int: ", cancel="x"):
        """Method to safely get a int value, for convenience."""

        while True:
            try:
                val = input(prompt[:-2] + " (" + cancel + " to exit)" + prompt[-2:])
                return "0" if val == cancel else int(val)
            except ValueError:
                print("Invalid value")
                continue

    @staticmethod
    def intInputRepeat(promptList=["Enter a int: "], cancel="x"):
        """Method to get a list of int values."""
        inputList = []
        for x in range(len(promptList)):
            inputList.append(IntInput.intInput(promptList[x], cancel))
        return inputList


class BetterInput:

    @staticmethod
    def getIntInputRange(prompt="Enter a range (lowest->highest): ", cancel="x"):
        while True:
            try:
                vals = input(prompt).split()
                for x in range(len(vals)):
                    vals[x] = int(vals[x])
                return list(range(min(vals), max(vals) + 1))
            except ValueError:
                print("Invalid range")
                continue
