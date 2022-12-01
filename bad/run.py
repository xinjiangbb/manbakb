import os

def get_logs_dir():
    """
    获取项目的logs目录的绝对路径
    :return:
    """
    # 文件的绝对路径
    abspath = os.path.abspath(__file__)
    # 文件的根目录
    root_dir = os.path.dirname(abspath)
    logs_dir = os.path.join(root_dir,'logs')
    # 如果不存在
    if not os.path.exists(logs_dir):
        os.mkdir(logs_dir)
    return logs_dir

def get_devices():
    # 定义空的list
    devices = []
    # 获取设备串号 执行命令 adb devices 将打印输出的内容放到文件中
    os.system('adb devices > devices.txt')
    # 从 devices.txt 文件中获取内容
    with open('./devices.txt',mode='r',encoding='utf8') as file:
        # 获取到多行内容，数据类型为list ['List of devices attached\n', '127.0.0.1:62001\tdevice\n', '127.0.0.1:62025\tdevice\n', '127.0.0.1:62026\tdevice\n', '\n']
        lines = file.readlines()
        # 循环list
        for line in lines:
            # 拿到每一行内容，经过大量观察分析， 如果字符串中包含  \tdevice 字符串说明 里面含有 device的设备串号
            if "\tdevice" in line:
                # print(line, type(line)) # 127.0.0.1:62001	device
                # 从字符串中提取 127.0.0.1:62001
                # 1. 先将 \tdevice\n 替换为空字符串 ""
                device_id = line.replace("\tdevice\n","")
                # print(f'处理之后的设备串号：{device_id}')
                # 将处理之后的设备串号 存到 devices 列表
                devices.append(device_id)

        # 将获取到的所有的devices信息返回出去，
        return devices



# device,package_name,count 不同参数 设置count的默认值为1000
def run_monkey(device,package_name,count=1000):
    # 创建monkey的日志目录
    logs_dir = get_logs_dir()
    monkey_dir = os.path.join(logs_dir,'monkey_log')
    # 如果不存在monkey日志目录
    if not os.path.exists(monkey_dir):
        # 创建monkey目录
        os.mkdir(monkey_dir)
    #针对不同的设备串号 生成对应文件名
    device_file = device.replace(":","_")
    # 生成日志文件的路径，日志文件放在monkey 日志文件夹下
    log_file = os.path.join(monkey_dir,f'{device_file}.log')
    monkey_cmd = f'adb -s {device} shell monkey -p {package_name} -vv {count} > {log_file}'
    os.system(monkey_cmd)
    print(f'运行设备{device}完毕，生成对应日志文件{log_file}')

def run_install(device,package_name):
    """
    运行安装卸载测试
    1. 先把原来安装好的包卸载
    2. 安装apk
    :param device: 设备串号
    :param package_name:  包名
    :return:
    """
    # 创建安装卸载的日志目录
    logs_dir = get_logs_dir()
    # 定义安装卸载日志目录
    install_dir = os.path.join(logs_dir,'install_log')
    # 创建目录
    if not  os.path.exists(install_dir):
        os.mkdir(install_dir)
    # 定义日志文件名
    device_id = device.replace(":","_")
    # 安装日志
    install_log_path = os.path.join(install_dir,f'{device_id}_install.log')
    # 卸载日志
    uninstall_log_path = os.path.join(install_dir,f'{device_id}_uninstall.log')
    uninstall_cmd = f"adb -s {device} shell pm uninstall {package_name} > {uninstall_log_path}"
    # 执行卸载命令
    os.system(uninstall_cmd)
    print(f"卸载完成，生成对应的日志文件：{uninstall_log_path}")
    apkfile = os.path.join(os.path.abspath(__file__),'../apks/app-release.apk')
    # 执行安装命令
    install_cmd=f'adb -s {device} install {apkfile} > {install_log_path}'
    os.system(install_cmd)
    print(f"安装完成，生成对应的日志文件：{install_log_path}")
# 因为 get_devices() 函数有返回值， devices_list 的就是 函数返回的值
# 1. 获取所有的设备
devices_list = get_devices()

option = input('支持如下自动化测试：\n1.执行monkey测试\n2.安装卸载测试\n请选择测试类型[1,2]：')
if option == "1":
    package = input("请输入运行包名:")
    count = input("请输入运行次数（按下Enter 使用默认值1000）：")

    for device in devices_list:
        if count=="":
            run_monkey(device,package)
        else:
            run_monkey(device,package,count)
elif option == "2":
    package = input("请输入运行包名:")
    for device in devices_list:
        run_install(device,package)
else:
    print('输入参数有误。拜拜！')


