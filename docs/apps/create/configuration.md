# Configuration
The second part of the app creation process deals with defining the configuration. The configuration is used to configure the docker containers, but also to link multiple containers together in case a single app would rely on multiple docker containers.

The configuration is stored in a git repository like github or bitbucket and contains the configuration files and resources for all docker containers inside the app. When an app is installed, a git clone will be done to get the contents from the git repository. **Be aware that private git repo's are not supported at the moment**

In theory, you could use any diretory layout you like, but we usually put all the configuration within a config folder. It is possible to also put other resources into the git repo and mount them as volumes inside the container.

For our elasticsearch tint, we will need the following filesystem layout:
```
 root
 +-- config
     +-- elasticsearch
         +-- elasticsearch.yml
         +-- logging.yml
```

## Templates
Resources and configuration files are treated as templates using the jinja2 language, which means you can put in control structures like loops or if-else-then conditionals into your templates. You can also work with variables inside these templatess. Let's have a quick overview.

### Variables
Variables are enclosed in double brackets for hex variables and double curly brackets for ansible variables. They may have attributes or elements on them which you can access using the dot notation.

cluster variables:
```
[[ myvar ]]
[[ myobject.name ]]
```

ansible variables:
```
{{ ansible_hostname }}
```

If a variable or attribute does not exist, you will get back an undefined value. That value will evaluate to an empty string if printed or iterated over, and fails for every other operation.

The following cluster variables are available:

 - **hex.id** - the unique id of the hex
 - **hex.name** - the name of the hex
 - **hex.arch** - the architecture of the hex
 - **hex.network_range** - the network range used for the internal network
 - **hex.node_count** - the number of nodes in this cluster
 - **hex.hive.user.id** - the id of the user to which this cluster is linked (if it is linked)
 - **hex.hive.user.name** - the name of the user to which this cluster is linked (if it is linked)
 - **hex.hive.user.email** - the email address of the user to which this cluster is linked (if it is linked)
 - **firmware** - the firmware version
 - **docker.registry** - the default docker registry used for installing the app
 - **dirs.data** - the data directory on the **host** filesystem used for this container
 - **dirs.config** - the config directory on the **host** filesystem used for this container
 - **tint.id** - the id of the app you are installing

### Conditionals

For testing on cluster variables:
```
[% if name is defined %]
...
[% endif %]
```

For testing on ansible variables:
```
{% if name is defined %}
...
{% endif %}
```

### Loops

For looping over cluster variables:
[% for item in items %]
...
[% endfor %]

For looping over ansible variables:
{% for item in items %}
...
{% endfor %}

## Common template fragments
We noticed we reuse a lot of fragments from our templates, so we are happy to share them with you.


### Iterate over all hosts
```
{% for host in groups['all'] %}
...
{% endfor %}
```

### Get the internal ip address of a specific node
Since the internal ip address of a node is predictable you could use something like the following:

```
{{ ansible_local.bb.network.range }}.1
```

However, we would prefer you to use something like this:

```
[[ hex.id ]]-n1.hex
```

All internal ip addresses are mapped to __hex.id__-n__sequence__.hex

### Get the hostname of the node on which you are installing
```
{{ ansible_hostname }}
```

## Example Templates
For our elasticsearch tint, we would need to create two templates; one for elasticsearch.yml, and one for logging.yml:

### elasticsearch.yml
```
##################### Elasticsearch Configuration Example #####################

# This file contains an overview of various configuration settings,
# targeted at operations staff. Application developers should
# consult the guide at <http://elasticsearch.org/guide>.
#
# The installation procedure is covered at
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/setup.html>.
#
# Elasticsearch comes with reasonable defaults for most settings,
# so you can try it out without bothering with configuration.
#
# Most of the time, these defaults are just fine for running a production
# cluster. If you're fine-tuning your cluster, or wondering about the
# effect of certain configuration option, please _do ask_ on the
# mailing list or IRC channel [http://elasticsearch.org/community].

# Any element in the configuration can be replaced with environment variables
# by placing them in ${...} notation. For example:
#
#node.rack: ${RACK_ENV_VAR}

# For information on supported formats and syntax for the config file, see
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/setup-configuration.html>


################################### Cluster ###################################

# Cluster name identifies your cluster for auto-discovery. If you're running
# multiple clusters on the same network, make sure you're using unique names.
#
#cluster.name: elasticsearch 
cluster.name: "{{ ansible_local.bb.hex.name }}"


#################################### Node #####################################

# Node names are generated dynamically on startup, so you're relieved
# from configuring them manually. You can tie this node to a specific name:
#
#node.name: "Franz Kafka"
node.name: "{{ ansible_hostname }}"

# Every node can be configured to allow or deny being eligible as the master,
# and to allow or deny to store the data.
#
# Allow this node to be eligible as a master node (enabled by default):
#
#node.master: true
#
# Allow this node to store data (enabled by default):
#
#node.data: true

# You can exploit these settings to design advanced cluster topologies.
#
# 1. You want this node to never become a master node, only to hold data.
#    This will be the "workhorse" of your cluster.
#
#node.master: false
#node.data: true
#
# 2. You want this node to only serve as a master: to not store any data and
#    to have free resources. This will be the "coordinator" of your cluster.
#
#node.master: true
#node.data: false
#
# 3. You want this node to be neither master nor data node, but
#    to act as a "search load balancer" (fetching data from nodes,
#    aggregating results, etc.)
#
#node.master: false
#node.data: false

# Use the Cluster Health API [http://localhost:9200/_cluster/health], the
# Node Info API [http://localhost:9200/_nodes] or GUI tools
# such as <http://www.elasticsearch.org/overview/marvel/>,
# <http://github.com/karmi/elasticsearch-paramedic>,
# <http://github.com/lukas-vlcek/bigdesk> and
# <http://mobz.github.com/elasticsearch-head> to inspect the cluster state.

# A node can have generic attributes associated with it, which can later be used
# for customized shard allocation filtering, or allocation awareness. An attribute
# is a simple key value pair, similar to node.key: value, here is an example:
#
#node.rack: rack314

# By default, multiple nodes are allowed to start from the same installation location
# to disable it, set the following:
#node.max_local_storage_nodes: 1


#################################### Index ####################################

# You can set a number of options (such as shard/replica options, mapping
# or analyzer definitions, translog settings, ...) for indices globally,
# in this file.
#
# Note, that it makes more sense to configure index settings specifically for
# a certain index, either when creating it or by using the index templates API.
#
# See <http://elasticsearch.org/guide/en/elasticsearch/reference/current/index-modules.html> and
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/indices-create-index.html>
# for more information.

# Set the number of shards (splits) of an index (5 by default):
#
#index.number_of_shards: 5
index.number_of_shards: 6

# Set the number of replicas (additional copies) of an index (1 by default):
#
#index.number_of_replicas: 1

# Note, that for development on a local machine, with small indices, it usually
# makes sense to "disable" the distributed features:
#
#index.number_of_shards: 1
#index.number_of_replicas: 0

# These settings directly affect the performance of index and search operations
# in your cluster. Assuming you have enough machines to hold shards and
# replicas, the rule of thumb is:
#
# 1. Having more *shards* enhances the _indexing_ performance and allows to
#    _distribute_ a big index across machines.
# 2. Having more *replicas* enhances the _search_ performance and improves the
#    cluster _availability_.
#
# The "number_of_shards" is a one-time setting for an index.
#
# The "number_of_replicas" can be increased or decreased anytime,
# by using the Index Update Settings API.
#
# Elasticsearch takes care about load balancing, relocating, gathering the
# results from nodes, etc. Experiment with different settings to fine-tune
# your setup.

# Use the Index Status API (<http://localhost:9200/A/_status>) to inspect
# the index status.


#################################### Paths ####################################

# Path to directory containing configuration (this file and logging.yml):
#
#path.conf: /path/to/conf

# Path to directory where to store index data allocated for this node.
#
#path.data: /path/to/data
#
# Can optionally include more than one location, causing data to be striped across
# the locations (a la RAID 0) on a file level, favouring locations with most free
# space on creation. For example:
#
#path.data: /path/to/data1,/path/to/data2
path.data: /data

# Path to temporary files:
#
#path.work: /path/to/work

# Path to log files:
#
#path.logs: /path/to/logs

# Path to where plugins are installed:
#
#path.plugins: /path/to/plugins


#################################### Plugin ###################################

# If a plugin listed here is not installed for current node, the node will not start.
#
#plugin.mandatory: mapper-attachments,lang-groovy


################################### Memory ####################################

# Elasticsearch performs poorly when JVM starts swapping: you should ensure that
# it _never_ swaps.
#
# Set this property to true to lock the memory:
#
#bootstrap.mlockall: true

# Make sure that the ES_MIN_MEM and ES_MAX_MEM environment variables are set
# to the same value, and that the machine has enough memory to allocate
# for Elasticsearch, leaving enough memory for the operating system itself.
#
# You should also make sure that the Elasticsearch process is allowed to lock
# the memory, eg. by using `ulimit -l unlimited`.


############################## Network And HTTP ###############################

# Elasticsearch, by default, binds itself to the 0.0.0.0 address, and listens
# on port [9200-9300] for HTTP traffic and on port [9300-9400] for node-to-node
# communication. (the range means that if the port is busy, it will automatically
# try the next port).

# Set the bind address specifically (IPv4 or IPv6):
#
#network.bind_host: 192.168.0.1
network.bind_host: 0
network.host: _non_loopback_

discovery.zen.ping.unicast.hosts: [ {{ansible_local.bb.network.range}}.1,  {{ansible_local.bb.network.range}}.2, {{ansible_local.bb.network.range}}.3, {{ansible_local.bb.network.range}}.4, {{ansible_local.bb.network.range}}.5,  {{ansible_local.bb.network.range}}.6 ]

# Set the address other nodes will use to communicate with this node. If not
# set, it is automatically derived. It must point to an actual IP address.
#
#network.publish_host: 192.168.0.1

# Set both 'bind_host' and 'publish_host':
#
#network.host: 192.168.0.1

# Set a custom port for the node to node communication (9300 by default):
#
#transport.tcp.port: 9300

# Enable compression for all communication between nodes (disabled by default):
#
#transport.tcp.compress: true

# Set a custom port to listen for HTTP traffic:
#
#http.port: 9200

# Set a custom allowed content length:
#
#http.max_content_length: 100mb

# Disable HTTP completely:
#
#http.enabled: false


################################### Gateway ###################################

# The gateway allows for persisting the cluster state between full cluster
# restarts. Every change to the state (such as adding an index) will be stored
# in the gateway, and when the cluster starts up for the first time,
# it will read its state from the gateway.

# There are several types of gateway implementations. For more information, see
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/modules-gateway.html>.

# The default gateway type is the "local" gateway (recommended):
#
#gateway.type: local

# Settings below control how and when to start the initial recovery process on
# a full cluster restart (to reuse as much local data as possible when using shared
# gateway).

# Allow recovery process after N nodes in a cluster are up:
#
#gateway.recover_after_nodes: 1

# Set the timeout to initiate the recovery process, once the N nodes
# from previous setting are up (accepts time value):
#
#gateway.recover_after_time: 5m

# Set how many nodes are expected in this cluster. Once these N nodes
# are up (and recover_after_nodes is met), begin recovery process immediately
# (without waiting for recover_after_time to expire):
#
#gateway.expected_nodes: 2


############################# Recovery Throttling #############################

# These settings allow to control the process of shards allocation between
# nodes during initial recovery, replica allocation, rebalancing,
# or when adding and removing nodes.

# Set the number of concurrent recoveries happening on a node:
#
# 1. During the initial recovery
#
#cluster.routing.allocation.node_initial_primaries_recoveries: 4
#
# 2. During adding/removing nodes, rebalancing, etc
#
#cluster.routing.allocation.node_concurrent_recoveries: 2

# Set to throttle throughput when recovering (eg. 100mb, by default 20mb):
#
#indices.recovery.max_bytes_per_sec: 20mb

# Set to limit the number of open concurrent streams when
# recovering a shard from a peer:
#
#indices.recovery.concurrent_streams: 5


################################## Discovery ##################################

# Discovery infrastructure ensures nodes can be found within a cluster
# and master node is elected. Multicast discovery is the default.

# Set to ensure a node sees N other master eligible nodes to be considered
# operational within the cluster. Its recommended to set it to a higher value
# than 1 when running more than 2 nodes in the cluster.
#
#discovery.zen.minimum_master_nodes: 1

# Set the time to wait for ping responses from other nodes when discovering.
# Set this option to a higher value on a slow or congested network
# to minimize discovery failures:
#
#discovery.zen.ping.timeout: 3s

# For more information, see
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/modules-discovery-zen.html>

# Unicast discovery allows to explicitly control which nodes will be used
# to discover the cluster. It can be used when multicast is not present,
# or to restrict the cluster communication-wise.
#
# 1. Disable multicast discovery (enabled by default):
#
#discovery.zen.ping.multicast.enabled: false
#
# 2. Configure an initial list of master nodes in the cluster
#    to perform discovery when new nodes (master or data) are started:
#
#discovery.zen.ping.unicast.hosts: ["host1", "host2:port"]

# EC2 discovery allows to use AWS EC2 API in order to perform discovery.
#
# You have to install the cloud-aws plugin for enabling the EC2 discovery.
#
# For more information, see
# <http://elasticsearch.org/guide/en/elasticsearch/reference/current/modules-discovery-ec2.html>
#
# See <http://elasticsearch.org/tutorials/elasticsearch-on-ec2/>
# for a step-by-step tutorial.

# GCE discovery allows to use Google Compute Engine API in order to perform discovery.
#
# You have to install the cloud-gce plugin for enabling the GCE discovery.
#
# For more information, see <https://github.com/elasticsearch/elasticsearch-cloud-gce>.

# Azure discovery allows to use Azure API in order to perform discovery.
#
# You have to install the cloud-azure plugin for enabling the Azure discovery.
#
# For more information, see <https://github.com/elasticsearch/elasticsearch-cloud-azure>.

################################## Slow Log ##################################

# Shard level query and fetch threshold logging.

#index.search.slowlog.threshold.query.warn: 10s
#index.search.slowlog.threshold.query.info: 5s
#index.search.slowlog.threshold.query.debug: 2s
#index.search.slowlog.threshold.query.trace: 500ms

#index.search.slowlog.threshold.fetch.warn: 1s
#index.search.slowlog.threshold.fetch.info: 800ms
#index.search.slowlog.threshold.fetch.debug: 500ms
#index.search.slowlog.threshold.fetch.trace: 200ms

#index.indexing.slowlog.threshold.index.warn: 10s
#index.indexing.slowlog.threshold.index.info: 5s
#index.indexing.slowlog.threshold.index.debug: 2s
#index.indexing.slowlog.threshold.index.trace: 500ms

################################## GC Logging ################################

#monitor.jvm.gc.young.warn: 1000ms
#monitor.jvm.gc.young.info: 700ms
#monitor.jvm.gc.young.debug: 400ms

#monitor.jvm.gc.old.warn: 10s
#monitor.jvm.gc.old.info: 5s
#monitor.jvm.gc.old.debug: 2s

################################## Security ################################

# Uncomment if you want to enable JSONP as a valid return transport on the
# http server. With this enabled, it may pose a security risk, so disabling
# it unless you need it is recommended (it is disabled by default).
#
#http.jsonp.enable: true
```

### logging.yml
```
# you can override this using by setting a system property, for example -Des.logger.level=DEBUG
es.logger.level: INFO
rootLogger: ${es.logger.level}, console, file
logger:
  # log action execution errors for easier debugging
  action: DEBUG
  # reduce the logging for aws, too much is logged under the default INFO
  com.amazonaws: WARN

  # gateway
  #gateway: DEBUG
  #index.gateway: DEBUG

  # peer shard recovery
  #indices.recovery: DEBUG

  # discovery
  #discovery: TRACE

  index.search.slowlog: TRACE, index_search_slow_log_file
  index.indexing.slowlog: TRACE, index_indexing_slow_log_file

additivity:
  index.search.slowlog: false
  index.indexing.slowlog: false

appender:
  console:
    type: console
    layout:
      type: consolePattern
      conversionPattern: "[%d{ISO8601}][%-5p][%-25c] %m%n"

  file:
    type: dailyRollingFile
    file: ${path.logs}/${cluster.name}.log
    datePattern: "'.'yyyy-MM-dd"
    layout:
      type: pattern
      conversionPattern: "[%d{ISO8601}][%-5p][%-25c] %m%n"

  index_search_slow_log_file:
    type: dailyRollingFile
    file: ${path.logs}/${cluster.name}_index_search_slowlog.log
    datePattern: "'.'yyyy-MM-dd"
    layout:
      type: pattern
      conversionPattern: "[%d{ISO8601}][%-5p][%-25c] %m%n"

  index_indexing_slow_log_file:
    type: dailyRollingFile
    file: ${path.logs}/${cluster.name}_index_indexing_slowlog.log
    datePattern: "'.'yyyy-MM-dd"
    layout:
      type: pattern
      conversionPattern: "[%d{ISO8601}][%-5p][%-25c] %m%n"
```