# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础平台 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-BASE 蓝鲸基础平台 is licensed under the MIT License.

License for BK-BASE 蓝鲸基础平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# 定义一些常用的字符串常量
# 存储类型
MYSQL = "mysql"
ES = "es"
HDFS = "hdfs"
CLICKHOUSE = "clickhouse"
TSPIDER = "tspider"
DRUID = "druid"
HERMES = "hermes"
TSDB = "tsdb"
TREDIS = "tredis"
QUEUE = "queue"
IGNITE = "ignite"
TCAPLUS = "tcaplus"
TDW = "tdw"
POSTGRESQL = "postgresql"
TPG = "tpg"
TDBANK = "tdbank"
QUEUE_PULSAR = "queue_pulsar"
ICEBERG = "iceberg"
KAFKA = "kafka"
PULSAR = "pulsar"
PRESTO = "presto"
TDBANK_TDW = "tdbank_tdw"

NODES = "nodes"

# cc配置
BK_CLOUD_ID = "bk_cloud_id"
NODE_TYPE = "node_type"
SCOPE = "scope"
HOST_SCOPE = "host_scope"
MODULE_SCOPE = "module_scope"

# 平台模块常用常量
DATAHUB = "datahub"
DATAMANAGE = "datamanage"
DATAQUERY = "dataquery"
JOBNAVI = "jobnavi"

META = "meta"
ID = "id"
RESULT_TABLE_ID = "result_table_id"
RESULT_TABLE_NAME = "result_table_name"
RESULT_TABLE_NAME_ALIAS = "result_table_name_alias"
CLUSTER_NAME = "cluster_name"
CLUSTER_TYPE = "cluster_type"
CLUSTER_TYPE_JAVA = "clusterType"
CLUSTER_GROUP = "cluster_group"
CLUSTER_DOMAIN = "cluster_domain"
CLUSTER_PORT = "cluster_port"
ZK_DOMAIN = "zk_domain"
ZK_PORT = "zk_port"
CLUSTER_KAFKA_DEFAULT_PORT = 9092
CLUSTER_ZK_DEFAULT_PORT = 2181
APP_CODE = "app_code"
BK_BIZ_ID = "bk_biz_id"
BK_BIZ_NAME = "bk_biz_name"
BK_BIZ_ID_BKDATA = 591
BK_BIZ_NAME_BKDATA = "bkdata"
BK_BKDATA_NAME = "tgdp"
BK_USERNAME = "bk_username"
BK_APP_CODE = "bk_app_code"
BK_APP_SECRET = "bk_app_secret"
BKDATA_AUTHENTICATION_METHOD = "bkdata_authentication_method"
REFRESH_TOKEN = "refresh_token"
ACCESS_TOKEN = "access_token"
ENV_NAME = "env_name"
GRANT_TYPE = "grant_type"
STORAGES = "storages"
STORAGE_CONFIG = "storage_config"
STORAGE_KEYS = "storage_keys"

# kv 存储配置
STORAGE_VALUES = "storage_values"
STORAGE_SEPARATOR = "storage_separator"
STORAGE_KEY_SEPARATOR = "storage_key_separator"
STORAGE_KEY_PREFIX = "storage_key_prefix"
SCENARIO_TYPE = "scenario_type"
PRIMARY_KEYS = "primary_keys"
STORAGE_TYPE = "storage_type"
DATA_TYPE = "data_type"
TYPE = "type"
PERIOD = "period"
PARQUET = "parquet"
BKDATA = "bkdata"
DEFAULT = "default"
JSON = "json"

# 连接信息
CONNECTION_INFO = "connection_info"
CONNECTION = "connection"
CONNECTION_URL = "connectionUrl"
CONNECTION_USER = "connectionUser"
CONNECTION_PASSWORD = "connectionPassword"

# 物理表
PHYSICAL_TABLE_NAME = "physical_table_name"

# 过期配置
EXPIRES = "expires"
EXPIRE = "expire"
EXPIRE_DAYS = "expire_days"
MIN_EXPIRE = "min_expire"
MAX_EXPIRE = "max_expire"
LIST_EXPIRE = "list_expire"

# 任务配置
DELTA_DAY = "delta_day"
MERGE_DAYS = "merge_days"
TIMEOUT = "timeout"
TASK_TYPE = "task_type"
TASK_ID = "task_id"
STORAGE_CLUSTER = "storage_cluster"
CHANNEL_CLUSTER = "channel_cluster"

# tag 相关配置
RESULT_TABLE = "result_table"
CLUSTER_ROLE = "cluster_role"
GEOG_AREA = "geog_area"
GEOG_AREAS = "geog_areas"
GEOG_AREA_ALIAS = "geog_area_alias"
GEOG_AREA_CODE = "geog_area_code"
MAINLAND = "mainland"
INLAND = "inland"
OVERSEAS = "overseas"
TAGS = "tags"

# 存储常用配置常量
CAPACITY = "capacity"
DATABASE = "database"
TIME = "time"
DATA = "data"
NAME = "name"
PRIORITY = "priority"
VERSION = "version"
BELONGS_TO = "belongs_to"
DESCRIPTION = "description"
ZOOKEEPER_CONNECT = "zookeeper.connect"
STATUS = "status"
LOCATION = "location"
INFO = "info"
INDEX = "index"
INDEX_FIELDS = "index_fields"
INDICES = "indices"
MAPPINGS = "mappings"
SETTINGS = "settings"
SAMPLE = "sample"
FIELDS = "fields"
FIELD_NAME = "field_name"
FIELD_TYPE = "field_type"
REPORT_MODE = "report_mode"
ACTIONS = "actions"
ACTION = "action"
ENABLE = "enable"
DISABLE = "disable"
OK = "OK"
ALIAS = "alias"
ADD = "add"
REMOVE = "remove"
ANALYZED_FIELDS = "analyzed_fields"
DATE_FIELDS = "date_fields"
DOC_VALUES_FIELDS = "doc_values_fields"
JSON_FIELDS = "json_fields"
DOC_VALUES = "doc_values"
PROPERTIES = "properties"
ENABLE_REPLICA = "enable_replica"
HAS_REPLICA = "has_replica"
INCLUDE_IN_ALL = "include_in_all"
ROUTING = "routing"
ALLOCATION = "allocation"
INCLUDE = "include"
TAG = "tag"
NUMBER_OF_REPLICAS = "number_of_replicas"
FALSE = "false"
TRUE = "true"
TABLE = "table"
COLUMN = "column"
COLUMNS = "columns"
VALUE = "value"
PARTITIONS = "partitions"
TODAY_DIRS = "today_dirs"
LATEST_FILES = "latest_files"
MODIFY_TIME = "modify_time"
HDFS_URL = "hdfs_url"
DELETE_PATHS = "delete_paths"
PATH = "path"
LENGTH = "length"
ADD_SQL = "add_sql"
EXIST_SQL = "exist_sql"
DROP_SQL = "drop_sql"
WITH_DATA = "with_data"
WITH_HIVE_META = "with_hive_meta"
RT_FIELDS = "rt_fields"
MYSQL_FIELDS = "mysql_fields"
CHECK_RESULT = "check_result"
CHECK_DIFF = "check_diff"
APPEND_FIELDS = "append_fields"
DELETE_FIELDS = "delete_fields"
BAD_FIELDS = "bad_fields"
INDEXED_FIELDS = "indexed_fields"
SCHEMA = "schema"
DB_NAME = "db_name"
TABLE_NAME = "table_name"
EXTRA = "extra"
PLATFORM = "platform"
IS_MANAGED = "is_managed"
MANAGE = "manage"
STORAGE_CHANNEL_ID = "storage_channel_id"
STORAGE_CHANNEL = "storage_channel"
GENERATE_TYPE = "generate_type"
ACTIVE = "active"
PREVIOUS_CLUSTER_NAME = "previous_cluster_name"
CREATED_BY = "created_by"
CREATED_AT = "created_at"
UPDATED_BY = "updated_by"
UPDATED_AT = "updated_at"
SERIES = "series"
LIMIT = "limit"
START_DATE = "start_date"
END_DATE = "end_date"
START_TIME = "start_time"
END_TIME = "end_time"
START = "start"
END = "end"
PROJECT_ID = "project_id"
COMPONENT = "component"
BID = "bid"
CODE = "code"
MESSAGE = "message"
APP = "app"
DNS_PORT = "dns_port"
GCS_USER = "gcs_user"
GCS = "gcs"
DNS = "dns"
JOBID = "jobid"
EXPIRATION_TIME = "expiration_time"
SQL = "sql"
SYS_TYPE = "sys_type"
OPERATE_TYPE = "operate_type"
RELATED = "related"
PAGE = "page"
PAGE_SIZE = "page_size"
RELATED_FILTER = "related_filter"
ATTR_NAME = "attr_name"
ATTR_VALUE = "attr_value"
TDW_RELATED = "tdw_related"
COLS_INFO = "cols_info"
PARTS_INFO = "parts_info"
TDW_USERNAME = "tdw_username"
TDW_PASSWORD = "tdw_password"
RECEIVER = "receiver"
NOTIFY_WAY = "notify_way"
FIELD_ALIAS = "field_alias"
IS_DIMENSION = "is_dimension"
FIELD_INDEX = "field_index"
PHYSICAL_FIELD = "physical_field"
PHYSICAL_FIELD_TYPE = "physical_field_type"
IS_TIME = "is_time"
ORDER = "order"
COMPONENT_TYPE = "component_type"
SRC_CLUSTER_ID = "src_cluster_id"
DEST_CLUSTER_ID = "dest_cluster_id"
DEST = "dest"
SERVICE_TYPE = "service_type"
RESOURCE_TYPE = "resource_type"
UPDATE_TYPE = "update_type"
TB_NAME = "tb_name"
REPORT_DATE = "report_date"
DATA_SIZE = "data_size"
SIZE = "size"
REPORT_TIME = "report_time"
TABLE_SIZE_MB = "table_size_mb"
TABLE_RECORD_NUMS = "table_record_nums"
TABLES = "tables"
SIZE_MB = "size_mb"
ROW_NUMS = "row_nums"
RELATED_TAGS = "related_tags"
SEGMENTS = "segments"
DATASOURCE = "datasource"
INTERVAL = "interval"
DEFAULT_INTERVAL = 60000
MINTIME = "minTime"
COUNT = "count"
TASK = "task"
ES_CONF = "es_conf"
RT_CONF = "rt_conf"
ES_FIELDS = "es_fields"
AVRO = "avro"
OPERATOR_NAME = "operator_name"
STREAM_TO = "stream_to"
STREAM_TO_ID = "stream_to_id"
METADATA = "metadata"
OPERATION = "operation"
STORAGE_ADDRESS = "storage_address"
IP = "ip"
PORT = "port"
INNER = "inner"
OUTER = "outer"
RESULT = "result"
TCP_TGW = "tcp_tgw"
HTTP_TGW = "http_tgw"
INNER_CLUSTER = "inner_cluster"
ORDER_BY = "order_by"
PARTITION_BY = "partition_by"
SAMPLE_BY = "sample_by"
PLUGIN_NAME = "plugin_name"
PLUGIN_VERSION = "plugin_version"
PLUGIN_TEMPLTATES_NAME = "plugin_templates_name"
PLUGIN_TEMPLTATES_VERSION = "plugin_templates_version"
RT_ID = "rt.id"
RTID = "rtId"
ZOOKEEPER_ADDR = "zookeeper.addr"
BOOTSTRAP_SERVERS = "bootstrap.servers"
PULSAR_CHANNEL_TOKEN = "pulsar_channel_token"
BROKER_SERVICE_URL = "brokerServiceUrl"
EMPTY_STRING = ""
CHANNEL_ID = "channel_id"
CHANNEL = "channel"
STORAGE_PARTITIONS = "storage_partitions"
ROLE_USERS = "role_users"
NAMESPACE = "namespace"
MAINTAINER = "maintainer"
FLOW_ID = "flow_id"
TENANT = "tenant"
USER_IDS = "user_ids"
DATA_ENCODING = "data_encoding"
MSG_SYSTEM = "msg_system"
PUBLIC = "public"
BIZ_ID = "biz_id"
DATA_SET = "data_set"
ROLE_ID = "role_id"
PARTITION = "partition"
SERVER_ID = "server_id"
CLUSTER_INDEX = "cluster_index"
RAW_DATA_ID = "raw_data_id"
PARTITION_SPEC = "partition_spec"
RECORD_NUM = "recordNum"
RECORD = "record"
CONDITION_EXPRESSION = "conditionExpression"
ASSIGN_EXPRESSION = "assignExpression"
TIME_FIELD = "timeField"
CAMEL_ASYNC_COMPACT = "asyncCompact"
ASYNC_COMPACT = "async_compact"
UPDATE_PROPERTIES = "updateProperties"
ADD_FIELDS = "addFields"
REMOVE_FIELDS = "removeFields"
METHOD = "method"
FIELD = "field"
HOUR = "HOUR"
ARGS = "args"
ICEBERG_FIELDS = "iceberg_fields"
COMPACT_START = "compactStart"
COMPACT_END = "compactEnd"
DELETE_PARTITION = "deletePartition"
RENAME_FIELDS = "renameFields"
EXPIREDAYS = "expireDays"
NEWTABLENAME = "newTableName"
TABLENAME = "tableName"
DATABASENAME = "databaseName"
CONF_KEY = "conf_key"
CONF_VALUE = "conf_value"
USED = "Used"
TOTAL = "Total"
PERCENT_USED = "PercentUsed"
BEANS = "beans"

# 状态
UNKNOWN = "UNKNOWN"
SUCCESS = "SUCCESS"
FAILED = "FAILED"
PENDING = "PENDING"
WAITING = "WAITING"
RUNNING = "RUNNING"
CONNECTOR_RUNNING = "running"


# 时间相关
DTEVENTTIME = "dtEventTime"
DTEVENTTIMESTAMP = "dtEventTimeStamp"
THEDATE = "thedate"
LOCALTIME = "localTime"
TIMESTAMP = "timestamp"
OFFSET = "offset"
ET = "____et"  # 默认iceberg分区字段，内部字段，对用户不可见
PARTITION_TIME = "__time"  # clickhouse的分区字段

# processing type
BATCH = "batch"
STREAM = "stream"
CLEAN = "clean"
TRANSFORM = "transform"
MODEL = "model"
MODE = "mode"
STREAM_MODEL = "stream_model"
BATCH_MODEL = "batch_model"
STORAGE = "storage"
VIEW = "view"
QUERYSET = "queryset"
SNAPSHOT = "snapshot"
PROCESSING_TYPE = "processing_type"

# 数据类型
LONG = "long"
INT = "int"
STRING = "string"
BIGINT = "bigint"
TEXT = "text"
BOOLEAN = "boolean"
TINYINT = "tinyint"
FLOAT = "float"
DOUBLE = "double"
LONGTEXT = "longtext"
SHORT = "short"
DATETIME = "datetime"
BIGDECIMAL = "bigdecimal"
DECIMAL = "decimal"
INTEGER = "integer"
VARCHAR = "varchar"

INT_32 = "int32"
BOOL = "bool"
INT_64 = "int64"


REAL = "real"
DATE = "date"
OBJECT = "object"
KEYWORD = "keyword"
LIST = "list"
RANGE = "range"
LABEL = "label"
PLAT_NAME = "plat_name"
ROUTE = "route"
RAW_DATA_NAME = "raw_data_name"
TOPIC_NAME = "topic_name"
DATASET = "dataset"
BIZID = "bizid"
FILTER_NAME_AND = "filter_name_and"
FILTER_NAME_OR = "filter_name_or"
STREAM_FILTERS = "stream_filters"
DATA_SCENARIO = "data_scenario"
RAW_DATA_ALIAS = "raw_data_alias"
SENSITIVITY = "sensitivity"
CONDITION = "condition"
SPECIFICATION = "specification"
LOG = "log"
TLOG = "tlog"

# 账号，地址，域名等
LOCALHOST = "localhost"
ROOT = "root"
MAPLELEAF = "mapleleaf"
HOSTS = "hosts"
MODULES = "modules"
HOST = "host"
USER = "user"
PASSWORD = "password"
DB = "db"
USER_BACKEND = "user_backend"
PASSWORD_BACKEND = "password_backend"
SASL_PASS = "sasl.pass"
JDBC = "jdbc"
HTTP = "http"
TDWHDFS = "tdwhdfs"
TUBE = "tube"

# REQUESTS
JSON_HEADERS = {"Content-Type": "application/json"}

# task config
TASKS_MAX = "tasks.max"
GROUP_ID = "group.id"
DATA_ID = "data_id"
GROUP = "group"
AUTO_OFFSET_RESET = "auto_offset_reset"
TOPICS_DIR = "topics.dir"
TOPICS = "topics"
TOPIC = "topic"
CONFIG = "config"

# queue 授权状态
GRANTED = "granted"
REVOKING = "revoking"
REVOKED = "revoked"
EXPIRED = "expired"
PRODUCER = "producer"
USERNAME = "username"
GROUPID = "groupId"
GROUPID_LOWERCASE = "groupid"
CLUSTERINFO = "clusterInfo"
NOAUTH = "noAuth"
CLUSTER = "cluster"
QUEUE_USER = "queue_user"
QUEUE_PASSWORD = "queue_password"
DATA_TOKEN = "data_token"
TOKEN = "token"
QUEUE_DB = "queue_db"
DATABUS = "databus"
ACCESS = "access"

IDS = "ids"
RPC_PORT = "rpc_port"
SERVICERPC_PORT = "servicerpc_port"
HDFS_CLUSTER_NAME = "hdfs_cluster_name"
HDFS_DEFAULT_PARAMS = "hdfs_default_params"
FS_DEFAULTFS = "fs.defaultFS"
DFS_REPLICATION = "dfs.replication"
DFS_NAMESERVICES = "dfs.nameservices"
DFS_HA_NAMENODES = "dfs.ha.namenodes"
DFS_CLIENT_FAILOVER_PROXY_PROVIDER = "dfs.client.failover.proxy.provider"
DFS_NAMENODE_RPC_ADDRESS = "dfs.namenode.rpc-address"
DFS_NAMENODE_SERVICERPC_ADDRESS = "dfs.namenode.servicerpc-address"
DFS_NAMENODE_HTTP_ADDRESS = "dfs.namenode.http-address"
TOPIC_DIR = "topic_dir"
HDFS_CONF_DIR = "hdfs_conf_dir"
HDFS_CONF = "hdfs_conf"
LOG_DIR = "log_dir"
FLUSH_SIZE = "flush.size"
PARQUET_FLUSH_SIZE = "flush_size"
DEFAULT_FLUSH_SIZE = 1000000
RAW = "raw"
CHANNEL_NAME = "channel_name"
CHANNEL_TYPE = "channel_type"
CHANNEL_CLUSTER_NAME = "channel_cluster_name"
OP = "op"
ADMIN = "admin"
APP_ID = "app_id"
ZONE_ID = "zone_id"
SET_ID = "set_id"
INCREMENTING = "incrementing"
TABLE_WHITE_LIST = "tableWhitelist"
INCREMENTING_COLUMN_NAME = "incrementingColumnName"
POLL_INTERVAL_MS = "pollIntervalMs"
TABLE_POLL_INTERVAL_MS = "tablePollIntervalMs"
KAFKA_METRIC_CONFIG = "kafkaMetricConfig"
ITERARION_IDX = "_iterarion_idx"
TEST_NAMESPACE = "test_namespace"
MONITOR_PRODUCER_BOOTSTRAP_SERVERS = "monitor.producer.bootstrap.servers"
MONITOR_PRODUCER_TOPIC = "monitor.producer.topic"
PRODUCER_TOPIC = "producer.topic"
MONITOR_MODULE_NAME = "monitor.module.name"
MONITOR_COMPONENT_NAME = "monitor.component.name"
MIGRATION = "migration"
SOURCE = "source"
PULLER_CLUSTER_NAME = "puller_cluster_name"
CONNECTORS = "connectors"
WORKERS_NUM = "workers_num"

TIMEZONE_ID = "timezone_id"
DATA_DIR = "data_dir"
FIELD_NAMES = "field_names"

# 灰度数据湖
HDFS_MAINTAIN_SKIP_RTS = "hdfs.maintain.skip.rts"
ICEBERG_TRANSFORM_RTS = "iceberg.transform.rts"

REGISTER_TYPE = "register_type"
AUTH_TYPE = "authtype"
APP_USER = "app_user"
FILENAME = "filename"
CONTENT = "content"

TRANS_ID = "trans_id"
GET_TABLE_ATTACHS = "get_table_attachs"
GET_TABLE_STRUCT = "get_table_struct"
STRUCT = "struct"
TABLE_STRUCT_CONTENT = "table_struct_content"
TABLE_LIST = "table_list"
ATTACHMENT_ID = "attachment_id"
AUTO_APPROVE = "auto_approve"
AUTO_EXEC_TRANS = "auto_exec_trans"
ATTACH_ID = "attach_id"
MEMO = "memo"

COLS = "cols"
MSG = "msg"
TCAPLUS_FIELDS = "tcaplus_fields"
XML = "xml"
YES = "yes"
CHECK = "check"
RET = "ret"
KEY_FIELDS = "key_fields"
VALUE_FIELDS = "value_fields"
KEY_FIELD = "KeyField"
VALUE_FIELD = "ValueField"
KEY_NAME = "Name"
KEY_TYPE = "Type"
FILES = "files"

HDFS_DATA_TYPE = "hdfs.data_type"

ICEBERG_BIZ_IDS = "iceberg.biz.ids"
HIVE_METASTORE_PORT = "HIVE_METASTORE_PORT"
HIVE_METASTORE_HOSTS = "HIVE_METASTORE_HOSTS"
HIVE_METASTORE_URIS = "hive.metastore.uris"

RESULT_TABLE_INFO = "result_table_info"
RESULT_TABLE_IDS = "result_table_ids"
QUERY_RT_BATCH_SIZE = 50
TIME_ZONE = "time_zone"
PREFER_STORAGE = "prefer_storage"

QUALIFIED_NAME = "qualified_name"
DEPTH = "depth"
EXTRA_RETRIEVE = "extra_retrieve"
DIRECTION = "direction"

# clickhouse相关
REPLICATED_TABLE = "replicated_table"
DISTRIBUTED_TABLE = "distributed_table"
DATETIME_TYPE = "DateTime"
CONSISTENCY = "consistency"
SCHEMAS = "schemas"
CLICKHOUSE_FIELDS = "clickhouse_fields"
DISTINCT_PARTITIONS = "distinct_partitions"
TOTAL_PARTITIONS = "total_partitions"
TOP_PARTITIONS = "top_partitions"
EXCEPTION = "exception"
MAX = "max"
MIN = "min"
SUM = "sum"
AVERAGE = "average"
USED_SIZE = "used_size"
MAX_SIZE = "max_size"
STORAGE_USAGE = "storage_usage"
QUERY_ID = "query_id"
QUERY = "query"
ELAPSED = "elapsed"
PROCESSLIST = "processlist"
TOTAL_SPACE = "total_space"
USED_SPACE = "used_space"
USED_MAX = "usage_max"
USED_MIN = "usage_min"
USED_SUM = "used_sum"
TOTAL_SUM = "total_sum"
TOTAL_USAGE = "total_usage"
LOCAL = "local"
CK_DEFAULT_CONNECT_TIMEOUT_SEC = 60
CK_DEFAULT_SYNC_REQUEST_TIMEOUT_SEC = 30

# DT 相关
CHANNEL_CLUSTER_INDEX = "channel_cluster_index"
TRANSFERRING_ID = "transferring_id"
TRANSFERRING_ALIAS = "transferring_alias"
TRANSFERRING_TYPE = "transferring_type"
INPUTS = "inputs"
OUTPUTS = "outputs"
DATA_SET_TYPE = "data_set_type"
DATA_SET_ID = "data_set_id"
STORAGE_CLUSTER_CONFIG_ID = "storage_cluster_config_id"
CHANNEL_CLUSTER_CONFIG_ID = "channel_cluster_config_id"

SHIPPER = "shipper"
PULLER = "puller"
# transport相关
KEY_FIELDS_JAVA = "keyFields"
KEY_SEPARATOR_JAVA = "keySeparator"
IGNITE_CACHE_JAVA = "igniteCache"
IGNITE_MAX_RECORDS_JAVA = "igniteMaxRecords"
IGNITE_CLUSTER_JAVA = "igniteCluster"
IGNITE_HOST_JAVA = "igniteHost"
IGNITE_PASS_JAVA = "ignitePass"
IGNITE_PORT_JAVA = "ignitePort"
IGNITE_USER_JAVA = "igniteUser"
USE_THIN_CLIENT_JAVA = "useThinClient"
HDFS_CUSTOM_PROPERTY_JAVA = "hdfsCustomProperty"
THIN_CLIENT_THRESHOLD = "thin.client.threshold"
FLUSH_SIZE_JAVA = "flushSize"
SINK_CONFIG_JAVA = "sinkConfig"
SOURCE_CONFIG_JAVA = "sourceConfig"
MSG_TYPE_JAVA = "msgType"
SOURCE_RT_ID = "source_rt_id"
SOURCE_TYPE = "source_type"
SINK_RT_ID = "sink_rt_id"
SINK_TYPE = "sink_type"
CONCURRENCY = "concurrency"
CONNECTOR = "connector"
HDFS_PROPERTY_JAVA = "hdfsProperty"
DATA_DIR_JAVA = "dataDir"
ICEBERG_DATABASE_JAVA = "icebergDatabase"
ICEBERG_TABLE_JAVA = "icebergTable"
GEOG_AREA_JAVA = "geogArea"
DATA_TYPE_JAVA = "dataType"
RT_ID_JAVA = "rtId"
CLICKHOUSE_RT_ID_JAVA = "clickhouseRtId"
CLICKHOUSE_PROPERTIES_JAVA = "clickhouseProperties"
DB_NAME_JAVA = "dbName"
REPLICATED_TABLE_JAVA = "replicatedTable"
CLICKHOUSE_COLUMN_ORDER_JAVA = "clickhouseColumnOrder"
TOPIC_NAME_JAVA = "topicName"
PARALLELISM = "parallelism"
ARCHIVE = "archive"
SCHEMA_TYPE_JAVA = "schemaType"
CONFIGS = "configs"
SOURCE_RT_ID_JAVA = "sourceRtId"
SINK_RT_ID_JAVA = "sinkRtId"
LAST_READ_LINE_NUMBER = "last_read_line_number"
LAST_READ_LINE_NUMBER_JAVA = "lastReadLineNumber"
LAST_READ_FILE_NAME = "last_read_file_name"
LAST_READ_FILE_NAME_JAVA = "lastReadFileName"
PROCESSED_ROWS = "processed_rows"
PROCESSED_ROWS_JAVA = "processedRows"
FINISHED = "finished"
CREATE_TIME = "create_rime"
CREATE_TIME_JAVA = "createTime"
UPDATE_TIME = "update_time"
UPDATE_TIME_JAVA = "updateTime"
FINISH_TIME = "finish_time"
FINISH_TIME_JAVA = "finishTime"
TIME_TAKEN = "time_taken"
TIME_TAKEN_JAVA = "timeTaken"
STAGE_STATUS = "stage_status"
STAGE_TYPE = "stage_type"
EXECUTE = "execute"
STAGE_SEQ = "stage_seq"
STAGES = "stages"
ACCESS_CONF_INFO = "access_conf_info"
RESOURCE = "resource"
SCOPE_CONFIG = "scope_config"
PATHS = "paths"
SYSTEM = "system"
LINUX = "linux"
FOR_DATALAB = "for_datalab"
START_SHIPPER_TASK = "start_shipper_task"
TID = "tid"
INAME = "iname"
INTERFACE_NAME = "interface_name"
ASCII = "ascii"
IS_MIX_SCHEMA = "is_mix_schema"
TASKS = "tasks"

MAX_RECORDS = "max_records"
KEY_SEPARATOR = "key_separator"
SORTED_KEYS = "sorted_keys"

QUEUE_PULSAE = "queue_pulsar"
DIR_DOMAIN = "dir_domain"
DIR_LIST = "dir_list"
SERVERPORT = "ServerPort"
SERVERIP = "ServerIP"

SNAPSHOTS = "snapshots"
TIMESTAMP_MS = "timestamp_ms"
SASL_USERNAME = "sasl_username"
SECURITY_PROTOCOL = "security_protocol"
SASL_PASSWD = "sasl_passwd"
SASL_MECHANISMS = "sasl_mechanisms"
SASL__USER = "sasl.user"
SASL__PASS = "sasl.pass"
USE__SASL = "use.sasl"

RAW_DATA = "raw_data"
SCENARIO_NAME = "scenario_name"
PROCESSING_ID = "processing_id"
DATA_PROCESSING = "data_processing"
DIMENSION_TYPE = "dimension_type"
DIMENSION_NAME = "dimension_name"

TABLE_INFO = "table_info"

MINMAX = "minmax"
GRANULARITY = "granularity"
EXPRESSION = "expression"
INDEX_TYPE = "index_type"

FREE_DISK = "free_disk"
ZK_ADDRESS = "zk_address"
WEIGHTS = "weights"
FACTOR = "factor"
HTTP_PORT = "http_port"
PREASSIGNED_DATA_ID = "preassigned_data_id"
IGNORE_FILE_END_WITH = "ignore_file_end_with"
ENCODING = "encoding"

SOURCE_HDFS_PROPERTY_JAVA = "sourceHdfsProperty"
SOURCE_DATA_DIR_JAVA = "sourceDataDir"
SOURCE_ICEBERG_DATABASE_JAVA = "sourceIcebergDatabase"
SOURCE_ICEBERG_TABLE_JAVA = "sourceIcebergTable"
SOURCE_GEOG_AREA_JAVA = "sourceGeogArea"
SOURCE_DATA_TYPE_JAVA = "sourceDataType"

SINK_HDFS_PROPERTY_JAVA = "sinkHdfsProperty"
SINK_DATA_DIR_JAVA = "sinkDataDir"
SINK_ICEBERG_DATABASE_JAVA = "sinkIcebergDatabase"
SINK_ICEBERG_TABLE_JAVA = "sinkIcebergTable"
SINK_GEOG_AREA_JAVA = "sinkGeogArea"
SINK_DATA_TYPE_JAVA = "sinkDataType"
SOURCE_TYPE_JAVA = "sourceType"
SINK_TYPE_JAVA = "sinkType"
RECOVER_CLASS_NAME_JAVA = "recoverClassName"
PERCENTAGE = "percentage"

ODM = "odm"
TGLOG = "tglog"
OFFLINEFILE = "offlinefile"
HDFS_PATH = "hdfs_path"
HDFS_PORT = "hdfs_port"
HDFS_HOST = "hdfs_host"
DATALAB = "datalab"
RAW_DATA_IDS = "raw_data_ids"
FILE = "file"
UPLOAD_UUID = "upload_uuid"
TASK_NAME = "task_name"
CHUNK_ID = "chunk_id"
CHUNK_SIZE = "chunk_size"
MD5 = "md5"

LATEST = "latest"
EARLIEST = "earliest"
CONF = "conf"
OUTPUT_FORMAT = "output_format"
DEPLOY_PLAN_ID = "deploy_plan_id"
OP_TYPE = "op_type"
PROCESS_INFOS = "process_infos"
SETUP_PATH = "setup_path"
PROC_NAME = "proc_name"
PID_PATH = "pid_path"
ACCOUNT = "account"
IP_LIST = "ip_list"
DATA_SOURCE = "data_source"
BIZ = "biz"

BACKUPS = "backups"
CYCLE_TIME = "cycle_time"
CANCLE = "cancle"

MINUTE = "minute"
TDM_CLUSTER_ID = "tdm_cluster_id"
TDM_CLUSTER_ALIAS = "tdm_cluster_alias"
TDM = "tdm"

STORE_SIZE = "store.size"
DOCS_COUNT = "docs.count"
TOP = "top"
FILE_NAME = "file_name"

# 场景名称
STORAGE_SCENARIO_NAME = "storage_scenario_name"
STORAGE_SCENARIO_ALIAS = "storage_scenario_alias"
FORMAL_NAME_FILED = "formal_name"
STORAGE_SCENARIO_PRIORITY = "storage_scenario_priority"
CLUSTER_TYPE_PRIORITY = "cluster_type_priority"
STORAGE_CLUSTER_CONFIG = "storage_cluster_config"
BEGIN_TIME = "begin_time"
LOGS_ZH = "logs_zh"
LOGS_EN = "logs_en"

TDBANK_FIELDS = "tdbank_fields"
ALTER_ID = "alter_id"
METRIC_ID = "metric_id"
REPORT = "report"
RESOURCECENTER = "resourceCenter"
CREATE_CLUSTER = "create_cluster"
UPDATE_CLUSTER = "update_cluster"
GET_CLUSTER = "get_cluster"
SUB = "sub"
U_RT_ID = "rt_id"
RT_ID_STORAGE = "rt_id_storage"
GTE = "gte"
LTE = "lte"
PARTITION_DATE = "partition_date"
PARTITION_NAME = "partition_name"
LZ_SERVERS_INFO = "lz_servers_info"
SERVER_TYPE = "server_type"
APP_GROUP_NAME = "app_group_name"
BG_ID = "bg_id"
SERVERS_INFO = "servers_info"
DIM_FIELDS = "dim_fields"
EXCEPT_FIELDS = "except_fields"
TDW_APP_GROUP = "tdw_app_group"
SOURCE_SERVER = "source_server"
TARGET_FILTER = "target_filter"
TARGET_TYPE = "target_type"
TAG_FILTER = "tag_filter"
MATCH_POLICY = "match_policy"
ERRORS = "errors"
