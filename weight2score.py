import batch_rvc

index = "None"
#index = "logs/cv03/added_IVF1379_Flat_nprobe_1_cv03_v2.index"
method = "rmvpe" #"harvest"

skip_infer = False
use_cpu = False

# TODO respece key

key1 = "cv016" # for filter
#key2 from parsed data name
key3 = "recitation"
key4 = "b16-32k"

input_audio_dir = "/notebooks/01_normal/"
rvc_audio_dir = "/notebooks/rvc_out"
output_dir = "/notebooks/jyakoTen/"
# remove old audios

#data_list =["cv03_e20_s2000","cv03_e25_s2500","cv03_e30_s3000"]
data_list =["cv03_e20_s540.pth"]
data_list =["cv015_e10_s220","cv015_e50_s1100","cv015_e20_s440","cv015_e30_s660","cv015_e40_s880","cv015_e25_s550","cv015_e45_s990","cv015_e15_s330","cv015_e5_s110","cv015_e35_s770"]

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
