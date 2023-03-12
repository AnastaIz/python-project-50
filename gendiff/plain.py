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
                if val['type'] == ADDED:
                    lines.append(
                        f"Property '{prop + key}' was {ADDED} "
                        f"with value: {modify_value(val['value'])}"
                    )

                elif val['type'] == REMOVED:
                    lines.append(
                        f"Property '{prop + key}' was {REMOVED}"
                    )

                elif val['type'] == UPDATED:
                    lines.append(
                        f"Property '{prop + key}' was {UPDATED}. "
                        f"From {modify_value(val['value1'])} "
                        f"to {modify_value(val['value2'])}"
                    )
                else:
                    lines.append(walk(val['value'], prop + key + '.'))

        return '\n'.join([line for line in lines if 'Property' in line])

    return walk(value, '')
