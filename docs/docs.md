# Guide to contributing

This is the guide to contributing, and please read it if you want to contribute.

## How to fork repo:

This is the guide to fork the repo, first, **click the fork button**, and know, you may need 
git here, but here's the command: 

```bash
$ git clone <link>
```

And add some change and now type:

```bash
git add .
git commit -m "<message>"
git push
```

And now, **send the PR**!

## Tools you need:
 * Python (and tools like numpy)
 * C programming language
 * Make for compiling code (or if you're on Windows skip this as you have `build.ps1`)
 * GDB (or debugging tools) to debug code
 * Git because of obvious reason

## Changes? Bugs?
Please **send the PR**, and also please send what you have changed and 
the code should be legitament and **no ransomware or virus**.

## How to compile?
To compile the code on Linux, you may need to do some changes, and then
next, type:

```bash
$ make
```

And you can run it by typing:

```bash
$ make run
```

or 

```bash
$ ./code.py
```

But for Windows users, you can just do some change, and save it, then type:

```bash
./build.ps1
```

## Rules:
While it's open-source and you can do `"anything"`, you have some rules to follow, 
but you also must **follow the LICENSE**. But hwere's the other rules in this repo:
 * No swearing or making fun of others
 * Don't add ransomware or viruses in here

## JSON changes
If you want to modify the JSON in the code, you may but you must
know what data is. Becuase JSON don't support comments but only data, 
I may need to do this way.

But here's the graph:
| Data function | What they do | unit |
| ----- | --- | --- |
| "time_stamp" | How much time will pass | decimal accepted |
| "step_max" | How much step we'll count to | only integer |
| "position" | What is the current posititon | decimal accepted |
| "velocity" | What is the velocity | decimal accepted |
| "mu" | gravitational parameter | decimal accepted |

And now you can contribute!