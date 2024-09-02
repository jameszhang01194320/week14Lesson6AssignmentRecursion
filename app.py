def find_file(file_system, target):
    for item in file_system:
        if isinstance(item, list):
            # If the item is a folder (a list), we need to search inside it recursively
            if find_file(item, target):
                return True
        elif item == target:
            # If the item is the target file, print "big HOORAY" and return True
            print("big HOORAY")
            return True
    return False  # If the file is not found in the current folder

# Test the function with the provided file system and target
file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"
find_file(file_system, target)
