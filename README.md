# Programming Assignment 1 (Matching and Verifying)

## Authors
- Goran Not, UFID: 71994424
- Jack Lohse, UFID: 

## Files
- 'main.py' => Reads input file using util.py functions and calls gale_shapely algorithm
- 'util.py' => Parses and converts input file into desired format to be passed into G-S algorithm
-'src/matching/algorithm.py' => Contains the implementation of G-S algorithm 
-'src/verify/verifier.py' => Performs Validity + Stability checks

## Requirements/Dependencies
- Minimum Python 3.9+ ('dict[int,int]' type hints used)
- No dependencies (standard python library only)

## Required Input Format
- First line: integer 'n'
- Next 'n' lines: Hospital preference lists
- Next 'n' lines: Student preference lists

## Output Format
- Output 'n' lines, one per hospital 'i'
- i j , meaning hospital i is matched to student j
- The verifier prints whether matching is valid and stable, or reason for invalidity/blocking pair causing unstable matching.

## How to Run (Matcher)
Example: (using terminal or Bash)
- py main.py tests/example.in > output.txt
- if 'py' does not work on your system, use 'python' or 'python3'

## Task C Solution and Graph
