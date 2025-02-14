import os

def update_icon(file_path, new_icon_path):
    """
    Updates the Icon line in a .desktop file with a new icon path.

    Args:
        file_path (str): The path to the .desktop file.
        new_icon_path (str): The new path for the icon.

    """
    try:
        # Read the file contents
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Modify the Icon line and write the file back
        with open(file_path, "w") as file:
            for line in lines:
                if line.startswith("Icon="):
                    file.write(f"Icon={new_icon_path}\n")
                else:
                    file.write(line)

        print(f"Icon path for {os.path.basename(file_path)} updated successfully.")

    except PermissionError:
        print(f"Permission denied: Try running this script with elevated permissions (sudo) for {file_path}.")
    except FileNotFoundError:
        print(f"File not found: Check that the path to {file_path} is correct.")


# Paths and icons for each application
applications = {
    "brave-browser": "/usr/share/applications/brave-browser.desktop",
    "spotify": "/usr/share/applications/spotify.desktop",
    "gnome-todo": "/usr/share/applications/org.gnome.Todo.desktop",
    "nvim": "/usr/share/applications/nvim.desktop",
    "alacritty": "/usr/share/applications/Alacritty.desktop",
    "vesktop": "/usr/share/applications/vesktop.desktop",
    "obsidian": "/usr/share/applications/obsidian.desktop",

}

new_icons = {
    "brave-browser": "/home/lakshan/Applications/resetIcons/CustomIcons/brave-desktop.svg",
    "spotify": "/home/lakshan/Applications/resetIcons/CustomIcons/spotify.svg",
    "gnome-todo": "/home/lakshan/Applications/resetIcons/CustomIcons/org.gnome.Todo.svg",
    "nvim": "/home/lakshan/Applications/resetIcons/CustomIcons/nvim.svg",
    "alacritty": "/home/lakshan/Applications/resetIcons/CustomIcons/alacritty.svg",
    "vesktop": "/home/lakshan/Applications/resetIcons/CustomIcons/clamtk.svg",
    "obsidian": "/home/lakshan/Applications/resetIcons/CustomIcons/obsidian.svg",
}

# Update icons for each application
for app, path in applications.items():
    update_icon(path, new_icons[app])
