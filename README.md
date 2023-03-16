### Hexlet tests and linter status:
[![Actions Status](https://github.com/AnastaIz/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AnastaIz/python-project-50/actions)
[![Actions Status](https://github.com/AnastaIz/python-project-50/workflows/gendiff_ci/badge.svg)](https://github.com/AnastaIz/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/8ed7ef494ebeaf32d891/maintainability)](https://codeclimate.com/github/AnastaIz/python-project-50/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/8ed7ef494ebeaf32d891/test_coverage)](https://codeclimate.com/github/AnastaIz/python-project-50/test_coverage)


## Вычислитель отличий (Generate Difference)

Вычислитель отличий - это утилита, которая сравнивает два конфигурационных файла и выводит их разницу.
Справочную информацию можно получить следующим образом:

```bash
gendiff -h
```

Для сравнения двух файлов необходимо передать пути до файлов. Утилита поддерживает файлы JSON или YAML(YML).

```bash
gendiff 'file_path1.json' 'file_path2.json'
```

Результат сравнения файлов может выводиться в разных форматах: 
* plain ("плоский"),
* json ("JSON-формат"),
* stylish (по умолчанию)

```bash
gendiff 'file_path1.yml' 'file_path2.yml' -f 'plain'
```

### Пример вывода в формате PLAIN:

[![asciicast](https://asciinema.org/a/G3YDOphQG5CtCStIlBiucY4wU.svg)](https://asciinema.org/a/G3YDOphQG5CtCStIlBiucY4wU)

### Пример вывода в формате STYLISH:

[![asciicast](https://asciinema.org/a/UMTYTauEfI3fVJ6MoM1gMdWZz.svg)](https://asciinema.org/a/UMTYTauEfI3fVJ6MoM1gMdWZz)

### Пример вывода в формате JSON:

[![asciicast](https://asciinema.org/a/EqN2iaOXfDDvlAoSBBb7u7p4W.svg)](https://asciinema.org/a/EqN2iaOXfDDvlAoSBBb7u7p4W)