# type markers:
ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'


def diff(data1, data2):
    result = {}
    for key in sorted(data1.keys() | data2.keys()):
        item = {}
        if key not in data2:
            item['type'] = REMOVED
            item['value'] = data1[key]
        elif key not in data1:
            item['type'] = ADDED
            item['value'] = data2[key]
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                item['type'] = NESTED
                item['value'] = diff(data1[key], data2[key])
            elif data1[key] == data2[key]:
                item['type'] = UNCHANGED
                item['value'] = data1[key]
            else:
                item['type'] = UPDATED
                item['value1'] = data1[key]
                item['value2'] = data2[key]
        result[key] = item
    return result
