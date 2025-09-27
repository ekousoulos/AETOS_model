Visualisation
==============

Visualization & Plotting
------------------------

The repository includes dedicated plotting scripts for analysing key outputs, such as **installed capacity** and **generation activity**.  
Run them by passing the results file and scenario tag as arguments. 

Replace :bdg-primary:`<RESULTS_FILE>` with the name of your results file (e.g. :bdg-success:`20250912_UNNZv1.csv`),  
and :bdg-primary:`<TAG>` with the scenario tag (e.g. :bdg-success:`UNNZ`):

.. code-block:: bash

   python scripts/totalcapnorm.py results/<RESULTS_FILE> <TAG>

   python scripts/totalactnorm.py results/<RESULTS_FILE> <TAG>

The first script produces **normalised capacity plots**, while the second produces **normalised activity plots**.  
Figures are saved automatically into the ``visualisation`` folder.  