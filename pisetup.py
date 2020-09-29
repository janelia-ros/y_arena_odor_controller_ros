import os
import click
import subprocess
from pathlib import Path

class Docker(object):

    def __init__(self,dry_run,*args,**kwargs):
        self.dry_run = dry_run
        self.path = Path('etc')

    def _output(self,args):
        print(" ".join(args))
        if not self.dry_run:
            subprocess.run(args)

    def install(self):
        for child in self.path.rglob('*'):
            if child.is_file():
                cmd = ['sudo', 'cp', str(child), str('/' / child)]
                self._output(cmd)

    def uninstall(self):
        for child in self.path.rglob('*'):
            if child.is_file():
                cmd = ['sudo', 'rm', str('/' / child)]
                self._output(cmd)

@click.group()
@click.option('-d','--dry-run', is_flag=True)
@click.pass_context
def cli(ctx,dry_run):
    if dry_run:
        click.echo('Dry Run')

    docker = Docker(dry_run)

    ctx.ensure_object(dict)
    ctx.obj['DOCKER'] = docker

@cli.command()
@click.pass_context
def install(ctx):
    click.echo('Installing')
    ctx.obj['DOCKER'].install()

@cli.command()
@click.pass_context
def uninstall(ctx):
    click.echo('Uninstalling')
    ctx.obj['DOCKER'].uninstall()

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    cli(obj={})
