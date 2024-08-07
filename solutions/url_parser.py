# To test the script use: 
# python url_parser.py '/:version/api/:collection/:id' '/6/api/listings/3?sort=desc&limit=10'

import argparse
from urllib.parse import parse_qs, urlparse

def parse_url(url_format, url_instance):
    # Split the URL format
    format_parts = url_format.strip('/').split('/')
    url_parts = url_instance.split('?')[0].strip('/').split('/')
    
    # Extract variables
    variables = {}
    for f, u in zip(format_parts, url_parts):
        if f.startswith(':'):
            variables[f[1:]] = u
    
    # Parse parameters
    query_params = parse_qs(urlparse(url_instance).query)
    for key, value in query_params.items():
        variables[key] = value[0]
    
    return variables

parser = argparse.ArgumentParser()
parser.add_argument('url_format', type=str)
parser.add_argument('url_instance', type=str)
result = parse_url(parser.parse_args().url_format, parser.parse_args().url_instance)
print(result)
