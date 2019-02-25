# CS263_Performance_Comparisons

## Language Benchmarks
* pidigits :Streaming arbitrary-precision arithmetic
* binary-trees: Allocate and deallocate many many binary trees
* n-body: Double-precision N-body simulation
* reverse-complement: write DNA reverse complement
* k-nucleotide: Hashtable update and k-nucleotide strings
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

## Paper
1.[Hello](http://delivery.acm.org/10.1145/2740000/2738614/p103-rohou.pdf?ip=169.231.54.24&id=2738614&acc=ACTIVE%20SERVICE&key=CA367851C7E3CE77%2E022A0CC51A76093F%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1551066458_a6dbeef3b3303d0c99121ee80fa1c85e)

2.[A Comprehensive Evaluation of Common Python Implementations](https://ieeexplore.ieee.org/abstract/document/6879048)

3.[Performance Comparison and Evaluation of Web Development Technologies](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7023652&tag=1)

4.


