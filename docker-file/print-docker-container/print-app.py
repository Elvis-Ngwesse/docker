import os
import getpass
import platform
import shutil


def list_directory(path, label=None):
    label_str = f" ({label})" if label else ""
    print(f"\n📁 Contents of: {path}{label_str}")
    try:
        if not os.path.exists(path):
            print(" [Path does not exist]")
            return
        for item in os.listdir(path):
            print(" -", item)
    except Exception as e:
        print(" [Error]:", e)


def get_desktop_path(system, username):
    if system == "Windows":
        return os.path.join("C:\\Users", username, "Desktop")
    elif system == "Darwin":
        return os.path.join("/Users", username, "Desktop")
    else:
        return os.path.join("/home", username, "Desktop")


def main():
    # Get user info and system platform
    username = getpass.getuser()
    system = platform.system()
    print(f"👋 Hello, {username}! Detected OS: {system}")

    # Paths
    desktop_path = get_desktop_path(system, username)
    root_path = "C:\\" if system == "Windows" else "/"

    # List files
    list_directory(desktop_path, "Desktop")
    list_directory(root_path, "Root Directory")


if __name__ == "__main__":
    main()
