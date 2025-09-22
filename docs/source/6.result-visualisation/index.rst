Visualisation
==============

Visualization & Plotting
------------------------

The repository includes plotting scripts for key outputs (capacity, generation, trade, emissions).  

Use the provided Python scripts to generate plots from the results CSV.  
Replace :bdg-primary:`<RESULTS_FILE>` with the name of your results file (e.g. :bdg-success:`20250912_UNNZv1.csv`),  
and :bdg-primary:`<TAG>` with the scenario tag (e.g. :bdg-success:`UNNZ`).


.. code-block:: bash

   #Visualising Total Capacity Normalised
   python scripts/totalcapnorm.py results/<RESULTS_FILE> <TAG>
   
   #Visualising Total Activity Normalised
   python scripts/totalactnorm.py results/<RESULTS_FILE> <TAG>


