import os
import librosa
import soundfile as sf
import numpy as np
import shutil

#y_noise,sr_noise = librosa.core.load("noise.wav", sr=22050, mono=True)
# wavの変換の関数
def copy_audio_by_length(in_path,outpath,max_duration,move=False):
    total = 0
    filenames = os.listdir(in_path)
    file_count = 0
    for filename in filenames:
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            d =librosa.get_duration(filename=in_path+"/"+filename)
            src_file = os.path.join(in_path,filename)
            dst_file = os.path.join(outpath,filename)
            if move:
                os.rename(src_file, dst_file)
            else:
                shutil.copy(src_file, dst_file)
            
            total += d
            file_count += 1
            if total > max_duration:
                break
    return total,file_count
    
           
    
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',"-i" , help='input dir',required=True)
parser.add_argument('--duration_sec',"-sec" , help='audio_duration',required=True,type=int)
parser.add_argument('--output',"-o" ,required=True)
parser.add_argument('--move',"-m" ,action="store_true")

args = parser.parse_args()
# TODO check file

total,file_count = copy_audio_by_length(args.input,args.output,args.duration_sec,args.move)
min = total/60.0
action = "moved" if args.move else "copied"
print(f"{file_count} files {action}.{int(total):03d} sec/{min:.2f} min")