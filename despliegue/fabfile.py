from fabric.api import run, sudo

def deploy_wep_app():
    run('cd ~ && git clone https://github.com/ajpelaez/IV-Proyecto.git')
    run('cd IV-Proyecto && pip3 install -r requirements.txt')

def start_web_app():
    sudo('iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000')
    background_run('hug -f IV-Proyecto/FindBlaBlaCarBot/api.py')

def background_run(command):
    command = 'nohup %s &> /dev/null &' % command
    run(command, pty=False)
