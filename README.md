# complex-alias


[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/patrickleweryharris/complex-alias/blob/master/LICENSE) [![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Aliases with non-deterministic arguments

Aliases are really useful, but they have certain limitations. Namely, they can't
accommodate things that change from execution to execution. These things include
commit messages, file names, specific flags, etc. This script offers a way to
create 'aliases' with more complex arguments.

## Table of Contents
- [Installation](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Install

```
$ git clone https://github.com/patrickleweryharris/complex-alias.git
$ cd complex-alias
$ ./install.sh
```

Make sure to add `~/.complex-alias` to your path

## Usage

```
$ complex-alias <name> <command> [flag]
```

Complex-alias works by creating a script under `name` that executes `command` with arguments

Let's go through an example.

Say you want to create an alias that lets you `cd` into a directory and then do `ls`.

Using complex-alias, you would do the following:

```
$ complex-alias cdl "cd %1 && ls" -e
```
Where arguments are denoted by a `%` and a number (`%` is used because `$` causes
problems in bash). The argument numbers must start from 1. The `-e` flag is used
if you want to evaluate a new shell in the alias (i.e. it runs `exec $SHELL`
after the command). This flag is useful in this case because we want to stay in
the directory that we `cd` into.

Running this command will produce a shell script called `cdl` in the `~/.complex-alias` directory
with the following contents:

```
#!/bin/bash
function execute(){
   cd $1 && ls
   exec /bin/zsh

}

execute $1
```

Where `/bin/zsh` will be replaced with whatever shell you are currently using.

Which can be called via:

```
$ cdl <dir>
```

## Contribute

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © Patrick Harris
