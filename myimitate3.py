import scipy.io as sio
import json
import pandas as pd
import customserializer
import os

img_json_path="C:\\Users\\Lsk\\Desktop\\RGB_N\\matlab\\提取坐标\\img_to_json\\" # 只用到这两个
fusion_path ="C:\\Users\\Lsk\\Desktop\\RGB_N\\matlab\\提取坐标\\myimitate\\"             # 只要到这两个
img_json_type=".json"
img_type="_rgb.png"
img_type2="_rgb.json"
mat_type="_mask.mat"
mat_path = "C:\\Users\\Lsk\\Desktop\\RGB_N\\matlab\\提取坐标\\coordinate\\"  # 连通域轮廓坐标数据文件路径，其中img_coordinate_3是mat文件，在MATLAB中生成的元胞数组
#img_coordinate = sio.loadmat(mat_path)  # 加载指定数据

def dict_shapes(points,label, fill_color=None, line_color=None):
         return {"points": points, "label":label,  "fill_color": fill_color, "line_color": line_color}
label="temper"

def dict_other_json(shapes,imagePath, imageData, fillColor=None, lineColor=None):

    return {"shapes": shapes,"imagePath": imagePath, "imageData": imageData, "fillColor": fillColor, "lineColor": lineColor }


imgpathDir = os.listdir(img_json_path)
print(imgpathDir)
for img in range(len(imgpathDir)):
    pathDir=imgpathDir[img][:-9]
    matpathDir=mat_path + pathDir + mat_type
    img_coordinate = sio.loadmat(matpathDir)

    ##"shapes"的编写
    def dict_shapes(points,label, fill_color=None, line_color=None):
        return {"points": points, "label":label,  "fill_color": fill_color, "line_color": line_color}
    label="temper"

    XY= img_coordinate["mid_arug"]
    shapes=[]
    for i in range(len(XY)):
        points=[]
        tem=[]
        X=XY[i][0][0][0]
        Y=XY[i][1][0][0]
        if (len(X))>2:
            for key in range(len(X)):
                tem.append(X[key][0])
                tem.append(Y[key][0])
                points.append(tem)
                tem =[]
            shapes.append(dict_shapes(points,label))
        ### "shapes"编写完毕

    ### "shapes"和imagedate信息合成
    # def dict_other_json(shapes,imagePath, imageData, fillColor=None, lineColor=None):
    #
    #     return {"shapes": shapes,"imagePath": imagePath, "imageData": imageData, "fillColor": fillColor, "lineColor": lineColor }
    #
    fillColor = [0, 0, 255, 128]
    lineColor = [0, 255, 0, 128]

    img_file = img_json_path +str(pathDir) +img_type2
    imageData = json.load(open(img_file))
    imagePath = str(img) + img_type

    data=dict_other_json(shapes,imagePath,imageData,fillColor,lineColor)
    json_file = fusion_path + str(img) + img_type2

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, default=customserializer.to_json)