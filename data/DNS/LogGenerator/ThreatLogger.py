import logging
import logging.handlers

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = ('test.sfn', 5514))

formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)


def main():
    with open("log.csv") as logFile:
        for line in logFile:
            log.info(f"{line}")
            print(f"{line}")

if __name__ == '__main__':
	main()