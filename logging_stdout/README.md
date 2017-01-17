# Usage

Copy the configure_log to your repository to use it as you please.

## Script development strategy

Instead of populating your code with _prints _that you \[should]\ delete afterwards,
use plain logs. This way you decide when to show debugging information through the
 log configuration.

If you divide your script in several files \[packages]\ you can set different log levels
 for each using the . This way, as you develop and test, you will be only bothered with the logs
 of the code you are creating at that moment.

_Note_:- You really should divide if the scripts starts to grow. A typical approach
 for a simple script is having the input parameter logic in one file, the core in another
 and the auxiliary code in another. And have tests!


# Test

Execute the following command:

```
python example.py
```

You should see the logs on your terminal.

# Improvements and recommendations

## Log level

You may have different levels for each part of your code. My recommendation is that you
 configure each package independently. Use a external file or files for this.

## Format
Change the formatter as you wish, you can use YMAL, JSON, INI files, or do it directly
as in the example. Check the documentation for more information:

https://docs.python.org/2/library/logging.html#logrecord-attributes