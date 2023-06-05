def get_statistics(input_list):
    # Write your code here.
    hash_map =  {
        "mean": 0,
        "median": 0,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0],
    }

    hash_map['mean'] = sum(input_list) / len(input_list)

    sorted_values = sorted(input_list)

    if len(sorted_values) % 2 == 0:

        hash_map['median'] = (sorted_values[len(input_list) // 2] + sorted_values[(len(input_list) // 2) - 1]) / 2
    else:
        hash_map['median'] = (sorted_values[len(input_list) // 2])

    count = dict()

    for i in input_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    hash_map['mode'] = 1. * max(count, key = count.get)
    
    std  = 0
    mean = hash_map['mean']
    for value in input_list:
        std += (value - mean) ** 2
    hash_map['sample_standard_deviation'] = (std / (len(input_list) - 1)) ** .5
    hash_map['sample_variance'] = hash_map['sample_standard_deviation'] ** 2

    c = 1.96
    temp = c * (hash_map['sample_standard_deviation'] / (len(input_list) ** .5))
    hash_map['mean_confidence_interval'] = [hash_map['mean'] - temp, hash_map['mean'] + temp]
    
    return hash_map
