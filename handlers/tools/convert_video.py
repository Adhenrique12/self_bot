import ffmpeg

def convert_video(input_file):
     
    output_file = "output.mp4"
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vcodec='libx264', acodec='aac')
        .run()
    )
    