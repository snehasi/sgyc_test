import testinfra
import sys

def check_installed(host, package):
    return host.package(package).is_installed

def check_deamon(host, service):
    return host.service(service).is_running

if len(sys.argv) != 2:
    print("Usage: python {} docker_id".format(sys.argv[9]))

docker_id = sys.argv[1]

print("Connecting to docker container")
docker_host = testinfra.get_host("docker://{}".format(docker_id))

for package in ["puppet", "puppetserver"]:
    if check_installed(docker_host, package):
        print("Package '{}' installed on basic config master".format(package))
    else:
        print("Package '{}' not installed on basic config master".format(package))

for deamon in ["rsyslog", "sshd"]:
    if check_deamon(docker_host, deamon):
        print("Deamon '{}' running on basic config master".format(deamon))
    else:
        print("Deamon '{}' not running on basic config master".format(deamon))
