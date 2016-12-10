#formal_checker
trying的作用：
检查数据格式是否正确。以下为格式要求。
1.顶层目录下允许并且只允许存在三个目录：  annotation、doc、speech  并且这三个目录的名字是固定的
2.annotation 目录下只允许存在一个（只能是一个）txt文件，文件的文件名必须和顶层目录的名字一致
3.speech 目录下只允许存在后缀为  .wav 的文件（至少有一个wav文件）
4.doc 目录下的文件不做限制，可以存放任意文件
5.顶层目录下除了上述的3个目录外，
  a)必须存在一个 desc 后缀的文件，文件名必须和顶层目录的名字一致；
  b)必须存在一个 info 后缀的文件，文件名必须和顶层目录的名字一致；
  
使用方法：
python trying.py
输入adress:（顶层目录路径）

输出：
对格式错误的信息进行提示