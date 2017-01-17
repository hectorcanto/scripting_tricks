# Usage

Copy the configure_log to your repository to use it as you please

# Test

Execute the following command:

```
python example.py
```

You should see the logs on your terminal.

# Improvements

## Log level

You may have different levels for each part of your code. My recommendation is that you
 configure each package independently. Use a external file or files for this.

## Format
Change the formatter as you wish, you can use YMAL, JSON, INI files, or do it directly
as in the example. Check the documentation for more information:

https://docs.python.org/2/library/logging.html#logrecord-attributes