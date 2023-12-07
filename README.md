# Learn To Code Sustainably: Experiments

This repository contains the collection of code samples generated during the evaluation phase of our green coding review.

**This project is based on a collaboration between [TWT GmbH Science & Innovation](https://twt-innovation.de/en/) and Mercedes-Benz and contributors from National Technical University of Athens, Massachusetts Institute of Technology, and Harvard University.**

The paper also presents a methodology and metric to score the "greenness" of a code generation tool called the **green capacity**.
We evaluated and compared the green capacity of [ChatGPT](https://openai.com/chatgpt), [GitHub Copilot](https://github.com/features/copilot), and [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/).

For this preliminary evaluation, we selected 6 different tasks from [LeetCode](https://leetcode.com/):
* [3Sum](https://leetcode.com/problems/3sum)
* [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
* [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
* [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [Sort List](https://leetcode.com/problems/sort-list/)

The repository is structured as follows:
```
└── Experiment Name
    ├── Tool 1
    │   ├── Default Variant
    │   ├── Default Variant set up for memory evaluation
    │   ├── Runtime Optimized Variant
    │   ├── Memory Optimized Variant
    │   ├── FLOPs Optimized Variant
    │   └── Energy Consumption Optimized Variant
    ├── Tool 2
    │   ├── Default Variant
    ⋮   ⋮
    ⋮   ⋮
```

## Overview Valid Solutions

|                             | User               | ChatGPT            |                    |                    |                    |                    | Copilot            |                    |                    |                    |                    | CodeWhisperer      |                    |                    |                    |                    |
|-----------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| Problem                     |                    | initial            | runtime            | memory             | FLOPs              | energy             | initial            | runtime            | memory             | FLOPs              | energy             | initial            | runtime            | memory             | FLOPs              | energy             |
|                             |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |
| 3Sum                        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Assign Cookies              | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Median of two sorted arrays | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :heavy_check_mark: | :heavy_check_mark: |
| Network Delay Time          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Search Insert Position      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Sort List                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

**Note:** FLOPs means the total amount of floating point operations performed during the execution. This **not** to be confused with "floating-point operations per second".

## Evaluation

### 1. Energy Consumption & Runtime

We measured the energy consumption using [perf-stat](https://www.man7.org/linux/man-pages/man1/perf-stat.1.html) with the `power/energy-pkg/` event. The command looked like the following:

```
sudo perf stat -e power/energy-pkg/ -a -r 10 python3 -X perf ./cookies/ChatGPT/01_default.py
```

This command also outputs the **runtime** the execution took.

### 2. Count of Floating Point Operations

To measure the total number of floating point operations the code needs to finish execution, we used again [perf-stat](https://www.man7.org/linux/man-pages/man1/perf-stat.1.html), but this time with the following events only:
* fp_arith_inst_retired.scalar_single
* fp_arith_inst_retired.scalar_double

```
sudo perf stat -e fp_arith_inst_retired.scalar_single,fp_arith_inst_retired.scalar_double python3 -X perf ./cookies/ChatGPT/01_default.py
```

### 3. Peak Memory Usage

To measure the peak memory usage, we used the Python module [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html).
To use it, we imported the package at the very start of each file, and started the tracker.

```python
import tracemalloc
tracemalloc.start()
```

At the end of the file, after the generated code finished execution, we saved the peak value from the tracker:

```python
curr, peak = tracemalloc.get_traced_memory()
```

## Prerequisites

* Linux with `perf` installed (we used Linux Mint 21.2 Cinnamon with kernel version 5.17.0-79-generic & `perf` version 5.15.111)
* Python 3 (we used Python 3.12.0rc1)

## Quick Start

To quickly start the evaluation, the four shell scripts can be used.

For example, to run the evaluation of the energy consumption, simply execute the `evaluate-energy-consumption.sh` script.
Each script runs the initial implementation by each tool for each of the problems and prints the results.

By default, in each of the files, the "single run" is set up meaning that each of the functions is called **without** iterations.

To run the long versions, in each of the files, the commented out code section at the end of each file (`for`-loop) must be uncommented.
Then, the scripts can again be used to run the evaluations.

## Acknowledgements

The work on this paper inspired a development project between Mercedes-Benz and TWT. 
The main authors of the paper related to this repository are Tina Vartziotis, Ippolyti Dellatolas, George Dasoulas, Maximilian Schmidt, Florian Schneider, Tim Hoffmann, Sotirios Kotsopoulos, Jan Brecht, Michael Keckeisen.

We express our gratitude to Raphaela Löbel from TWT, Maria Stasinou from NIKI Ltd Digital Engineering, and Viet Dung Le from Mercedes-Benz for their engaging and informative discussions, which significantly influenced the project’s scope.
