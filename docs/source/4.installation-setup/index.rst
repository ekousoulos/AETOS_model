Installation & Setup
====================

Setting up the **AETOS** model is straightforward.  
Follow the four steps below to get started:

.. contents::
   :local:
   :depth: 1

.. tip::
   Make sure you have `Python <https://www.python.org/>`_ and  
   `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ installed beforehand.

Step 1 – Clone the Repository
-----------------------------

Clone the repository, which contains everything from data editing to running and visualisation:

.. code-block:: bash

   git clone https://github.com/ekousoulos/AETOS_model.git
   cd AETOS_model

Step 2 – Create a Python Environment
------------------------------------

Use **Miniconda** (or Anaconda) to create a clean Python environment for running the provided scripts:

.. code-block:: bash

   conda create -n aetos python=3.11
   conda activate aetos

Step 3 – Install a Solver
-------------------------

You will need a solver to process the model:

- `GLPK <https://www.gnu.org/software/glpk/>`_ (open-source, recommended for LP file creation)  
- `CPLEX <https://www.ibm.com/products/ilog-cplex-optimization-studio>`_ (fast & robust, academic license available)  
- `Gurobi <https://www.gurobi.com/>`_ (powerful commercial solver, free academic license)  

Example installation for GLPK (Linux/Mac):

.. code-block:: bash

   conda install -c conda-forge glpk

Step 4 – Install Otoole
-----------------------

`Otoole <https://otoole.readthedocs.io/>`_ is the main utility for handling OSeMOSYS input/output.  

.. code-block:: bash

   pip install otoole

.. important::
   Otoole is required for converting, validating, and reporting model input/output files.

Additional Packages for Visualisation
-------------------------------------

For plotting and analysis, you will also need:

.. code-block:: bash

   pip install pandas numpy matplotlib

✅ You’re all set! After these steps, you can run the AETOS workflows, edit data, solve scenarios, and visualise results.
