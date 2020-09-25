import os
import click
import subprocess
from pathlib import Path

class Docker(object):

    def __init__(self,dry_run,*args,**kwargs):
        self.dry_run = dry_run

    def _output(self,args):
        if not self.dry_run:
            subprocess.run(args)
        else:
            print(args)

    def run(self):
        docker_command = ['docker','run','-v','/dev/arena:/dev/arena','--rm']
        devs = sorted(Path('/dev').glob('ttyACM*'))
        devs_command = ['--device={0}:{0}'.format(dev) for dev in devs]
        docker_command.extend(devs_command)
        docker_command.append('yarenavalvecontroller:0.1.0')
        self._output(docker_command)

@click.command()
@click.option('-d','--dry-run', is_flag=True)
def cli(dry_run):
    if dry_run:
        print('Dry Run')
    docker = Docker(dry_run)
    docker.run()

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    cli()
