"""
JSON file navigator.
"""
import json
import sys
import argparse


def open_json(path):
    """
    Opens json file and returns the data.
    """
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def ask_index(data):
    """
    Checks an input and returns it.
    """
    print(f"Choose an index from 0 to {len(data)-1}:")
    try:
        ind = int(input(">>> "))
    except ValueError:
        ind = ask_index(data)

    if not 0 <= ind <= (len(data)-1):
        ind = ask_index(data)

    return ind


def ask_key(data):
    """
    Checks an input and returns it.
    """
    print(list(data.keys()))
    print("Сhoose a key:")
    key = input(">>> ")

    if key not in data.keys():
        key = ask_key(data)
    return key


def check_data(data):
    """
    Checks the type of data and returns an object.
    """
    if isinstance(data, list):
        if len(data) == 0:
            print("The list is empty.")
            navigate()
        else:
            ind = ask_index(data)
            return data[ind]
    elif isinstance(data, dict):
        key = ask_key(data)
        return data.get(key)


def navigate():
    """
    Starts the search again from the root or exits.
    """
    print("Choose 'root' or 'exit':")
    inp = input(">>> ")
    if inp == "exit":
        sys.exit()
    elif inp == "root":
        main()
    else:
        navigate()


def parse_args():
    """
    Returns the path.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    return parser.parse_args()


def main():
    """
    Main cycle of search.
    """
    args = parse_args()
    data = open_json(args.path)
    while isinstance(data, (dict, list)):
        data = check_data(data)
    print(data)
    navigate()


if __name__ == "__main__":
    main()
