
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
version = '0.4.0'
root_dir = '/opt/alertmanager_bot'


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
    s = host.service('alertmanager_bot')

    assert s.is_enabled
    # assert s.is_running


def test_user(host):
    u = host.user('am-bot')

    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user('am-bot')

    assert g.exists


def test_default_template(host):
    f = host.file(root_dir + '/releases/' + version + '/default.tmpl')

    assert f.exists
