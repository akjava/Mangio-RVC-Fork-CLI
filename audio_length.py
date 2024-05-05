import os
import librosa
import soundfile as sf
import numpy as np


#y_noise,sr_noise = librosa.core.load("noise.wav", sr=22050, mono=True)
# wavの変換の関数
def audio_length(in_path):
    total = 0
    filenames = os.listdir(in_path)
    for filename in filenames:
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            #print(in_path+filename)
            
            d =librosa.get_duration(filename=in_path+"/"+filename)
            total += d
            #print(d)
    return total
           
    
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',"-i" , help='input dir')
parser.add_argument('--base_dir',"-b" , default='/notebooks/')

parser.add_argument('--key',"-k" , help='input dir')
args = parser.parse_args()

if args.input is None and args.key is None:
    print("need input dir or Mangio-RVC-Fork-CLI/logs/{key}/0_gt_wavs")
    exit(1)

key = args.key

path  = os.path.join(args.base_dir,args.input)
if key is not None:
    path = f"Mangio-RVC-Fork-CLI/logs/{key}/0_gt_wavs"
else:
    parent_path,filename = os.path.split(path)
    basename,ext = os.path.splitext(filename)
    key = basename
          
total = audio_length(path)
min = total/60.0
epoch = 500/min
print(path)



print(f"{int(total):03d} sec :{min:.2f} min suggested epoch = {epoch:.2f}")
#print(f"total:{total}")
khz = 32
batch_size = 16
suggest_epoch = int(round(epoch/5)+2) * 5 
patterns = [
    "{key} /notebooks/{key}/ {khz}k 24",
    "{key} 0 1 1 rmvpe 128 v2", #sometime batch 8broken
    "{key} cv2",
    "{key} {khz}k 1 0 5 {suggest_epoch} {batch_size} 0 1 0 1 v2"
]
for pattern in patterns:
    #print(fpattern)
    print(pattern.format_map(locals()))