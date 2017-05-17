import yaml
import sys
import commands
from itertools import groupby
from operator import itemgetter

if (len(sys.argv) != 3):
	print "Invalid number of arguments"
	sys.exit(0)

wd = str(sys.argv[1])
env = str(sys.argv[2])
hosts_file = wd + '/hosts/' + env
env_path = wd + '/group_vars/' + env
tf_path = wd + '/roles/terraform/meta/' + env

tfstate_file = tf_path + '/terraform.tfstate'
nodes_file = env_path + '/nodes.yml'

node_stream = open(nodes_file, "r")
nodes = yaml.load(node_stream)

# Print private ip in nodes.yml
for node in nodes['nodes']:
	cmd = ['terraform', 'state', 'show', '-state', tfstate_file, 'scaleway_server.'+node, '|', 'grep', '-i', 'private_ip', '|', 'sed', '\'s/^.*= //\'']
	private_ip = commands.getoutput(' '.join(cmd))
	nodes['nodes'][node]['ip'] = private_ip

	cmd = ['terraform', 'state', 'show', '-state', tfstate_file, 'scaleway_server.'+node, '|', 'grep', '-i', 'public_ip', '|', 'sed', '\'s/^.*= //\'']
	public_ip = commands.getoutput(' '.join(cmd))
	nodes['nodes'][node]['public_ip'] = public_ip

file_ = open(nodes_file, 'w')
file_.write(yaml.dump(nodes))
file_.close()

# Construct hosts file
file_ = open(hosts_file, 'w')
file_.write('['+env+']\n')

groups = {}
for node in nodes['nodes']:
	key = nodes['nodes'][node]['role']
	value = nodes['nodes'][node]['public_ip']

	file_.write(value+'\n')

	if (key in groups):
		groups[key].append(value)
	else:
		groups[key] = [value]

for key in groups:
	file_.write('['+key+']\n')
	for value in groups[key]:
		file_.write(value+'\n')
file_.close()