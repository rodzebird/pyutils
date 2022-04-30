import os

from colorama import Fore, Style

from pyutils.atomic import to_bool


class Environment:
    def __init__(self, verbose, silent, debug, local, dev, dry_run):
        self.__verbose = to_bool(verbose)
        self.__silent = to_bool(silent)
        self.__debug = to_bool(debug)
        self.__local = to_bool(local)
        self.__dev = to_bool(dev)
        self.__dry_run = to_bool(dry_run)

        self.__initialized = False

    @staticmethod
    def from_env(prefix=""):
        return Environment(
            verbose=os.environ.get(f"{prefix}VERBOSE"),
            silent=os.environ.get(f"{prefix}SILENT"),
            debug=os.environ.get(f"{prefix}DEBUG"),
            local=os.environ.get(f"{prefix}LOCAL"),
            dev=os.environ.get(f"{prefix}DEV"),
            dry_run=os.environ.get(f"{prefix}DRY_RUN"),
        )

    def apply(self):
        os.environ["ENV_VERBOSE"] = str(self.__verbose)
        os.environ["ENV_SILENT"] = str(self.__silent)
        os.environ["ENV_DEBUG"] = str(self.__debug)
        os.environ["ENV_LOCAL"] = str(self.__local)
        os.environ["ENV_DEV"] = str(self.__dev)
        os.environ["ENV_DRY_RUN"] = str(self.__dry_run)

        self.__initialized = True

    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"

    def __str__(self):
        return f"{Fore.MAGENTA}<Environment {Fore.YELLOW}debug={Fore.CYAN}{self.__debug}{Fore.YELLOW}, local={Fore.CYAN}{self.__local}{Fore.YELLOW}, dev={Fore.CYAN}{self.__dev}{Fore.YELLOW}, dry_run={Fore.CYAN}{self.__dry_run}{Fore.MAGENTA}>{Style.RESET_ALL}"

    @property
    def initialized(self):
        return self.__initialized

    @staticmethod
    def __is(value):
        if value in (None, ""):
            return False
        return value.lower() in ("true", "1", "t")

    @staticmethod
    def verbose():
        return Environment.__is(os.environ.get("ENV_VERBOSE"))

    @staticmethod
    def silent():
        return Environment.__is(os.environ.get("ENV_SILENT"))

    @staticmethod
    def debug():
        return Environment.__is(os.environ.get("ENV_DEBUG"))

    @staticmethod
    def local():
        return Environment.__is(os.environ.get("ENV_LOCAL"))

    @staticmethod
    def dev():
        return Environment.__is(os.environ.get("ENV_DEV"))

    @staticmethod
    def dry_run():
        return Environment.__is(os.environ.get("ENV_DRY_RUN"))


def dry_run_log(msg="Dry Run mode activated, operation is deactivated"):
    print(f"🚧 {Fore.LIGHTYELLOW_EX}{msg}{Style.RESET_ALL} 🚧\n")


def dry_run_log_exec():
    dry_run_log("Dry Run mode activated, execution handling is deactivated")


def dry_run_log_discord():
    dry_run_log("Dry Run mode activated, Discord messaging is deactivated")


def dry_run_log_pubsub():
    dry_run_log("Dry Run mode activated, Pub/Sub messaging is deactivated")
