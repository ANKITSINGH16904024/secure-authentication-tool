import exifread

file_name = input("Enter image file name: ")

try:
    with open(file_name, "rb") as f:
        tags = exifread.process_file(f)

        if not tags:
            print("No EXIF data found 📭")
        else:
            print("\nEXIF Data:\n")
            for tag in tags:
                print(f"{tag}: {tags[tag]}")

except FileNotFoundError:
    print("File not found ❌")

except Exception:
    print("Not an image or no EXIF ❌")
