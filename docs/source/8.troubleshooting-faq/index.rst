Troubleshooting & FAQ
=====================

Troubleshooting
---------------

.. attention::

   If you encounter problems, please first check the following:

- **Solver not found** → Ensure `glpsol` (GLPK) or `cplex` is on your PATH  
- **Memory issues** → Use `--solver cplex` or increase RAM in your HPC script  
- **Missing dependencies** → Run `pip install -r requirements.txt`  
- **Long runtimes** → Test with fewer scenarios or a shorter time horizon  

If problems persist, open an issue on GitHub:  

`Report an Issue on GitHub <https://github.com/YourUser/AETOS_model/issues>`_  

When reporting, include:  

- The scenario you were running  
- The solver used (GLPK / CPLEX)  
- Your OS and Python version  
- Error messages or logs  


FAQ
---

**Which solver should I use?**  
Use **CPLEX** if available (faster, more memory-efficient). Use **GLPK** for a free and open-source option.

**Where do I find the input data?**  
All processed inputs are hosted on Zenodo:  
`AETOS Dataset on Zenodo <https://doi.org/10.5281/zenodo.xxxxxxx>`_

**How do I install the model?**  
Follow the steps under *Installation & Setup*. Clone the repo, create an environment, and install either GLPK or CPLEX.

**How do I run a quick test?**  
Run with fewer years, fewer scenarios, or a smaller temporal resolution to ensure everything works before attempting the full model.

**My model run is too slow, what can I do?**  
Try switching solver (GLPK → CPLEX), reduce temporal resolution, or run on HPC with more memory.

**Can I contribute improvements?**  
Yes! Open a pull request on GitHub or submit an issue with your suggestion.

**Can I reuse AETOS data for my own research?**  
Yes, the data is open under a CC-BY license. Please cite the Zenodo repository and relevant publications.

**How can I add a new country or technology?**  
You’ll need to extend the dataset and model definition. Check the documentation on *Model Architecture* before making changes.
