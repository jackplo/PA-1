# Programming Assignment 1 (Matching and Verifying)

## Authors

- Goran Not, UFID: 71994424
- Jack Lohse, UFID: 70686167

## Files

- 'test.py' => Entry point, calls verifier or matcher and generate the plots
- 'util.py' => Parses and converts input file into desired format to be passed into G-S algorithm
- 'src/matching/algorithm.py' => Contains the implementation of G-S algorithm
- 'src/verify/verifier.py' => Performs Validity + Stability checks
- 'src/graph/grapher.py' => Utiliy functions for graphing with matplotlib
- '/prefs' => The directory containing the preference list inputs for both hospitals and students, with all files named with {'n'.txt}.
- '/matches' => The directory containing the output to the respective preference list input with the same naming convention as the file in /prefs

## Requirements/Dependencies

- Minimum Python >= 3.12 ('dict[int,int]' type hints used)
- Python package manager uv
- Matplotlib

## How to run

Clone the repo with:

```bash
git clone git@github.com:jackplo/PA-1.git
```

This project utilizes UV to make project management and package installation easier. This project can still be run without using uv, but it is highly recommended to use uv as it makes the process much easier. We outline the procedure for both methods below.

**If using uv:**

Install the python uv package manager if you do not have it. Below are the commands for mac, window, and linux. Alternatively visit the [uv repo](https://github.com/astral-sh/uv) for more information:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing uv, create a new virtual environment from the project root using:

```bash
uv venv
```

Then install the packages from the `pyproject.toml`

```bash
uv pip install -r pyproject.toml
```

Then run the project with the following commands:

```bash
# To run gale shapley on a single preference list
uv run test.py --gs prefs/<file>.txt

# To run gale shapley on a suite of preference list
uv run test.py --gs-suite prefs/

# To run the verifier on a single match list
uv run test.py --verify prefs/<file>.txt matches/<file>.txt

# To run the verifier on a suite of match lists (this command assumes there is a corresponding preference list for each match list)
uv run test.py --verify-suite prefs/ matches/
```

**If using pip:**

Install matplotlib with pip

```bash
python -m pip install -U pip
python -m pip install -U matplotlib
```

Make sure you are using the correct interpreter that matplotlib installed to. Then run the following commands to run the project.

```bash
# To run gale shapley on a single preference list
python test.py --gs prefs/<file>.txt

# To run gale shapley on a suite of preference list
python test.py --gs-suite prefs/

# To run the verifier on a single match list
python test.py --verify prefs/<file>.txt matches/<file>.txt

# To run the verifier on a suite of match lists (this command assumes there is a corresponding preference list for each match list)
python test.py --verify-suite prefs/ matches/
```

The above commands may differ for some people based on devices or python version. Command alternative to `python` are `python3` and `py`

## Required Input File Format

- First line: integer 'n'
- Next 'n' lines: Hospital preference lists
- Next 'n' lines: Student preference lists

## Output File Format

- Writes each matching to a file in the matches/ directory that has a name corresponding to the preference list it was generated from
- Output 'n' lines, one per hospital 'i'
- i j , meaning hospital i is matched to student j
- The verifier prints whether matching is valid and stable, or reason for invalidity/blocking pair causing unstable matching.

## Task C Solution and Graph

Gale Shapley Algorithm input size vs execution time graph
![Gale Shapley Algorithm input size vs execution time graph](gs_execution_time.png)

Verifier Algorithm input size vs execution time graph
![Verifier Algorithm input size vs execution time graph](verifier_execution_time.png)

- Based on both line graphs above, the matcher and the verifier running times increase as n increases, pointing towards a polynomial growth. By analyzing the growth rate of the two, we can see that the verifier increases much steeper than the matcher. This suggests that the verifier is closer to a cubic growth (O(n^3)) while the Gale Shapley matching algorithm is closer to O(n^2). This is caused because for each hospital, the verifier considered up to (n-1) students as potential blocking pairs, which adds up to n^2 candidate pairs. Additionally, the verifier uses list.index() which is an O(n) operation leading to a total of O(n^3), hence leading to a steeper curve. Finally, to support this claim, we see that by the time n reaches 1000, the execution time gets to about 0.43 seconds in the Gale-Shapley algorithm, while in the verifier it gets to around 7.94 seconds, indicating quicker growth.