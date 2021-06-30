#! /bin/bash

#启动某个集群的worker

trap "exit 1" TERM
export TOP_PID=$$

echoerr() { echo "$@" 1>&2; }

if [[ -f "/etc/profile" ]]; then
    source /etc/profile
fi

workdir=$( cd $(dirname $0) && pwd )


get_property_with_default()
{
    local ret=$(cat "$cluster_conf_path" | grep "$1=" | awk -F '=' '{print $2}')
    if [[ -z "$ret" ]]; then
        echo $2
    else
        echo $ret
    fi
}

get_property()
{
    local ret=$(cat "$cluster_conf_path" | grep "$1=" | awk -F '=' '{print $2}')
    if [[ -z "$ret" ]]; then
        echoerr "Missing $1"
        kill -s TERM $TOP_PID
    fi
    echo $ret
}


cluster_name=$1
if [[ -z "$cluster_name" ]]; then
    echo "Missing cluster name"
    exit 1
fi

cluster_conf_path="$workdir/../conf/${cluster_name}.cluster.properties"
echo "cluster name: $cluster_name"
if [[ ! -f $cluster_conf_path ]]; then
    echo "Can not find configuration of cluster $cluster_name"
    exit 1
fi


# Which java to use
if [ -z "$JAVA_HOME" ]; then
  JAVA="java"
else
  JAVA="$JAVA_HOME/bin/java"
fi

#CLASSPATH
##jar包路径
if [ -d "$workdir/../lib/" ]; then
        CLASSPATH=$CLASSPATH:$workdir/../lib/*
else
    echo "Missing lib directory"
    exit 1
fi

#-- END CLASSPATH

# 以mysql的jar包为准检查用户是否补充敏感协议包
if [ ! -f $workdir/../lib/common/mysql-connector-java-5.1.38.jar ]; then
    echo "Missing mysql package"
    exit 1
fi

# 创建日志文件目录
log_dir=$workdir/../logs/supervisor
mkdir -p $log_dir

# 启动集群参数
init_memory_size=$(get_property_with_default "deploy.cluster.memory.init" "256M")
max_memory_size=$(get_property_with_default "deploy.cluster.memory.max" "2G")
max_direct_memory_size=$(get_property_with_default "deploy.cluster.memory.direct.max" "1024M")

export KAFKA_HEAP_OPTS="-Xmx${max_memory_size} -Xms${init_memory_size} -Xss512k"
export KAFKA_JVM_PERFORMANCE_OPTS="-server -XX:+UseG1GC -XX:+PrintGCDetails -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:MaxDirectMemorySize=${max_direct_memory_size} -XX:+HeapDumpOnOutOfMemoryError -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSize=128K -Xloggc:${log_dir}/${cluster_name}_gc.log -Djava.awt.headless=true"
export KAFKA_LOG4J_OPTS="-Dlog4j.configuration=file:$workdir/../conf/log4j.properties -Ddatabus.logdir=$log_dir -Ddatabus.clustername=$cluster_name"

### 设置语言、时区等环境变量 ###
export TZ_OPTS="-Ddatabus.display.timezone=__GMT_TIME_ZONE__"
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"

# 记录集群启动参数
echo $JAVA $KAFKA_HEAP_OPTS $KAFKA_JVM_PERFORMANCE_OPTS $KAFKA_LOG4J_OPTS $TZ_OPTS -cp $CLASSPATH com.tencent.bk.base.datahub.databus.connect.common.cli.BkDataDatabusShipper "$cluster_conf_path"
exec $JAVA $KAFKA_HEAP_OPTS $KAFKA_JVM_PERFORMANCE_OPTS $KAFKA_LOG4J_OPTS $TZ_OPTS -cp $CLASSPATH com.tencent.bk.base.datahub.databus.connect.common.cli.BkDataDatabusShipper "$cluster_conf_path"

