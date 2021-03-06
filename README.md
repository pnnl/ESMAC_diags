
# Earth System Model Aerosol-Cloud Diagnostics Package

This Earth System Model (ESM) aerosol-cloud diagnostics package (ESMAC Diags) is currently used to evaluate aerosols, clouds and aerosol-cloud interactions simulated by the Department of Energy’s (DOE) Energy Exascale Earth System Model (E3SM). The first version (v1.0) focuses on comparing simulated aerosol properties with in-situ aircraft, ship and surface measurements. Various types of diagnostics and metrics are performed for aerosol number, size distribution, chemical composition, and CCN concentration to assess how well E3SM represents observed aerosol properties across spatial scales. Metrics for various meteorological and aerosol precursor quantities from the same field campaigns are also included. Version 2 is under development focusing on aerosol-cloud interactions.

More information can be found in README_ESMAC_Diags_v1.0-alpha.pdf

## To install
This code is best run using a conda virtual environment. To install the required environment one can do
```bash
conda env create -f environment.yml
```
to set up a esmac_diags environment. Note if running this on a HPC system, you may need to load the appropriate module for anaconda. 

Once the environment has been created you can activate it with ```conda activate esmac_diags``` and then this code can be installed with
```bash
pip install -e .
```
Which will install the code as editable allowing you to make changes to the codebase and it be reflected in the installed package. 


# Test run
To verify the package, enter scripts/ directory and run 
```bash
python run_testcase.py
```
Then go to the directory in testcase/figures/. There should be three figures generated:

flighttrack_ACEENA_20170630a.png

flightheight_ACEENA_20170630a.png

AerosolComposition_ACEENA_20170630a.png

Directory testcase/figures_verify/ contains what the three figures should look like. If the three figures in testcase/figures/ are consistent with figures_verify/, the testcase is successfully run.


