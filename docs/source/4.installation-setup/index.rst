Installation & Setup
====================
Setup Steps
------------

Setting up the **AETOS** model is straightforward.  
Follow the four steps below to get started:

.. contents::
   :local:
   :depth: 1

.. warning::
   Make sure you have `Python <https://www.python.org/>`_ and  
   `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ installed beforehand.

**Step 1 – Clone the Repository**

Clone the repository, which contains everything from data editing to running and visualisation:

.. code-block:: bash

   git clone https://github.com/ekousoulos/AETOS_model.git
   cd AETOS_model

**Step 2 – Create a Python Environment**

Use **Miniconda** (or Anaconda) to create a clean Python environment for running the provided scripts:

.. code-block:: none

   conda create -n aetos python=3.11
   conda activate aetos

**Step 3 – Install a Solver**

You need GLPK to generate the LP file, and a high-performance solver (CPLEX or Gurobi) to solve it efficiently:

- `GLPK <https://www.gnu.org/software/glpk/>`_ (open-source, **mandatory** for LP file creation)  
- `CPLEX <https://www.ibm.com/products/ilog-cplex-optimization-studio>`_ (fast & robust, academic license available)  
- `Gurobi <https://www.gurobi.com/>`_ (powerful commercial solver, free academic license)  
- `CBC <https://github.com/coin-or/Cbc>`_ (open-source, decent performance for medium models)  
- `HiGHS <https://highs.dev/>`_ (very fast open-source solver, promising alternative for LP/MIP)  

Example installation for GLPK (Linux/Mac):

.. code-block:: bash

   conda install -c conda-forge glpk
   
Example installation for CPLEX (Linux/Mac/Windows):

.. code-block:: bash

   conda install -c ibmdecisionoptimization cplex

**Step 4 – Install Otoole**

`Otoole <https://otoole.readthedocs.io/>`_ is the main utility for handling OSeMOSYS input/output.  

.. code-block:: bash

   pip install otoole


Additional Packages for Visualisation
-------------------------------------

For plotting and analysis, you will also need **pandas**, **numpy** and  **matplotlib** withing your **aetos** Pyhon environment:

.. code-block:: bash

   pip install pandas numpy matplotlib

✅ You’re all set! After these steps, you can run the AETOS workflows, edit data, solve scenarios, and visualise results.
