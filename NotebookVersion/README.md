# Notebook version of RankingFacts
This is a notebook version of tool "Ranking Facts" that runs locally. Web-based application can be found in here: http://demo.dataresponsibly.com/rankingfacts/.


### Assumptions for Input Dataset

1. The input dataset is a table that is stored in .CSV file.
2. We have four real datasets as examples. [dataset README](https://github.com/DataResponsibly/RankingFacts/blob/master/NotebookVersion/dataset/README.md)

### Install RankingFacts

Step 1 Download RankingFacts.

Step 2 Unzip the downloaded source file and initiate the python environment. We require python version >= 3.6 and < 3.8. Replace "python" to your python version. For example, replace "python" with "python3" and "pip" with "pip3" if your python is called by "python3". 

```bash
cd RankingFacts  # go to the RankingFacts repository that is just downloaded
python -m venv venv
source venv/bin/activate  # activate the environment for RankingFacts
pip install -r requirements.txt
```

### Run RankingFacts
```bash
jupyter notebook
```

And open the notebook **Nutrition_Labels_For_Rankings.ipynb**.




Copyright <2018> <dataresponsibly.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
