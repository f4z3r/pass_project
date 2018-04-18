# pass_project
Program Analysis for System Security and Reliability project

## Usage
`taint_analysis.py` controls the execution. Its usage is the following:
```
usage: taint_analysis.py [-h] [-v | -q] [-d] {compile,run} ...

Control program to launch all actions related to this project.

positional arguments:
  {compile,run}  Commands
    compile      compile the datalog program
    run          run the datalog program

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  provide verbose output
  -q, --quiet    provide next to no output unless an error occured
  -d, --debug    provide debug information
```
Note that debug information is provided as a YAML logfile under `assets/logs/` and is not printed to console.

The `compile` command allows to compile the Datalog program into a binary executable for faster execution of larger inputs. Note that the compilation can take some time.

The `run` command takes one source file (or several) and analyses it. This will use a binary executable if present, otherwise it will run the Datalog program in an interpreter. Its precise usage is the following:
```
usage: taint_analysis.py run [-h] [-f] [-d DEST] source [source ...]

positional arguments:
  source                a list of any number of source files

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           forces to use the interpreter even if a binary exists
  -d DEST, --dest DEST  a filename where to store the results
```

If the `-d` option is given, the results are printed to the given filename instead of the console. Moreover, note that verbosity options should be provided before the `run` command.

### Note
In order to run the interpreter or to compile the Datalog program, [`souffle`](https://github.com/oracle/souffle/wiki) should be in `PATH`. If a binary is already present, this is not necessary.

## Implementation
The functionalities of the application work as follows:

1. The input source file is parsed for Datalog tokens for the language defined [here](#predicates). Note that this is not a thorough parse at it will not look for errors in the input file but simply skip over invalid input.
2. The parsed tokens from step one are formatted as tab separated values in several `.facts` input files for the main Datalog program. These files can be found under `assets/datalog/` but should not be manually modified as this can result in errors in the main analysis.
3. The main Datalog analysis program is then called (either as a native binary or as the interpreter, depending on compilation) and analyses the input given in the `.facts` files based on the rules defined in the program (`assets/datalog/taint_analyser.dl`). The output of this is printed to output files in `assets/output`.
4. The output from step three is read by python in order to beautify the output. If a destination file is provided to `run`, this will be printed to the file instead of the console.

## Datalog TODO List
1. Find technique in method sanitation for implicit and explicit dependencies.
    - Different strategies might need to be adopted for implicit and explicit dependencies.
    - Explicit dependencies seem best handled immediately before `sink()`. However, if sanitised, check that dependent variables are implicitly sanitised and don't require their own sanitation.
    - Find a way for the following snippets:
      1. ```
         x := source();
         ...
         y = op(x, 5);
         sink(y);
         ...
         sink(x);  // Only sanitation of x needed after source()
         ```
      2. ```
         x := source();
         y := source();
         z := op(x, y);
         sink(z);  // only sanitise z after operation
         ```
      3. ```
         z := source();
         y := source();
         z := op(z, y);
         sink(z);  // only sanitise z after operation
         ```
      4. ```
         x := source();
         z := op(x, 0);
         sink(z);  // can sanitise either if x is not sunk
         ```
      5. ```
         x := source();
         y := source();
         z := op(x, y);
         sink(x);
         sink(z);
         sink(y);  // only sanitise x and y, not z
         ```
    - Implicit dependencies seem best handled immediately after sourcing. However note that this might create problems for other variables that explicitly depend on this input as they are not sanitised.
2. Find out why implicit sanitation is required for code snippets similar to [the second example given](#examples).
3. Is explicit sanitation required after performing a simple operation such as `x := op(x, 5)` on an already sanitised variable `x`?
4. Implement a predicate that finds the range of `if` statements. This can probably be performed using `contains()`.
5. Make sure that if a variable depends on more than 1 unsanitised variables, only sanitise the former one if the dependencies are not used elsewhere.


---

# Project Description
## Objective
[Taint analysis](https://en.wikipedia.org/wiki/Taint_checking) consists in determining which parts of a program are dependent on the user inputs. The goal of this project is to implement a Datalog based taint analysis for a simple language.

## Problem
We are given a source code with no loops, points or floating point variables. The code contains assignments, conditionals, `op()` method (representing a binary operator) and multiple calls to  `source()` and `sink()` methods. The output of the `source()` method is controlled by the user and the call to the `sink()` method represents a sensitive region of the program. We do not want the user supplied inputs to affect its arguments.

The goal here is to first determine if the arguments to each `sink()` call are dependent on the user inputs. The argument can be dependent explicitly or implicitly on the user input. If this is the case, the call to the `sink()` method can be made secure by sanitising the argument. This is done by calling the method `sanitize()` before calling the `sink()` method.

The second goal is thus to determine the minimal number of program locations at which the argument should be sanitised.

## Examples
### 1

| __Code__ | __Predicates__ |
|-|-|
| `x := source();` | `source(l1, x)` |
| `y := op(x, z);` | `follows(l2, l1), opv(l2, y, x, z)` |
| `if(y > 0)` | `follows(l3, l2), if(l3, l4, y > 0)` |
| `y := 5;` | `follows(l4, l3), assign(l4, y, 5)` |
| `sink(y);` | `follows(l5, l4), follows(l5, l2), join(l5, l2, l4), sink(l5, y)` |

For this code, if the argument to the `sink()` method is positive, then its value is dependent on the user input `x` through the call to `op()` method. Thus, there is explicit dependence on the user input. The code can be secured against this explicit dependency by inserting a call to the `sanitise()` method before the call to `sink()`.

### 2

| __Code__ | __Predicates__ |
|-|-|
| `x := source();` | `source(l1, x)` |
| `if(x > 0)` | `follows(l2, l1), if(l2, l3, x > 0)` |
| `z := 0;` | `follows(l3, l2), assign(l3, z, 0)` |
| `else` | `follows(l4, l1), if(l4, l5, x <= 0)` |
| `z := 1;` | `follows(l5, l4), assign(l5, z, 1)` |
| `sink(z);` | `follows(l6, l5), follows(l6, l3), join(l6, l3, l5), sink(l6, z)` |

For this code, the value of argument `z` to the `sink()` method is implicitly dependent on the user input `x` which determines its exact value through the `if` statement. The code can be guarded against implicit dependency by inserting a call to `sanitise()` after the call to `source()`.

## Language
The grammar for the language is formalised below. Note that `c` is an integer constant and `x`, `y` are variables.

```
<expression>  -> c
               | x
               | opc(x, c)
               | opc(x, y)

<conditional> -> if(<expression> >= 0)
               | if(<expression> > 0)
               | if(<expression> = 0)

<assignment>  -> x := <expression>
               | x := source()

<sink>       -> sink(x)
```

## Predicates
The input code is encoded using the following Datalog predicates:

| __Predicate__ | __Meaning__ |
|-|-|
| `source(l, x)` | assign output of `source()` to variable `x` at label `l`.|
| `sink(l, x)` | call `sink()` with `x` as argument at label `l`.|
| `follows(l2, l1)` | label `l2` follows label `l1`.|
| `if(l1, l2, cond)` | if condition `cond` at label `l1` holds then label `l2` follows label `l1`.|
| `join(l1, l2, l3)` | join labels `l2` and `l3` at `l1`.|
| `opv(l, x, y, z)` | apply `op()` to variables `y` and `z` and store the result in `x` at label `l`.|
| `opc(l, x, y, c)` | apply `op()` to variable `y` and constant `c` and store the result in `x` at label `l`. |
| `assign(l, x, y)` | assign the variable/constant `y` to `x` at label `l`.|

## Input/Output
The input to the analysis is the encoding of the code using the predicates described [this](#predicates) section. The analysis should produce the list of locations and arguments at which the `sanitise()` method should be called. For example the output of `(l5, y)` and `(l2, z)` respectively will get full grades for the [two code examples](#examples).

## Framework
The taint analysis should be implemented using the [Souffle](http://souffle-lang.org/docs/home/) ([wiki](https://github.com/oracle/souffle/wiki)) Datalog framework.

## Grading
The solutions will be graded based on the following criteria:

1. The analysis should determine the locations at which the inputs should be sanitised so that there is no explicit or implicit dependency of the arguments to the `sink()` method on the user input.
2. The number of calls to the `sanitise()` method should be minimal.
