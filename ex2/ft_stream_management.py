import sys
import typing


def main() -> None:
    edit_version = ""
    new_file: typing.IO[str] | None = None
    file: typing.IO[str] | None = None
    new_file_n = ""
    file_n = sys.argv[1]
    if (len(sys.argv) < 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file {file_n}")

        try:
            file = open(sys.argv[1], 'r')
            content = file.read()
            print("---")
            print()
            print(content)
            print("---")
            for i in content:
                if (i == '\n'):
                    edit_version += "#"
                    edit_version += i
                else:
                    edit_version += i
            if (edit_version[len(edit_version) - 1]):
                edit_version += "#"

        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file ’{file_n}’: {e}")
            return
        finally:
            if file is not None:
                file.close()
                print(f"File ’{sys.argv[1]}’ closed.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file ’{file_n}’: {e}")
        return
    print("Transform data:")
    print("---")
    print()
    print(edit_version)
    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_n = sys.stdin.readline().strip('\n')
    try:
        new_file = open(new_file_n, 'w')
        print(f"Saving data to ’{new_file_n}’")
        print(f"Data saved in file ’{new_file_n}’.")
        new_file.write(edit_version)
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file ’{new_file_n}’: {e}\n")

    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    main()
