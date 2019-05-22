"""
    day14 复习
    包:
        导入方式
        from 包名.模块名 import 成员  ---> 使用:成员
        from 包 import 模块 ---> 使用:模块.成员
        import 包名.模块名 --> 使用:包名.模块名
        备注:所有路径,从项目根目录开始算起.

    异常处理:
        异常:运行时遇到的错误.程序返回调用端.
        处理:将异常状态变为正常状态.
        自行抛出异常:raise 异常对象     xxxError(参数)
        自定义异常:封装错误信息
            定义:class  XXXError(Exception):
                    def __init__(self,参数):
                        self.成员变量 = ?
            抛出异常:
                raise XXXError(参数)
            处理:
            try:
                .....
            except XXXError as 变量:
                变量.成员
"""












