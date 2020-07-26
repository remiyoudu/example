## slam和SFM（三维重建）调研

区别

SLAM是“Simultaneous Localization And Mapping”的缩写，可译为同步定位与建图。SLAM最早被被应用在机器人领域，其目标是在没有任何先验知识的情况下，根据传感器数据实时构建周围环境地图，同时根据这个地图推测自身的定位。只利用相机作为外部感知传感器的SLAM称为视觉SLAM (vSLAM )；经典vSLAM系统流程图如图所示；

![preview](https://pic4.zhimg.com/v2-0d87af326d4e6fca1e3259716185c2a4_r.jpg)

- 视觉里程计 (Visual Odometry)：仅有视觉输入的姿态估计；

-  后端优化 (Optimization): 后端接受不同时刻视觉里程计测量的相机位姿，以及闭环检测的信息，对它们进行优化，得到全局一致的轨迹和地图；

-  闭环检测 (Loop Closing): 指机器人在地图构建过程中, 通过视觉等传感器信息检测是否发生了轨迹闭环, 即判断自身是否进入历史同一地点;

- 建图 (Mapping): 根据估计的轨迹，建立与任务要求对应的地图。

### 现状

- SLAM现在没有很好的落地方案
- 国内工业界的现状：拿着开源代码跑了一下
- 

### 相关文献

高翔博士--[视觉SLAM漫谈 (三): 研究点介绍](https://www.cnblogs.com/gaoxiang12/p/4395446.html)

slam研究方案--[《快看，那个学SLAM 的崩溃了》](https://zhuanlan.zhihu.com/p/62336523)

- 

