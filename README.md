# Conversion Script for Pelican to Camel

This tool copies the files from a source directory to a destination directory, and nests them under the kind of hierarchy [Camel](https://github.com/cliss/camel) expects. By default, it will overwrite any conflicting files in the nested subdirectories. This also converts file the MultiMarkdown Metadata that Pelican uses to the '@@' prefixed metadata.

## Example usage:

`./pelicamel.py --s ./output --d ./posts`

## Example help:

```
usage: pelicamel.py [-h] [-s SOURCE] [-d DESTINATION]

Process a directory of Pelican-style Markdown and create Camel-style nested
directories.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source directory containing Pelican-style *.md files.
  -d DESTINATION, --destination DESTINATION
                        Root directory to create subdirectories and files it.
```