from client import Programme


def main() -> int:
    programme = Programme()

    while programme.running:
        programme.runCycle()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
