"""
Contains utility functions for moderation and server settings
"""

from datetime import datetime
import json
import discord


def log(user='nAn', channel='nAn', server='nAn', content='nAn'):
    """Print logs with username, channel and content"""
    date = str(datetime.now())
    print('[{} by {} in {} from {}] {}'.format(date, user, channel, server, content))


def write_settings(server, default_role='nAn'):
    """Writes server settings to json files"""

    new_settings = {}
    new_settings[str(server.id)] = []
    new_settings[str(server.id)].append({
        'server_name': server.name,
        'default_role': default_role
    })

    with open('data/servers.json') as f:
        settings = json.load(f)

    settings.update(new_settings)

    with open('data/servers.json', 'w') as f:
        json.dump(settings, f, indent=4)
    

def read_settings(server_id, id='nAn'):
    """Returns data from json file"""
    data = []
    
    with open('data/servers.json') as f:
        settings = json.load(f)
        for p in settings[str(server_id)]:
            data = p[id]

    return data