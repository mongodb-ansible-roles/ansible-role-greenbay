import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ppc64le(host):
    cmd = host.run("uname -m")
    assert cmd.stdout == "ppc64le\n"


def test_greenbay_in_path(host):
    assert host.exists("greenbay")
    cmd = host.run("greenbay --version")
    assert cmd.stdout == "greenbay version 0.0.1-pre\n"
