import os
import shutil
import sys


def move_jpg_files(source_folder, destination_folder):
    if not os.path.isdir(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):
            destination_path = os.path.join(destination_folder, filename)

            # Avoid overwriting an existing file.
            if os.path.exists(destination_path):
                name, extension = os.path.splitext(filename)
                counter = 1
                while True:
                    new_name = f"{name}_{counter}{extension}"
                    destination_path = os.path.join(
                        destination_folder, new_name
                    )
                    if not os.path.exists(destination_path):
                        break
                    counter += 1

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"\nCompleted. {moved_count} JPG file(s) moved.")


def main():
    if len(sys.argv) == 3:
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
    else:
        print("=== JPG File Automation ===")
        source_folder = input("Enter source folder: ").strip()
        destination_folder = input("Enter destination folder: ").strip()

    move_jpg_files(source_folder, destination_folder)


if __name__ == "__main__":
    main()
