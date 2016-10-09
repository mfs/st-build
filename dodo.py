import glob
import os

GIT_URL = 'http://git.suckless.org/st'
PROJECT = 'st'

def task_clone_repo():
    return {
        'basename': 'cloning repo',
        'actions': ['git clone %s' % GIT_URL],
        'targets': [PROJECT],
        'uptodate': [True],
    }

def task_cd():
    return {
        'basename': 'entering build directory',
        'actions': [lambda: os.chdir(PROJECT)],
    }

def task_update_repo():
    return {
        'basename': 'cleaning/updating repository',
        'actions': ['git reset --hard', 'git clean -fdx', 'git pull'],
    }

def task_config():
    return {
        'basename': 'applying custom config',
        'actions': ['cp ../config.h .'],
    }

def task_apply_patches():
    return {
        'basename': 'applying patches',
        'actions': ['patch -p1 < ../%s' % f for f in glob.glob('patches/*')],
    }

def task_build():
    return {
        'basename': 'building',
        'actions': ['make'],
    }

def task_install():
    return {
        'actions': ['sudo make install'],
    }
