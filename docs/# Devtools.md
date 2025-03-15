# Devtools

## New tool

```lua
import_code("devtools")

mytool = Tool.New(toolname, version)
mytool.short_description = ""
mytool.long_description = ""

. . .
commands
. . .

mytool.init()

```
toolname is a string, version is any version, you can use any string, but rrecommended to use `x.x.x`

short and long descriptions are just what the tool is

`mytool.init()` is required at the end of the file, **AFTER** all commands have been made for it to register inside of crowsploit.

## New command

### Arguments

There's a few different argument types within crowsploit:

- Arg
- OptionalArg
- Kwarg
- Rest

All of the above can have the following data types:

- string
- bool
- float
- int
- ip

(These will be automatically handled and parsed by crowsploit, so you dn't have to worry about getting the correct datatype)

**Arg**

An arg is just a normal required argument.

```lua
Arg.New(name, type)
```

example:

```lua
Arg.New("count", "int")
```

All arguments (arg, optionalarg, and kwarg) have the ability to add a little description to them.
That is done with the following:

```lua
Arg.New(... ...).Info("Little description")
```

This works for all upcomming arguments too

**Optional Arg**

These are arguments but you are not required to provide them when running the command.

```lua
OptionalArg.New("name", "type")
```

Since this is optional, you can assign a default value
(Note, this default needs to fit the datatype provided as well)


```lua
OptionalArg.New("count", "int").Default(10)
```

**Kwarg**

These are optional arguments, only changable using `--` arguments.
(like `--limit` in the `history` command)

```lua
Kwarg.New("name","type")
```

Unlike the `Arg`, `Kwarg` can have an alias.
This just means it has a small shortcut for the same result
(like `-l` for `--limit` in `history` command)

This is easily setup like:

```lua
Kwarg.New("limit", "int").Alias("l")
```

And since it's an optional argument, you can also set a default value

```lua
Kwarg.New("limit","int").Alias("l").Default(10)
```

**RestArg**

This is an argument that shouldd come at the very end.
It's an overflow argument.

```lua
RestArg.New()
```

It takes no info, no name, no type.
It will always be a list of strings

### Command handling

All commands need to follow the following format:

```lua
function (arg)
```

All crowsploit command-functions have one argument.
This argument is a map and it has all the arguments as values.

It also has a `kernel` index by default, which is THE crowsploit kernel.

### Command types

- Main command
- Tool command
- Standalone command

### Main Command

Main command is a command that's run when the user only types in the tool name
For example, if you create a tool called `test`, you can run the `main`command by only running `test` in the crowsploit terminal

```lua
testtool = Tool.New("test", "1.0.0")

main_args= []
main_func = function(a)
  print("Test run")
end function

main_cmd = testtool.main_command(main_args, @main_func)
```

### Tool command

This will be the most used command when creating tools.
This *only* runs if the tool is prefixed before the command.

For example, for the tool `test` and command `hello`, you can run the `hello` command using `test hello`

```lua
testtool = Tool.New("test", "1.0.0")

hello_args = []
hello_func = function(a)
  print("Hello there!")
end function

hello_cmd = testtool.command("hello", hello_args, @hello_func)
```

### Standalone command

This command can be run without any references to the tool its from in the command itself
it's as its called, standalone

for example, for the tool `test` and the command `hello` you can run the `hello` command by using `hello` in the crowsploit interface

```lua
testtool = Tool.New("test", "1.0.0")

hello_args = []
hello_func = function(a)
  print("Hello there!")
end function

hello_cmd = testtool.standalone_command("hello", hello_args, @hello_func)
```