import sys


def main() -> None:
    try:
        if (len(sys.argv) < 2):
            raise Exception("Usage: ft_ancient_text.py <file>")
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file {sys.argv[1]}")

        try:
            file = open(sys.argv[1], 'rt')
            content = file.read()
            print("---")
            print()
            print(content)
            print("---")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            file.close()
            print(f"File ’{sys.argv[1]}’ closed.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
