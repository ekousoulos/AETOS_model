Datasets
========

The **AETOS** model is built on openly available and institutional datasets, 
processed into a consistent OSeMOSYS-ready format to support transparent and reproducible analysis.  

Input Data Sources
------------------

.. list-table:: 
   :header-rows: 1
   :widths: 25 75
   :class: source-table

   * - Region
     - Main Sources
   * - **Europe**
     - JRC-IDEES 2021, ENTSO-E, ENTSO-G, Eurostat, EU Reference Scenario 2020
   * - **Africa**
     - IRENA statistics, Africa Continental Master Plan, IEA Africa analyses
   * - **Cross-cutting**
     - IRENA Renewable Energy Database, Renewables Ninja, TIAM-ECN demand projections


.. container:: data-logos

   .. image:: /_static/data_logos/auda.png
      :width: 120px
      :alt: AUDA-NEPAD

   .. image:: /_static/data_logos/entsoe.svg
      :width: 120px
      :alt: ENTSO-E

   .. image:: /_static/data_logos/entsog.png
      :width: 120px
      :alt: ENTSO-G

   .. image:: /_static/data_logos/eu.svg
      :width: 120px
      :alt: European Commission

   .. image:: /_static/data_logos/PLEXOS.PNG
      :width: 120px
      :alt: PLEXOS

   .. image:: /_static/data_logos/rn.png
      :width: 120px
      :alt: Renewables Ninja


Preprocessing Methods
---------------------

.. note::

   - Harmonization of energy and capacity units (PJ, TWh, bcm, GW)  
   - Mapping of national codes to the OSeMOSYS regional structure  
   - Gap-filling of missing statistics using proxies from IEA, IRENA, or UN datasets  
   - Transformation of raw sources into standardized CSV templates via Python pipelines  

Techno-Economic Assumptions
---------------------------

.. tip::

   - **Capital costs, O&M, lifetimes:** EU Reference Scenario 2020, IRENA, Africa Continental Master Plan (CMP)  
   - **Discount rates:** Differentiated between African and European regions  
   - **Fuel prices:** IEA World Energy Outlook and regional market data  
   - **Learning rates:** Applied to renewables and storage technologies  

Renewable Generation Profiles
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70
   :class: source-table

   * - Technology
     - Data Sources
   * - **Solar PV & CSP**
     - Renewables Ninja time-series and IRENA averages
   * - **Wind (onshore/offshore)**
     - ENTSO-E profiles (Europe), IRENA/ERA5 (Africa)
   * - **Hydro**
     - Seasonal variations from International Hydropower Association (IHA) and regional hydrology
   * - **Biomass**
     - Aggregated from FAO and IRENA sources

Trade Infrastructure
--------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70
   :class: source-table

   * - Infrastructure
     - Data Sources
   * - **Electricity interconnectors**
     - Existing and planned lines from ENTSO-E and the Africa CMP
   * - **Natural gas**
     - Pipeline networks and LNG terminals from ENTSO-G, IEA, and CMP
   * - **Hydrogen**
     - Proposed corridors and conversion facilities from ENTSO-G and IRENA
   * - **Cost tiers**
     - Distance-based tiers applied for new infrastructure investments

Zenodo Repository
-----------------

.. important::

   All processed datasets and scenario outputs are openly available on Zenodo:  
   `AETOS Dataset <https://doi.org/10.5281/zenodo.xxxxxxx>`_  

   Please cite this repository alongside the model documentation when using AETOS in your research.  
