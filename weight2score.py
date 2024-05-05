import batch_rvc

index = "None"
#index = "logs/cv03/added_IVF1379_Flat_nprobe_1_cv03_v2.index"
method = "rmvpe" #"harvest"

skip_infer = False
use_cpu = False

# TODO respece key

key1 = "cv018" # for filter
#key2 from parsed data name
key3 = "recitation"
key4 = "b16-32k"

input_audio_dir = "/notebooks/01_normal/"
rvc_audio_dir = "/notebooks/rvc_out"
output_dir = "/notebooks/jyakoTen/"
# remove old audios
#"cv018_e15_s1110","cv018_e25_s1850","cv018_e5_s370","cv018_e20_s1480",
data_list =["cv018_e10_s740","cv018_e30_s2220"]
#data_list = ["cv017_e200_s11000"]
for data in data_list:
    if data.endswith(".pth"):
        data = data[0:-4]
# create rvc file
    if not skip_infer:
        batch_rvc.process_batch_infer(data,input_audio_dir,rvc_audio_dir,index,method,False) # no skip
    splited = data.split("_")
    key2 = splited[1]+splited[2]
   
    # whisper file
    batch_rvc.process_whisper(rvc_audio_dir,output_dir,key1,key2,key3,key4,use_cpu)
    file_dir = output_dir
    batch_rvc.jyako_ten(file_dir,key1,key2,key3,key4)
