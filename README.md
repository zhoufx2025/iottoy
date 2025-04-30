# 物联网小玩具（2025.4.30）

## 更新履历（2025.4.30）
| 序号 | 时间       | 内容                     |
| ---- | ---------- | ------------------------ |
| 1    | 2025/4/30  | 新规作成：想法、大纲、组成 |
| 2    |            |                          |
| 3    |            |                          |

## 想法（2025.4.30）
| 序号 | 内容         | 目标                                                                 |
| ---- | ------------ | -------------------------------------------------------------------- |
| 1    | 自动抓取小车 | 1. 玩具的自动识别（先实现玩具大类）<br>2. 自动夹取、取放到指定位置<br>3. 接入Homekit智能中枢，进行语音操控<br>4. 实现杂乱玩具自动整理归类操作 |
| 1.1  | 平板车       |                                                                     |
| 1.2  | 自动抓手     |                                                                     |
| 1.3  | 相机系统     |                                                                     |
| 1.4  | 控制协调系统 |                                                                     |

***
# 1.自动抓取小车（2025.4.30）

## 大纲（2025.4.30）
  利用树莓派当作控制中枢，同时安装了homeassistant，上接互动设备，下接驱动设备。
<img src="https://raw.githubusercontent.com/zhoufx2025/iottoy/raw/main/blob/main/img/1_outline.jpg"  width="500" alt="大纲">

## 硬件组成
### 组成结构及挑选（2025.4.30）ps：兼容性未知还在研究试错中，不断更新
<img src="https://github.com/zhoufx2025/iottoy/raw/main/blob/main/img/1_hardware.jpg"  height="500" alt="硬件组成结构"><img src="https://github.com/zhoufx2025/iottoy/raw/main/blob/main/img/1_hardware_select.png"  height="500" alt="硬件挑选">


## 软件组成
