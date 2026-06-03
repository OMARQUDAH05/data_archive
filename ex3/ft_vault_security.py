def secure_archive(
        name: str, option: str = "read", content: str = ""
        ) -> tuple[bool, str]:
    if (option.lower() == "read"):
        try:
            with open(name, 'r') as file:
                content = file.read()
            return (True, content)
        except Exception as e:
            return (False, f"{e}")
    elif (option.lower() == "write"):
        try:
            with open(name, 'w') as file:
                file.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, f"{e}")
    return (False,"")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("omaring", "read"))
    print()
    print("Using ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("omar", "read"))
    print()
    tup = secure_archive("file", "read",)
    print("Using ’secure_archive’ to read from a regular file:")
    print(tup)
    print()
    print("Using ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("oo", "write", tup[1]))


if __name__ == "__main__":
    main()
