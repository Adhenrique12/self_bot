import os


def clear():
    video = list(filter(lambda x: x.endswith('.mp4'), os.listdir(".")))
    if video:
        video = video[0]
        os.remove(video)
        print("The file has been deleted successfully")
    
    if os.path.exists("output.png"):
        os.remove("output.png")
    else:
        print("The file does not exist!")