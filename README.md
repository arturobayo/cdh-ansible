# cdh-ansible

cdh-ansible is an ansible-based Cloudera's Distribution of Apache Hadoop deployer for Red Hat/CentOS nodes.

# Features

  - Easy to configure (just modifying nodes.yml file for basic configuration)
  - Operating System level tuning
  - Active Directory / LDAP integration and SSSD
  - Customizable CDH version installer
  - Cloudera Manager installer on Service Nodes

You can also:
  - Launch cloud infrastructure using Terraform
  - Configure deployment to multiple environments

### Technology

cdh-ansible uses a number of open source projects to work properly:

* [Ansible] - Ansible is a radically simple IT automation system.
* [Terraform] - Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.

### How to run

cdh-ansible requires [Ansible] v2.0.2+ to run.

```sh
$ ansible-playbook run-setup.yml -e env=development
```
For production environments...

```sh
$ ansible-playbook -vvvv run-setup.yml -e env=development
```

### Configuration

The files specified below should be configured:

| File | Description |
| ------ | ------ |
| /group_vars/*environment*/nodes.yml | Configure your cluster's topology |


#### nodes.yml

This file contains information related to your environment. In particular, it should contain detailed info about your nodes. Syntax is specified below:

```
nodes:
  <NODE_NAME>:
    disks:
    - {dev: <DEVICE_NAME_IN_OS>, fs: <CREATE_FS_ON_DEV>, mount: <MOUNT_POINT>, size: <SIZE_IN_GB>, type: <DEV_TYPE>, volume: <REQUEST_VOLUME>}
    flavor: <CLOUD_VENDOR_NODE_FLAVOR>
    fqdn: <NODE_FQDN>
    role: <NODE_ROLE>
  <NODE_NAME>:
  ...
```
| Variable | Description | Allowed values | 
| ------ | ------ | ------ |
| NODE_NAME | Node name | Example: master01 |
| DEVICE_NAME_IN_OS | Device name | Example: vda,vdb |
| CREATE_FS_ON_DEV | Wether to create FS on device or not | true,false |
| MOUNT_POINT | Where to mount the device at OS-level | Example: /data/device1 |
| REQUEST_VOLUME | (Optional) Wether to create volume for the node in Terraform | true,false (Default: false) |
| SIZE_IN_GB | (Optional) Volume size in GB, used by Terraform when requesting new volume | 50, 250 |
| DEV_TYPE | (Optional) Volume type, used by Terraform when requesting new volume | Example: ssd,hdd |
| CLOUD_VENDOR_NODE_FLAVOR | (Optional) Used by Terraform to launch node in cloud vendor | Example: m4.xlarge (for AWS) |
| NODE_FQDN | Node's FQDN, used by ansible to auto-generate /etc/hosts file | Example: master01.mycluster.int |
| NODE_ROLE | Node's role in the cluster | service,master,worker,edge |


### Todos

 - Simplify configuration

License
----

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [ansible]: <https://github.com/ansible/ansible>
   [terraform]: <https://github.com/hashicorp/terraform>
