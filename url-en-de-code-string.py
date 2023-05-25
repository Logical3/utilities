import urllib.parse
import json
import sys
import argparse

parser = argparse.ArgumentParser(description='URL encode or decode a string')
parser.add_argument('input_string', nargs='?', help='The string to encode or decode')
parser.add_argument('--encode', '-e', action='store_true', help='Encode the input string')
parser.add_argument('--decode', '-d', action='store_true', help='Decode the input string')
parser.add_argument('--url', '-u', action='store_true', help='Specify whether the input string is a url')
args = parser.parse_args()

if args.decode:
    # Extract the query parameters from the URL if it's a URL
    if args.url:
        url_components = urllib.parse.urlparse(args.input_string)
        print("\n##### URL breakdown #####\n")
        print("Scheme:", url_components.scheme)
        print("Netloc:", url_components.netloc)
        print("Path:", url_components.path)
        print("Params:", url_components.params)
        encoded_query = url_components.query
        decoded_query = urllib.parse.unquote(encoded_query)
        query_params = urllib.parse.parse_qs(decoded_query)
        # Convert query params to a dictionary for prettifying
        query_dict = {k: v[0] for k, v in query_params.items()}
        print("Query Params:")
        print(json.dumps(query_dict, indent=4))
        print("Fragment:", url_components.fragment)

    # Decode the URL encoded string
    # print("Input string is: "+input_string)
    decoded_string = urllib.parse.unquote(args.input_string)

    # Check if the decoded string is a valid JSON string
    try:
        json_object = json.loads(decoded_string)
    except ValueError:
        json_object = None

    # Print the decoded string, prettified if it's a JSON string
    print("\n##### Decoded output ##### \n")
    if json_object:
        print(json.dumps(json_object, indent=4))
    else:
        print(decoded_string)
elif args.encode:
    # Parse the input string to check if it's a URL
    parsed_url = urllib.parse.urlparse(args.input_string)

    if parsed_url.scheme and parsed_url.netloc:
        # Encode the query parameters of the URL
        query_params = urllib.parse.parse_qs(parsed_url.query)
        for key in query_params:
            query_params[key] = [urllib.parse.quote(param, safe='') for param in query_params[key]]
        encoded_query = urllib.parse.urlencode(query_params, doseq=True)
        encoded_url = urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, encoded_query, parsed_url.fragment))
        print(encoded_url)
    else:
        # Encode the entire string
        print(urllib.parse.quote(args.input_string, safe=''))
else: 
    print("What should i do now? ")