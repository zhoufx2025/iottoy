from PIL import Image
import os
import pillow_heif

def heic_to_jpg(input_folder, output_folder):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为 HEIC 格式
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename[:-5] + ".jpg")
            
            # 打开 HEIC 文件
            heif_file = pillow_heif.read_heif(input_path)
            # 将 HEIC 文件转换为 Pillow 图像对象
            img = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            # 保存为 JPEG 文件
            img.save(output_path, "JPEG")
            print(f"Converted {filename} to {os.path.basename(output_path)}")

if __name__ == "__main__":
    # 指定输入文件夹和输出文件夹路径
    input_folder = "/path/to/in"  # 替换为你的 HEIC 文件夹路径
    output_folder = "/path/to/out"  # 替换为保存 JPEG 文件的文件夹路径
    
    heic_to_jpg(input_folder, output_folder)
    print("Conversion completed!")