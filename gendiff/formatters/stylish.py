import itertools
from gendiff.diff import ADDED, REMOVED, UPDATED

# symbols for view
PLUS_SYMBOL = '+ '
MINUS_SYMBOL = '- '


def to_string(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return to_string(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        deep_indent_with_symbol = replacer * (deep_indent_size - len(PLUS_SYMBOL))
        current_indent = replacer * depth

        lines = []

        for key, val in current_value.items():
            if isinstance(val, dict) and 'type' in val:
                if val['type'] == ADDED:
                    lines.append(f"{deep_indent_with_symbol}{PLUS_SYMBOL}"
                                 f"{key}: {iter_(val['value'], deep_indent_size)}")

                elif val['type'] == REMOVED:
                    lines.append(f"{deep_indent_with_symbol}{MINUS_SYMBOL}"
                                 f"{key}: {iter_(val['value'], deep_indent_size)}")

                elif val['type'] == UPDATED:
                    lines.append(f"{deep_indent_with_symbol}{MINUS_SYMBOL}"
                                 f"{key}: {iter_(val['value1'], deep_indent_size)}")
                    lines.append(f"{deep_indent_with_symbol}{PLUS_SYMBOL}"
                                 f"{key}: {iter_(val['value2'], deep_indent_size)}")
                else:
                    lines.append(f"{deep_indent}{key}: "
                                 f"{iter_(val['value'], deep_indent_size)}")
            else:
                lines.append(f"{deep_indent}{key}: "
                             f"{iter_(val, deep_indent_size)}")
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
