# 01.图像采集器
## 1.getphoto.py
-- 可以通过web进行相机图像采集，并且保存到文件夹中


# 02.图片预处理、训练及分类
## 1.change.py
-- 可以将苹果HEIC图片转换成JPEG格式
## 2.
-- JPEG文件重命名成（1-n.jpeg），方便标定。
## 3.labelImg 
-- 这里我选择的YOLO格式，做图片标定，会生成对应的标签文件。
可以参考sample文件夹
# 4.
-- dataset生成器：自动生成YOLO训练用的内容（train,val文件夹）
# 5.
-- 模型训练
会生成best.pt 最优模型
