Scenario Example
================

This section demonstrates running the model with the scenario :bdg-success:`AETOS_PNNZ20250911`
(policy-neutral net-zero, version 20250911).

Step 1 – Transform Input Data
-----------------------------

Convert the Excel file into CSV, then into the OSeMOSYS datafile:

.. code-block:: bash

   # Excel → CSV
   otoole convert excel csv input_data/AETOS_PNNZ20250911.xlsx CSVFiles config_otoole_v3_AETOS.yaml

   # CSV → TXT (datafile)
   otoole convert csv datafile CSVFiles output_data/AETOS_PNNZ20250911.txt config_otoole_v3_AETOS.yaml

Step 2 – Generate LP File with GLPK
-----------------------------------

Use **GLPK** to generate the LP problem file:

.. code-block:: bash

   glpsol -m model/osemosys_fast_v8_AETOS.txt -d output_data/AETOS_PNNZ20250911.txt --wlp results/results.lp --check

Step 3 – Solve the Model with CPLEX
-----------------------------------

Run **CPLEX** to solve the optimization problem:

.. code-block:: bash

   cplex
   read results/results.lp
   optimize
   write results/results.sol
   quit

Step 4 – Transform and Sort Results
-----------------------------------

Process the raw solver results and sort them:

.. code-block:: bash

   python scripts/transform_31072013.py results/results.sol results/trans_results.txt
   sort results/trans_results.txt > results/trans_results_sorted.txt

Step 5 – Export Results to Excel
--------------------------------

Export the processed results into Excel for analysis:

.. code-block:: bash

   python scripts/export_to_excel.py

Step 6 – Visualise Results
--------------------------

Generate plots for installed capacity and activity shares:

.. code-block:: bash

   python scripts/totalcapnorm.py results/20250912_UNNZv1.csv UNNZ
   python scripts/totalactnorm.py results/20250912_UNNZv1.csv UNNZ

.. toctree::
   :maxdepth: 1


