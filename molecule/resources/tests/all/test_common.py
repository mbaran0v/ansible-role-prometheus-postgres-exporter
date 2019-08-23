
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
version = '0.4.7'
root_dir = '/opt/postgres_exporter'
config_file = root_dir + '/shared/' + '/envs'
service_name = 'postgres_exporter'
user_name = 'postgres-exp'
group_name = user_name
socket = 'tcp://0.0.0.0:9187'


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file(root_dir)

    assert f.exists
    assert f.is_directory


def test_release_dir(host):
    f = host.file(root_dir + '/releases/' + version)

    assert f.exists
    assert f.is_directory


def test_release_symlink_dir(host):
    f = host.file(root_dir + '/current')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == root_dir + '/releases/' + version


def test_service(host):
    s = host.service(service_name)

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user(user_name)

    assert u.exists
    assert u.group == group_name
    assert u.shell == '/usr/sbin/nologin'


def test_config(host):
    f = host.file(config_file)

    assert f.exists
    assert oct(f.mode) == '0o600'


def test_socket(host):
    s = host.socket(socket)

    assert s.is_listening
