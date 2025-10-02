Troubleshooting & FAQ
=====================

Troubleshooting
---------------

.. attention::

   If you encounter problems, check these common issues first:

- **Solver not found** → Make sure ``glpsol`` (GLPK) or ``cplex`` is installed and available in your system ``PATH``.  

  *Adding to PATH:*  

  - On **Linux/macOS**: edit ``~/.bashrc`` (or ``~/.zshrc``) and add:  
    ``export PATH=$PATH:/path/to/solver``  

  - On **Windows**: go to *System Properties → Environment Variables → Path → Edit*,  
    then add the folder path containing ``glpsol.exe`` or ``cplex.exe``.  

  - Restart your terminal or IDE for changes to take effect.  


- **Memory issues** → Try solving with CPLEX (``--solver cplex``) or increase available RAM.  
- **Long runtimes** → Test the workflow with fewer years or a reduced temporal resolution before running the full scenario.  
- **No LP/SOL file created** → Double-check the input/output paths and confirm that the ``results/`` directory exists.  

.. important::  
   The AETOS model is computationally heavy. For a full-scale scenario such as ``AETOS_UNNZ20250911``:  
   - Generating the LP file can take **~2 hours**  
   - Solving with CPLEX on HPC can take **~6 hours**  
   
   If your run fails or hangs, it is most likely due to **insufficient memory**, not an error in the workflow. Consider reducing the problem size or running on a machine with more RAM/cores.  

If issues persist, please open an issue on GitHub:  
`Report an Issue on GitHub <https://github.com/ekousoulos/AETOS_model/issues>`_

When reporting an issue, please include:  

- **Step** → At which stage of the workflow the error occurs (e.g. Step 1: Transform Input Data, Step 3: Solve with CPLEX)  
- **Solver** → Which solver was used (e.g. CPLEX) and version if known  
- **System details** → Operating system, Python version, and hardware specs (CPU/RAM, HPC vs local)  
- **Logs** → Full error message, warnings, or relevant log output (copy-paste or attach)  


FAQ
---

.. dropdown:: Which solver should I use?
   :icon: question

   Use **CPLEX** if available (faster, more memory-efficient).  

.. dropdown:: Where do I find the input data?
   :icon: question

   All processed inputs are hosted on Zenodo:  
   `AETOS Dataset on Zenodo <https://zenodo.org/records/17007181>`_  

.. dropdown:: How do I install the model?
   :icon: question

   Follow the steps under *Installation & Setup*. Clone the repo, create an environment, and install either GLPK or CPLEX.  

.. dropdown:: How do I run a quick test?
   :icon: question

   Run with smaller horizon outlook, or a smaller temporal resolution to ensure everything works before attempting the full model.  

.. dropdown:: My model run is too slow, what can I do?
   :icon: question

   Try switching solvers, reduce the horizon outlook, or run on HPC with more memory.  

.. dropdown:: Can I contribute improvements?
   :icon: question

   Yes! Contributions are welcome. You can:  
      - Open a pull request on GitHub  
      - Submit an issue with your suggestion or bug report  

.. dropdown:: Can I reuse AETOS data for my own research?
   :icon: question

   Yes, the data is open under a CC-BY license. Please cite the Zenodo repository and relevant publications.  

.. dropdown:: How can I add a new country or technology?
   :icon: question

   You’ll need to extend the dataset and model definition. Check the documentation on *Model Architecture* before making changes.  
