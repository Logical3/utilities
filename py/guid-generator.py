import uuid
import random
import argparse

def random_hex(length):
    """
    Generate a random string of hexadecimal characters
    :param length: the number of random characters the result should be comprised of
    :return: a random hexadecimal string
    """
    return ''.join([random.choice('0123456789ABCDEF') for x in range(length)])

def generate_uber_trace_id():
    """
    Generate a tuple with [uber-trace-id, trace-id, root-span-id]
    :param sampled: whether the trace should be sampled or not
    :return: a tuple containing the otel ids included in all requests
    """
    # See https://www.jaegertracing.io/docs/1.33/client-libraries/#tracespan-identity for format
    trace_id = random_hex(24)
    root_span_id = random_hex(24)
    root_span = '0' # Means that this is the root span 
    is_sampled = '1' # Means that this trace needs to be sampled
    uber_trace_id = '{}:{}:{}:{}'.format(trace_id, root_span_id, root_span, is_sampled)
    print(uber_trace_id)

def decode(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Decode the bytes using base64
    decoded_bytes = base64.b64decode(input_bytes)

    # Convert the decoded bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')

    return decoded_string

def lowercase_choice(value):
    """
    Custom type for argparse that converts the value to lowercase
    """
    return value.lower()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Base64 encode/decode a string')
    parser.add_argument('-t', '--type', type=lowercase_choice, choices=['guid','uber'], default='guid', help='Pass the type of guid to be generated')
    args = parser.parse_args()

    if args.type.lower() == 'guid':
        print(uuid.uuid4())
    elif args.type.lower() == 'uber':
        generate_uber_trace_id()
    else:
        print("I don't know what to do now. ")