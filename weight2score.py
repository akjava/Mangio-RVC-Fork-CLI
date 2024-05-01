import batch_rvc

index = "None"
#index = "logs/cv03/added_IVF1379_Flat_nprobe_1_cv03_v2.index"
method = "rmvpe" #"harvest"

key1 = "cv03" # for filter
#key2 from parsed data name
key3 = "recitation"
key4 = "b04-32k"

input_audio_dir = "/notebooks/01_normal/"
rvc_audio_dir = "/notebooks/rvc_out"
output_dir = "/notebooks/jyakoTen/"
# remove old audios

data_list =["cv03_e5_s500","cv03_e10_s1000","cv03_e15_s1500"]

for data in data_list:
# create rvc file
    batch_rvc.process_batch_infer(data,input_audio_dir,rvc_audio_dir,index,method,False) # no skip
    splited = data.split("_")
    key2 = splited[1]+splited[2]
   
    # whisper file
    batch_rvc.process_whisper(rvc_audio_dir,output_dir,key1,key2,key3,key4)
    file_dir = output_dir
    batch_rvc.jyako_ten(file_dir,key1,key2,key3,key4)
