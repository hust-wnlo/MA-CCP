def generateTraceNames(trace):
    if trace.startswith('~'):
        trace = os.path.expanduser(trace)

    if os.path.isdir(trace):
        for trace_name in os.listdir(trace):
            yield os.path.join(trace, trace_name)
    elif os.path.isfile(trace):
        yield trace
    else:
        raise ValueError("{} is not a directory or a file".format(trace))


def generateAlgorithmTests(algorithm, cache_size, cache_size_label,
                           cache_size_label_type, window_size, trace_name, config):
    alg_config = {}
    if algorithm in config:
        keywords = list(config[algorithm])
        for values in product(*config[algorithm].values()):
            for key, value in zip(keywords, values):
                alg_config[key] = value
            yield AlgorithmTest(algorithm, cache_size, cache_size_label,
                                cache_size_label_type, window_size, trace_name, alg_config,
                                **config)
    else:
        yield AlgorithmTest(algorithm, cache_size, cache_size_label,
                            cache_size_label_type, window_size, trace_name, alg_config,
                            **config)

def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    print(directory)
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list



if __name__ == '__main__':
    import sys
    import json
    import math
    import os

    # with open(sys.argv[1], 'r') as f:
    #     config = json.loads(f.read())

    with open("example.config", 'r') as f:
        config = json.loads(f.read())

    writeSysinfo(config)

    # TODO revisit and cleanup
    if 'request_count_type' in config:
        if config['request_count_type'] == 'reuse':
            requestCounter = getReuseCount
        elif config['request_count_type'] == 'unique':
            requestCounter = getUniqueCount
        else:
            raise ValueError("Unknown request_count_type found in config")
    else:
        requestCounter = getUniqueCount

    # if config['traces'][0][-1] == "/":
    #     files = scan_files(config['traces'][0])
    # else:
    #     files = config['traces']

    if os.path.isdir(config['traces'][0]):
        files = scan_files(config['traces'][0])
    elif os.path.isfile(config['traces'][0]):
        files = config['traces']
    else:
        files = []

    for trace in files:
        for trace_name in generateTraceNames(trace):
            print()
            print(trace_name)
            if any(map(lambda x: isinstance(x, float), config['cache_sizes'])):
                count, total = requestCounter(trace_name, config) # count为总数的集合 total为所有的总数
                window_size = int(0.01*total)
            else:
                window_size = 100
            for cache_size in config['cache_sizes']:
                print()
                print("Cache ratio : " + str(cache_size))
                cache_size_label = cache_size   # 百分比 < 1
                cache_size_label_type = 'size'
                if isinstance(cache_size, float):
                    cache_size = math.floor(cache_size * count)  # 真实cache大小
                    if cache_size < 1:
                        cache_size = 1
                        print("warning: the raw cache is too samll (<1), so set cache = 1 !!!")

                    w_sum *= cache_size
                    cache_size_label_type = config['request_count_type']  # "reuse" or "unique"
                # if cache_size < 10:
                #     print(
                #         "Cache size {} too small for trace {}. Calculated size is {}. Skipping"
                #         .format(cache_size_label, trace_name, cache_size),
                #         file=sys.stderr)
                #     continue

                for algorithm in config['algorithms']:
                    for test in generateAlgorithmTests(algorithm, cache_size,
                                                       cache_size_label,
                                                       cache_size_label_type,
                                                       window_size, trace_name, config):
                        test.run(config)
    print(); print(alg_sum)
    if "output_csv" in config:
        writeAlgsumCSV(config, alg_sum)