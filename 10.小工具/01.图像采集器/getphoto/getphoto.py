import cv2
import numpy as np
from flask import Flask, render_template, Response
import threading
from datetime import datetime
import os

# 创建目录来保存照片
if not os.path.exists('photos'):
    os.makedirs('photos')

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 初始化Flask应用
app = Flask(__name__)

# 存储最新帧的变量
latest_frame = None
frame_lock = threading.Lock()

def gen_frames():
    """生成视频流帧"""
    while cap.isOpened():
        with frame_lock:
            # 从摄像头读取帧
            success, frame = cap.read()
            if not success:
                break
                
            # 将帧存储为最新帧
            latest_frame = frame.copy()
            
            # 换为JPEG格式
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # 生成MJPEG流格式
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """视频流路由"""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/take_photo')
def take_photo():
    """拍照路由"""
    with frame_lock:
        if latest_frame is not None:
            # 保存照片
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"photos/photo_{timestamp}.jpg"
            cv2.imwrite(filename, latest_frame)
            return f"照片已保存: {filename}"
        return "无法获取图像"

def run_flask_app():
    """运行Flask应用"""
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    # 启动Flask应用
    threading.Thread(target=run_flask_app).start()
    
    print("请在浏览器中访问 http://localhost:5000")
    
    # 按q键拍照
    while True:
        with frame_lock:
            ret, frame = cap.read()
            if not ret:
                break           
                
 # 显示摄像头图像
            cv2.imshow('按Q键拍照', frame)
            
            # 按Q键保存照片
            if cv2.waitKey(1) == ord('q'):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"photos/photo_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"照片已保存: {filename}")
    
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()