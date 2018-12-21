
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file('/opt/postgres_exporter')

    assert f.exists
    assert f.is_directory


def test_config_file(host):
    f = host.file('/opt/postgres_exporter/shared/envs')

    assert f.exists
    assert f.is_file


def test_release_dir(host):
    f = host.file('/opt/postgres_exporter/releases/0.4.7')

    assert f.exists
    assert f.is_directory


def test_release_symlink_dir(host):
    f = host.file('/opt/postgres_exporter/current')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == '/opt/postgres_exporter/releases/0.4.7'


def test_service(host):
    s = host.service('postgres_exporter')

    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket('tcp://0.0.0.0:9187')

    assert s.is_listening


def test_user(host):
    u = host.user('postgres-exp')

    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user('postgres-exp')

    assert g.exists
