import os
import ffmpeg
import subprocess
import whisper
import googletrans


# --------Converting Video into Audio file------------------------------
def convertVideoToMp3(input_file,output_file):
    ffmpeg_cmd = ["ffmpeg","-i",input_file,"-vn","-acodec","libmp3lame","-ab","192k","-ar","44100","-y",output_file]
    
    # ffmpeg -i
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully Converted")
    except subprocess.CalledProcessError as e:
        print("Conversion error")
        

convertVideoToMp3('video.mp4','audio.mp3')

# --------Converting audio file into Transcription ---------------------


model = whisper.load_model("base")
result = model.transcribe("audio.mp3",fp16=False,language='English')

with open("transcription.txt","w") as f:
    f.write(result["text"])