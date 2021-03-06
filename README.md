# CS263_Performance_Comparisons

## Language Benchmarks
* pidigits :Streaming arbitrary-precision arithmetic
* binary-trees: Allocate and deallocate many many binary trees
* n-body: Double-precision N-body simulation
* fasta: generate DNA sequences
* reverse-complement: write DNA reverse complement
* sudoku: solving 20 extremely hard Sudokus repeated 50 times
* matmul: multiplying two 100x1000 matrices 
* patmch: finding lines matching a complex regexp

## Project Plan
| Week          | Description           | 
| :----: | -------------|
| Week 3 (Jan.19 ~ Jan.25)      | Implement two algorithms: pidigits and binary-trees in Javascript, Ruby and Python. Estimate their performance in several aspects. |
| Week 4 (Jan.26 ~ Feb.1)      | Implement three algorithms: n-body, reverse-complement and k-nucleotide. Estimate their performance in several aspects.      | 
| Week 5 (Feb.2 ~ Feb.8) | Explore and find two algorithms in cryptographic engineering and estimate their performance      |
| Week 6 (Feb.9 ~ Feb.15) | Implement Sudoku solving n different programming language. Estimate their performance.      |
| Week 7 (Feb.16 ~ Feb.22) | Implement Pattern Matching and Matrix multiplication in different programming language. Estimate their performance.    |
| Week 8 (Feb.23 ~ Mar.1) | Estimate and validate how much the use of languages we choose cost when run using different instance sizes on cloud infrastructures, e.g. AWS and Azure   |

## Test Environments 
* Benchmark machine:<br />
CPU: Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz<br />
  Memory: 8GB<br />
  OS: Ubuntu 14.04 LTS VM<br />
* Interpreters:<br />
  Python--Cpython 3.4.3<br />
  Ruby--CRuby/YARV 2.5<br />
  JS--SpiderMonkey 52<br />
* Benchmarking & evaluation tools: <br />
  Ruby: benchmark, get_process_mem<br />
  Python: psutil, time, subprocess<br />
  Javascript: js-shell <br />
  mem, psutil & time, subprocess & js-shell<br />
* Profilers (tracing):  <br />
  ruby-prof; cProfiler<br />


## Hoow To Run
For every program, we enable the user input. To run the program, type python3 / ruby / js, plus script name and input value.
We put pigits here to illustrate how to run, other scripts are almost same.
* Python
```
Python3 pidigits.py 5000
```
* Ruby
```
ruby pidigits.rb 5000
```
* Javascript
```
js pidigits.js 5000
```


## Performance
* pidigits

| Argv | Execution Time(sec) | Memory(bytes) |
| :---: | :----: | :-------: |
| 500 | 0.0107309818267822  | 9805824  |
|1000 | 0.0260009765625     | 9777152 |
|5000 | 0.3612260818481445  | 10780672 |
|10000| 1.3939342498779297  | 12271616 |
|50000| NA | NA|


* matmul

| Argv | Execution Time(sec) | Memory(bytes) |
| :---: | :----: | :-------: |
| 100 | 0.11944198608398438  | 10096640  |
| 500 | 13.7977900505065925     | 19955712 |
|1000 |   107.124666929245   |  46149632  |

## Reference
1. [The Computer Language Benchmark Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)
2. [Programming Language Benchmarks](https://attractivechaos.github.io/plb/)
3. [Language Benchmark](http://www.bioinformatics.org/benchmark/)
4. [SJCL Crypto for Py & Js](https://github.com/berlincode/sjcl)
5. [SCEE encryption for py, js and rb](https://github.com/luke-park/SecureCompatibleEncryptionExamples)
6. [Profilers](https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-/)
## Paper
1. [NA](http://delivery.acm.org/10.1145/2740000/2738614/p103-rohou.pdf?ip=169.231.54.24&id=2738614&acc=ACTIVE%20SERVICE&key=CA367851C7E3CE77%2E022A0CC51A76093F%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1551066458_a6dbeef3b3303d0c99121ee80fa1c85e)
2. [A Comprehensive Evaluation of Common Python Implementations](https://ieeexplore.ieee.org/abstract/document/6879048)
3. [Performance Comparison and Evaluation of Web Development Technologies](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7023652&tag=1)
4. [A comparison of object oriented scripting languages: Python and Ruby](http://115.78.133.167:81/bitstream/TVHG_07113876976/1517/1/idoc.vn_a-comparison-of-object-oriented-scripting-languages-python-and-ruby.pdf)
5. [Benchmark may mislead Javascript Engineer](https://www.microsoft.com/en-us/research/publication/jsmeter-characterizing-real-world-behavior-of-javascript-programs/)
6. [Ruby, JS, Python](https://stackoverflow.com/questions/5168718/what-blocks-ruby-python-to-get-javascript-v8-speed)


