# 导入 Pillow 库中的 Image 模块，以及用于处理路径的 os 模块
from PIL import Image
import os

# 1. 定义图片的完整路径
#    使用 r"..." (原始字符串) 是处理 Windows 路径的好方法，
#    它可以防止反斜杠 \被误解为转义字符。
image_path = r"D:\alien_invasion\images\monkey.bmp"

# 2. 检查文件是否存在
if not os.path.exists(image_path):
    print(f"错误：文件未找到，请检查路径是否正确: {image_path}")
else:
    try:
        # 3. 打开图片文件
        with Image.open(image_path) as img:
            # 获取并打印原始尺寸
            original_width, original_height = img.size
            print(f"成功打开图片: {os.path.basename(image_path)}")
            print(f"原始分辨率: {original_width} x {original_height}")

            # 4. 计算新的分辨率 (原始尺寸的一半)
            # 使用整数除法 // 来确保结果为整数
            new_width = original_width // 2
            new_height = original_height // 2
            print(f"目标分辨率: {new_width} x {new_height}")

            # 5. 调整图片尺寸
            # Image.LANCZOS 是一个高质量的缩小算法，能让图片更清晰
            resized_img = img.resize((new_width, new_height), resample=Image.LANCZOS)

            # 6. 准备新的文件名和保存路径
            # 我们将在原始文件名后添加 "_resized"
            # 首先，分离路径、主文件名和扩展名
            dir_name = os.path.dirname(image_path)
            file_name, file_ext = os.path.splitext(os.path.basename(image_path))

            # 创建新的文件名
            new_file_name = f"{file_name}_resized{file_ext}"

            # 组合成完整的保存路径
            save_path = os.path.join(dir_name, new_file_name)

            # 7. 保存调整后的新图片
            resized_img.save(save_path)

            print("-" * 30)
            print(f"图片处理完成！\n新图片已保存至: {save_path}")

    except Exception as e:
        print(f"处理图片时发生了一个错误: {e}")