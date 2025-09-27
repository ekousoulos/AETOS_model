Scenario Example
================

This section demonstrates the full workflow of running the model with the scenario  
:bdg-success:`AETOS_UNNZ20250911` (*Unrestricted Trade, Net-Zero by 2050*).  

The steps below show how to prepare inputs, solve the model, process results, and generate visualisations.

Step 1 – Transform Input Data
-----------------------------

- **Input**: Excel file: ``input_data/AETOS_UNNZ20250911.xlsx`` & Config: ``config_otoole_v3_AETOS.yaml`` (defines parameter mappings, sets, and units)  
- **Output**: CSV files: ``CSVFiles/`` & Datafile (TXT, solver-ready): ``output_data/AETOS_UNNZ20250911.txt``  


.. code-block:: bash

   otoole convert excel csv input_data/AETOS_UNNZ20250911.xlsx CSVFiles config_otoole_v3_AETOS.yaml
   otoole convert csv datafile CSVFiles output_data/AETOS_UNNZ20250911.txt config_otoole_v3_AETOS.yaml

Step 2 – Generate LP File with GLPK
-----------------------------------

Run **GLPK** to convert the OSeMOSYS model and scenario data into a **linear program (LP) file**.  

- **Input**: Model: ``model/osemosys_fast_v8_AETOS.txt`` & Data: ``output_data/AETOS_UNNZ20250911.txt``  
- **Output**: LP file: ``results/results.lp``  

.. code-block:: bash

   glpsol -m model/osemosys_fast_v8_AETOS.txt -d output_data/AETOS_UNNZ20250911.txt --wlp results/results.lp --check

Step 3 – Solve the Model with CPLEX
-----------------------------------

Run **CPLEX** to solve the optimization problem from the LP file.  

- **Input**: LP file: ``results/results.lp`` (generated in Step 2)  
- **Output**: Solution file: ``results/results.sol``  

.. code-block:: clean

   cplex
   read results/results.lp
   optimize
   write results/results.sol
   quit

Step 4 – Transform and Sort Results
-----------------------------------

Process the raw solver output into a readable format and sort it.  

- **Input:** ``results/results.sol`` (CPLEX solution file)  
- **Output:**  
  - ``results/trans_results.txt`` (converted results)  
  - ``results/trans_results_sorted.txt`` (sorted results, ready for export/analysis)  


.. code-block:: bash

   python scripts/transform_31072013.py results/results.sol results/trans_results.txt
   sort results/trans_results.txt > results/trans_results_sorted.txt

Step 5 – Export Results to Excel
--------------------------------

Convert the processed results into an Excel file for further analysis and visualisation.  

- **Input:** ``results/trans_results_sorted.txt``  
- **Output:** ``results/<DATE_TAG>_v1.xlsx`` (Excel file saved in the ``results`` folder)  


.. code-block:: bash

   python scripts/export_to_excel.py

Step 6 – Visualise Results
--------------------------

Generate plots for **installed capacity** and **annual activity shares** using the provided Python scripts.  

- **Input:** Processed results in CSV format (e.g. ``results/20250912_UNNZv1.csv``)  
- **Output:** Plots (PDF/PNG) saved in the ``visualisation`` folder  


.. code-block:: bash

   python scripts/totalcapnorm.py results/20250912_UNNZv1.csv UNNZ
   python scripts/totalactnorm.py results/20250912_UNNZv1.csv UNNZ

.. toctree::
   :maxdepth: 1


