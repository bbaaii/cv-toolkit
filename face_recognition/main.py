#coding=utf-8
#图片人脸检测
import cv2
import datetime
import time

filepath = "img/xingye-2.png"
# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "C:\face\train\trained_models\detection_models\haarcascade_frontalface_default.xml"
)



img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
color = (0, 255, 0)  # 定义绘制颜色

faces = face_classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(140, 140))
	
#加载出训练好的性别模型
gender_classifier = load_model(
    "trained_models/gender_models/simple_CNN.81-0.96.hdf5")
gender_labels = {0: '女', 1: '男'}
color = (0, 255,0)

# 调用识别人脸
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
	
def predict (faceRects):	

	if len(faceRects):  # 大于0则检测到人脸
		for faceRect in faceRects:  # 单独框出每一张人脸
	
			x, y, w, h = faceRect   #返回人脸所对应的位置
		
			# 框出人脸
			cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
		
			#根据人脸的位置计算出眼睛及嘴巴的对应位置，并且用
		
			# 左眼
			cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
			#右眼
			cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
			#嘴巴
			cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)
			cv2.imshow("image", img)  # 显示图像
			cv2.waitKey(0)
			cv2.destroyAllWindows()

def gender (faces):					  
					  
#识别出人脸，标出性别
	for (x, y, w, h) in faces:
	
		face = img[(y - 60):(y + h + 60), (x - 30):(x + w + 30)]
		face = cv2.resize(face, (48, 48))
		face = np.expand_dims(face, 0)
		face = face / 255.0
		gender_label_arg = np.argmax(gender_classifier.predict(face))

		cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        return gender_label_arg
					  

		cv2.imshow("image", img)  # 显示图像
		cv2.waitKey(0)
		cv2.destroyAllWindows()

