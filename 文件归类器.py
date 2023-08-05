import os
import shutil
print("文件归类器v1.0， by 优酱")
print("主要功能：在当前目录下按照文件扩展名将文件归类到相应的子文件夹中")

input("请按任意键继续")

current_dir = os.getcwd()
print(f"当前工作目录是{current_dir}")
choice_dir = input("请问你是否需要更改工作目录？\n如果想要保持当前目录，请输入“keepit”。\n否则，请在下面的步骤中输入新的目标工作目录")
if choice_dir == "keepit":
    print("好的，已保持当前工作目录")
else:
    new_dir = input("请输入新的工作目录")
    os.chdir(new_dir)
    current_dir = new_dir
    print(f"已更改，当前工作目录是{current_dir}")

input("请按任意键继续")

for filename in os.listdir(current_dir):
    current_file = os.path.join(current_dir, filename)

    if os.path.isfile(current_file):
        file_extension_name = os.path.splitext(filename)[1] #[1]是元组2

        target_folder = os.path.join(current_dir, file_extension_name.lstrip("."))

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        target_file = os.path.join(target_folder, filename)

        shutil.move(current_file, target_file)

input("文件归类完成，请按任意键退出")