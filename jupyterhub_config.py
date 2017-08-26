# Configuration file for Jupyter Hub

c = get_config()

c.JupyterHub.log_level = 10
from oauthenticator.github import GitHubOAuthenticator
import os
import sys

c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.LocalGitHubOAuthenticator.create_system_users = True
c.JupyterHub.admin_access = True
c.JupyterHub.confirm_no_ssl = True
join = os.path.join

here = os.path.dirname(__file__)
root = os.environ.get('OAUTHENTICATOR_DIR', here)
sys.path.insert(0, root)
os.environ["DOCKER_HOST"] = ":4000"#
os.environ["OAUTH_CALLBACK_URL"]="http://34.233.164.104:8443/hub/oauth_callback"
os.environ["GITHUB_CLIENT_ID"]="c56448afbf92f173c5ba"
os.environ["GITHUB_CLIENT_SECRET"]="09d4d6c9025e884cfe98978ac637c69db27c9e56"
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.LocalAuthenticator.create_system_users = True
# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'
c.LocalAuthenticator.create_system_users = True
# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.DockerSpawner.container_image = 'mycustom'
#c.DockerSpawner.container_image = 'jupyterhub/singleuser:0.7'

#c.JupyterHub.spawner_class = 'cassinyspawner.SwarmSpawner'
c.JupyterHub.cleanup_servers = False
c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.DockerSpawner.container_ip = '0.0.0.0'
c.DockerSpawner.use_internal_ip = False
c.DockerSpawner.hub_ip_connect = c.JupyterHub.hub_ip
c.DockerSpawner.extra_host_config = {'mem_limit': '1g'}

c.DockerSpawner.volumes = {'/user-directories/{username}': '/home/ubuntu'} 
c.Spawner.mem_limit = '4G'
c.DockerSpawner.debug = True

