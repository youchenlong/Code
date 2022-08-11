"智慧考勤系统"

app-->
程序入口

db_config-->
配置信息

handler-->
路由
company--与公司相关的路由，包括公司创建，员工申请
employeeManage--与员工管理相关的路由，包括员工列表，员工信息，审批，职位修改，邀请员工，删除员工
faceID--与人脸识别相关的路由，包括人脸信息录入，打卡，跳转到注册页面
identify--与检验相关的路由，包括登录，注册
infoFind--与信息查询相关的路由，包括个人信息查询，考勤信息查询

api-->
业务逻辑
company_api--与公司相关的业务逻辑，包括公司创建，员工申请
employeeManage_api--与员工管理相关的业务逻辑，包括员工列表，员工信息，审批，职位修改，邀请员工，删除员工
faceID_api--与人脸识别相关的业务逻辑，包括人脸信息录入，打卡，跳转到注册页面
identify_api--与检验相关的业务逻辑，包括登录，注册
infoFind_api--与信息查询相关的业务逻辑，包括个人信息查询，考勤信息查询

operation-->
数据库操作
clockin_operation--打卡列表的操作
companyCreate_operation--公司创建列表的操作
companyList_operation--公司列表的操作
employeeApplication_operation--员工申请列表的操作
employeeDelete_operation--员工删除列表的操作
HRInvitation_operation--邀请新员工列表的操作
userList_operation--用户列表的操作

models-->
存放库表
clockin--打卡列表
companyCreate--公司创建列表
companyList--公司列表
employeeApplication--员工申请列表
employeeDelete--员工删除列表
HRInvitation--邀请新员工列表
userList--用户列表

utils-->
其他功能实现
data_process--将数据库操作查询的结果从类转换为列表
sql--操作其他数据库

