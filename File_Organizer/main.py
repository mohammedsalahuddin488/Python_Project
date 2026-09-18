import os

a = input(f"name the photo:")

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    # i = 1
    # for files in files_with_ext:
    #     os.rename(files, f"photo-{i}{ext}")
    #     i += 1
    if not(os.path.exists("Images")):
        os.mkdir("Images")
    for i, files in enumerate(files_with_ext):
        os.rename(files, f"Images/{a}{i+1}{ext}")

if __name__=="__main__":
    files = os.listdir()

    arrange_files(files, ".jpg")
