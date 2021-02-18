# lnl-data-collector
Simple python code to collect parameters from the .csv data report produced by the lognormal lung (lnl) model.

To run, type `python lnl_data_collector`. 
The file `test_out.csv` contains the output and its contents should match `test_out_example.csv`.

The parameters are collected from .csv data report files in the same directory as the script.
The list of parameters collected is contained in `param_names.txt`.
These names must correspond exactly to the strings in the .csv data report.

Quality of life improvements to add:
- variable output filename
- method of including subset of data report files
