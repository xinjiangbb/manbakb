# 如何运行
> 前提条件，自己电脑上安装的有python环境，如果没有，无法运行。
> 请安装 Python3.6+ 版本。

在命令行中运行
```shell
python run.py
```

*代码主要功能*
1. 支持Monkey 测试
2. 支持安装卸载测试

# 主要目录
```shell
logs              # 运行日志目录
  monkey_logs     # monkey 运行日志
  install_logs    # 安装卸载运行日志
apks              # 存放安装包
run.py            # 运行的主文件
```

# 使用说明
在执行安装卸载测试的时候，请务必将测试的apk文件修改文件名为 `app-release.apk`
然后才可以执行。

