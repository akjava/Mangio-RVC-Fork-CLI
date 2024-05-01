import subprocess


def process_batch_infer(input_dir,output_dir,rmdir=True,method="rmvpe",index="None"):

if rmdir:
    # ディレクトリ内のファイルを削除するコマンド
    subprocess.run(["rm", "-rf", f"{output_dir}/*"], check=True)

# Pythonスクリプトを実行するコマンド
# ここでは、変数を使用してコマンドを構築します。
# この例では、変数keyが定義されている必要があります。
key = "your_key_here" # ここで適切なキーを設定してください。
command = [
    "python", "infer_batch_rvc.py", "0", "/notebooks/01_normal/",
    index, method, "/notebooks/rvc_out",
    f"/notebooks/Mangio-RVC-Fork-CLI/weights/{key}.pth", "0.95", "cuda:0", "True", "3", "0", "1", "0.33"
]
subprocess.run(command, check=True)
