import os


def clear():
    videos = list(filter(lambda f: ".mp4" in f or ".webm" in f, os.listdir()))
    if videos:
        for video in videos:
            os.remove(video)
            print("The file has been deleted successfully")

    if os.path.exists("output.png"):
        os.remove("output.png")
    else:
        print("The file does not exist!")
