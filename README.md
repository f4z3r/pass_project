# pass_project
Program Analysis for System Security and Reliability project

## Objective
[Taint analysis](https://en.wikipedia.org/wiki/Taint_checking) consists in determining which parts of a program are dependent on the user inputs. The goal of this project is to implement a Datalog based taint analysis for a simple language.

## Problem
We are given a source code with no loops, points or floating point variables. The code contains assignments, conditionals, `op()` method (representing a binary operator) and multiple calls to  `source()` and `sink()` methods. The output of the `source()` method is controller by the user and the call to the `sink()` method represents a sensitive region of the program. We do not want the user supplied inputs to affect its arguments.

The goal here is to first determine if the arguments to each `sink()` call are dependent on the user inputs. The argument can be dependent explicitly or implicitly on the user input. If this is the case, the call to the `sink()` method can be made secure by sanitising the argument. This is done by calling the method `sanitize()` before calling the `sink()` method.

The second goal is thus to determine the minimal number of program locations at which the argument should be sanitised.

## Examples
### 1

| __Code__ | __Predicates__ |
|-|-|
| `x := source();` | `source(l1, x)` |
| `y := op(x, z);` | `follows(l2, l1), opv(l2, x, z)` |
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
| `z := 1;` | `follow(l5, l4), assign(l5, z, 1)` |
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
