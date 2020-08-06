[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=nondevops)](https://github.com/anuraghazra/github-readme-stats)


# n9e-collector-plugins 常用插件监控脚本集合(持续更新中)
夜莺监控采集脚本插件集合,源open-falcon插件请访问https://github.com/nondevops/open-falcon-plugins

## 该仓库的产生背景

``` text
open-falcon监控难运维，n9e易运维，但些许插件可能不兼容，为了保证不影响open-falcon-plugins仓库的质量，特创建此仓库存储
```

## 监控说明

``` text
如果系统环境不是ip作为唯一对象，请修改相应插件的获取方式；
该仓库的插件与gitlab统一自动更新到客户机；
```

## 插件介绍

``` bash
cachecloud # cachecloud 监控,soho开源的redis管理平台
ceph # ceph 监控
cert # 证书过期 监控
domain # 域名过期 监控
es # es 监控
hadoop # hadoop 监控
haproxy # haproxy 监控
hardware # hardware 监控
lvs # lvs 监控
memcached # memcached 监控
mongodb # mongodb 监控
nginx # nginx 监控
powerdns # powerdns 监控
public-cloud # 公有云 监控,如ELB数据
rabbitmq # rabbitmq 监控
redis # redis 监控
solr # solr 监控
squid # squid 监控
sys # 系统级 监控
zookeeper # zookeeper 监控
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
如对脚本或插件有疑问或有错误,欢迎提PR,大家共同维护
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
