import argparse


def mycd(curr: str, target: str) -> str:
    """
    Simulates a Unix cd command. Assumes the user starts in the curr directory and
    wants to change to the target directory.
    Args:
        curr: the starting directory
        target: the ending directory
    Return:
        The file path representing the target directory
    """
    curr_path = curr.split("/")
    target_path = target.split("/")

    # Filter the paths
    curr_path = [el for el in curr_path if el != ""]
    target_path = [el for el in target_path if el != "" and el != "."]

    if target.startswith("/"):
        curr_path = []

    # Process every element in the target path
    for element in target_path:
        if element == "..":
            if len(curr_path) > 0:
                curr_path.pop()
        elif not element.isalnum():
            return element + ": No such file or directory"
        else:
            curr_path.append(element)

    res = "/".join(curr_path)
    return '/' + res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mycd to change directory")
    parser.add_argument(dest="source", help="current directory")
    parser.add_argument(dest="target", help="target directory")
    args = parser.parse_args()

    print(mycd(args.source, args.target))
