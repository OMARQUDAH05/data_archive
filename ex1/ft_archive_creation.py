import sys
import typing


def main() -> None:
    edit_version = ""
    file: typing.IO[str] | None = None
    new_file: typing.IO[str] | None = None
    new_file_n = ""
    if (len(sys.argv) < 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {sys.argv[1]}")

        try:
            file = open(sys.argv[1], 'r')
            content = file.read()
            print("---")
            print()
            print(content)
            print()
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
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return
        finally:
            if file is not None:
                file.close()
                print(f"File ’{sys.argv[1]}’ closed.")

    except Exception as e:
        print(e)
        return
    print("Transform data:")
    print("---")
    print()
    print(edit_version)
    print()
    print("---")
    new_file_n = input("Enter new file name (or empty): ")
    if (new_file_n == ""):
        print("")
    try:
        new_file = open(new_file_n, 'w')
        print(f"Saving data to ’{new_file_n}’")
        print(f"Data saved in file ’{new_file_n}’.")
        new_file.write(edit_version)
    except Exception as e:
        print(f"{e}")

    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    main()
