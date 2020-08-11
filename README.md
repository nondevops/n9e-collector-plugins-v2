[![Jeff's github stats](https://github-readme-stats.vercel.app/api?username=nondevops&show_icons=true&theme=dark&layout=compact)](https://github.com/nondevops/n9e-collector-plugins)

# n9e-collector-plugins 常用插件监控脚本集合(持续更新中且不收取任何咨询答疑费用)
夜莺监控采集脚本插件集合,源open-falcon插件请访问https://github.com/nondevops/open-falcon-plugins

## 该仓库的产生背景

``` text
open-falcon监控难运维，n9e易运维，但些许插件可能不兼容，为了保证不影响open-falcon-plugins仓库的质量，特创建此仓库存储
```

## 监控说明

``` text
1.如果系统环境不是`hostname-ip`格式作为唯一endpoint对象，请修改相应插件的获取方式；

为什么要使用`hostname-ip`格式作为唯一endpoint对象? 原因为ip无法第一时间识别是什么业务的实例，加上历史遗留原因ip可能会被复用或者存在ip段管理混乱现象，ip作为唯一标识无法满足运维需求，故增加hostname-ip为唯一对象。

为什么不使用`hostname`作为唯一endpoint对象?原因为历史遗留问题，没有结合业务标准化孵化实例，导致虚拟机为默认的localhost,不具有识别性；

2.该仓库的插件与gitlab统一自动更新到客户机；

3.获取`hostname-ip`格式的命令可能写的比较简陋，没有多方面测试，不符合业务需求的请自行修改或提交PR；
```

## 插件介绍

``` bash
├── cert
│   └── 600_cert_expire_time.sh
├── self-plugins
│   └── 60_plugin_status.py
└── sys
    ├── connections
    │   └── tcp
    │       └── 10_ss.sh
    ├── ntp
    │   ├── 600_ntp_monitor.py
    │   └── bak-600_ntp_monitor.py
    ├── ping
    │   ├── 60_ping_loss.sh
    │   ├── 60_pings.sh
    │   └── ping_172.26.45.178.tmp
    ├── uptime
    │   └── 60_uptime.sh
    └── user-login
        └── 10_user_logged.py

.....(脚本太多了直接clone下来慢慢看吧)


```

## 克隆代码

``` bash
git clone https://github.com/nondevops/n9e-collector-plugins.git
```

## 提交修改配置

``` text
由于ansible配置是通过gitlab仓库管理, 需提交修改然后分发到相应的虚拟机才能生效,如未这样使用,请忽略此步骤
```

## 启用插件

``` text
在n9e管理端对相应目录树节点添加插件
```

## 检验数据上报情况

``` text
检查是否上报数据, 在“监控看图”搜索该机器,如过滤 nginx.conf 信息,如有数据,则表示采集上报成功
```

## 告警策略配置

``` text
根据自身的监控指标来设置
```
## 意见和交流
```
如对脚本或插件有疑问或有错误,欢迎提PR或者ISSUE,大家共同维护..
如1天之内未回复，请在我的主页或者博客某篇文章的微信二维码扫描添加我为好友进行问题沟通；
```

## 注意
```
如使用脚本产生了生产环境故障,作者不负任何责任,请在测试环境充分测试后上线.有些场景可能脚本没有考虑到,请多理解
特别说明一下,请尊重劳动成果,希望广大用户不喜勿喷...
```

## 欢迎访问我的博客

``` bash
获得更多的技术体验
https://www.cqops.club
```
