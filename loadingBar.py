# This contains the main code
import time

GREEN = "\033[32m"
RED = "\033[31m"

RESET = "\033[0m"  # Resets to default terminal color


class LoadingBar:
    def __init__(
        self, on_emoji: str, off_emoji: str, capacity: int, isPercentage: bool = False
    ):
        self.on_emoji = on_emoji
        self.off_emoji = off_emoji
        self.capacity = capacity
        self.isPercentage = isPercentage

    def print_bar(self, value, end=False):

        output = ""
        if value > self.capacity:
            return "Error: value must be smaller than or equal to total capacity"
        else:
            for i in range(0, self.capacity):
                if i < value:
                    output = output + self.on_emoji
                else:
                    output = output + self.off_emoji

        if self.isPercentage:
            if not end:
                print(
                    f"{output} {GREEN if value == self.capacity else RED} {round(value / self.capacity * 100)}% {RESET}",
                    end="\r",
                )
            else:
                print(
                    f"{output} {GREEN if value == self.capacity else RED} {round(value / self.capacity * 100)}% {RESET}",
                    end="\n",
                )
        else:
            if not end:
                print(
                    f"{output} {GREEN if value == self.capacity else RED} {value}/{self.capacity} {RESET}",
                    end="\r",
                )
            else:
                print(
                    f"{output} {GREEN if value == self.capacity else RED} {value}/{self.capacity} {RESET}",
                    end="\n",
                )


# Basic tests
if __name__ == "__main__":
    testBar = LoadingBar("🟩", "⬜️", 10)

    for i in range(0, testBar.capacity + 1):
        testBar.print_bar(i, False if i < testBar.capacity else True)
        time.sleep(0.5)
