import subprocess
import os

def process_batch_infer(key,input_dir,output_dir,index="None",method="rmvpe",skip_exist = False):
    #if rmdir:
        # ディレクトリ内のファイルを削除するコマンド
     #   pass
        #subprocess.run(["rm", "-rf", f"{output_dir}/*"], check=True)

    # Pythonスクリプトを実行するコマンド
    # cwd は /notebooks/Mangio-RVC-Fork-CLI/ 
    command = [
        "python", "infer_batch_rvc.py", "0", input_dir,
        index, method, output_dir,
        f"/notebooks/Mangio-RVC-Fork-CLI/weights/{key}.pth", "0.95", "cuda:0", "True", "3", "0", "1", "0.33",f"{skip_exist}"
    ]
    print(command)
    subprocess.run(command, check=True,cwd="/notebooks/Mangio-RVC-Fork-CLI/")

def list_weight_datas():
    result = []
    files = os.listdir("weights")
    keys = set()
    print("[pth list]")
    for file in files:
        file_name,ext = os.path.splitext(file)
        if file.endswith(".pth"):
            result.append(file_name)
            key = file.split("_")[0]
            keys.add(key)
    return result

def key_to_file(key1,key2,key3,key4=""):
    file=f"{key1}_{key2}_{key3}_result"
    if key4!="":
        file+="_"+key4
    return file+".txt"


    
def process_whisper(audio_dir,output_dir,key1,key2,key3,key4,use_cpu=False):
    whisper_dir = "/notebooks/whisper"

    output_path = os.path.join(output_dir,key_to_file(key1,key2,key3,key4))
    #output_path = key_to_file(key1,key2,key3,key4)
    command = [
        "python", "faster_whisper_batch.py", "--audio_txt", "ita04_recitation_audio_list.txt",
        "--audio_txt_dir", audio_dir, "--out",output_path
    ]
    if use_cpu:
        command.append("--cpu")
    print(command)
    subprocess.run(command, check=True,cwd=whisper_dir)
                            
def jyako_ten(file_dir,key1,key2,key3,key4):
    command = [
        "python","-m", "jyakoTen", "--key_dir", file_dir,
        "--key1",key1,"--key2",key2,"--key3",key3,"--key4",key4
    ]
    print(command)
    subprocess.run(command, check=True,cwd=file_dir)
                               
                               
    
