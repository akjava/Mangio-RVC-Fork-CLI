import os

dir_path = "/notebooks/jyakoTen/"

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',"-i" , help='input dir' ,default = ".")
args = parser.parse_args()


def parse_jyakoten_score(file_name,splitext=False):
    if file_name.find("score") == -1:
        return None
    
    if splitext:
        file_name,ext = os.path.splitext(file_name)
    values = file_name.split("_")
    size = len(values)
    result_dic = {}
    for i in range(size):
        if i==3:
            
            if not  values[3].startswith("score(") or not  values[3].endswith(")"):
                print(f"invalid score text '{score_text}'")
                return None
            score_text =  values[3][6:-1]
            score,max_score = score_text.replace(" ","").split("of")
            #print(score)
            result_dic["score"]=score
            result_dic["max_score"]=max_score
            pass
        if i>3: # 3 must be score
            index = i
        else:
            index = i+1
            # try to parse epoch
            if i==1:
               
                if values[1].startswith("e"):
                    
                    epoch_texts = values[1].split("s") #e10s100
                    if len(epoch_texts) == 2:#success split
                        epoch = epoch_texts[0][1:]
                        result_dic["epoch"]=epoch
        
        
            
        
        if i!=3:
            result_dic["key"+str(index)] = values[i]
    return result_dic
    

files = os.listdir(os.path.join(dir_path,args.input))
dic_list = []
for file in files:
    file_name,ext = os.path.splitext(file)
    #print(ext)
    if ext == ".txt":
        dic=parse_jyakoten_score(file_name)
        if dic is not None:
            dic_list.append(dic)
    
sorted_data_list = sorted(dic_list, key=lambda x: int(x['epoch']))


epochs = []
scores = []
for dic in sorted_data_list:
    epochs.append(int(dic['epoch']))
    scores.append(float(dic['score']))
    #print(dic)
    template = f"| {dic['score']} | 0.107| faster-whisper | large-v3 | float32 |  10 | yes | Epoch {int(dic['epoch']):02d}  | 32khz batch04 rmvpe index無 | "
    #print(template)
    
print(f"epochs = {epochs}")
print(f"scores = {scores}")
        