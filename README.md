This is a small representative example to show the issues I am facing with the options `-l gpu` and `-l A40`. 

This will launch `10` jobs will the **exact** same parameters as the ones I am facing issues with.

## Usage

```bash
git clone https://github.com/sarthakpati/small_example_to_show_cubic_sge_gpu_issues.git
# ensure you have *a* python environment activated - doesn't matter which one, since this does not do any installation
cd small_example_to_show_cubic_sge_gpu_issues
python submitter.py -e <your_email> # this will launch jobs using `-l gpu`
python submitter.py -e <your_email> -gpu A40 # this will launch jobs using `-l A40`
```