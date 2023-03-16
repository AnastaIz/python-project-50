from gendiff.diff import ADDED, REMOVED, UPDATED


def modify_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{str(value)}'"


def plain(value):

    def walk(current_value, prop):
        if not isinstance(current_value, dict):
            return ''

        lines = []

        for key, val in current_value.items():
            if isinstance(val, dict) and 'type' in val:
                status = val.get('type')
                path = prop + key
                line = f"Property '{path}' was {status}"
                if status == ADDED:
                    lines.append(line +
                                 f" with value: {modify_value(val.get('value'))}")

                elif status == REMOVED:
                    lines.append(line)

                elif status == UPDATED:
                    lines.append(line + f". From {modify_value(val.get('value1'))} "
                                        f"to {modify_value(val.get('value2'))}")
                else:
                    lines.append(walk(val.get('value'), prop + key + '.'))

        return '\n'.join([line for line in lines if 'Property' in line])

    return walk(value, '')
