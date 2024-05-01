class colors:
    IN_PROGRESS = "\033[96m"
    WARNING = "\033[93m"
    SUCCESS = "\033[92m"
    ERROR = "\033[91m"
    RESET = "\033[0m"


class Print:
    def i(msg=""):
        print(f"{colors.IN_PROGRESS}{msg}{colors.RESET}")


    def w(msg=""):
        print(f"{colors.WARNING}{msg}{colors.RESET}")


    def s(msg=""):
        print(f"{colors.SUCCESS}{msg}{colors.RESET}")


    def e(msg=""):
        print(f"{colors.ERROR}{msg}{colors.RESET}")
