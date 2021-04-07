# loglog
Documentation and abstractions for adding logs to av-centric scripts

## What is loglog?
Loglog is a meta-documentation project meant to help developers add logging functions to their scripts. Provided in the repository are a template scripts that provide examples of how to use and implement logs in various scripting languages. There are also scripts that have minor utility that are meant to serve as examples as of how scripting can be used advantageously.

## Template scripts

## logscript.sh
This is a template that can be used to implement logging in Bash. There are a series of functions defined in `bash_logging.config`. Here are functions

* `logCreate`: This initializes the log. It must be called before any of the following functions will work.
* `logOpen`: This opens the log using the native OS's preferred application.
* `logNewLine`: This adds a new line to the log, including a timestamp
* `logAddLine`: This appends to the last line in the log, not adding any timestamps
* `logLog`: This eponymous function logs how long it takes for a specific function to fun.
* `logOut`: When placed in a script this function redirects the stdout and the stderr to the log. They are not printed to console

## logscript.py
This is a template that can be used to implement logging in Python 3
