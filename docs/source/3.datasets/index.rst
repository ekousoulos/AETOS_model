Datasets
========

The **AETOS** model is built on openly available and institutional datasets, 
processed into a consistent OSeMOSYS-ready format to support transparent and reproducible analysis.  

Input Assumptions
------------------

**Input Assumption Files**

The AETOS model uses a collection of Excel files for assumptions on capacity, demand, fuel supply, trade, and techno-economics.  
Each file is linked to openly available datasets and institutional sources.

.. list-table::
   :header-rows: 1
   :widths: 30 70
   :class: source-table

   * - **Category**
     - **Sources**
   * - Electricity Capacity
     - JRC-IDEES, ENTSO-E, ENTSO-G, IRENA, EU Reference Scenario 2020
   * - Fuel Supply & Extraction
     - IEA, IRENA Statistics, UN Energy Data, Africa Continental Master Plan (CMP)
   * - Natural Gas & LNG
     - ENTSO-G, IEA Gas Market Reports, Africa CMP, IRENA
   * - Interconnections
     - ENTSO-E TYNDP, Africa Continental Master Plan
   * - Techno-economics
     - EU Reference Scenario 2020, IRENA, CMP, Energy Price Databases
   * - Transmission & Losses
     - ENTSO-E, IEA Africa Energy Outlook
   * - Demand
     - TIAM-ECN Projections, EU Reference Scenario 2020, Africa CMP
   * - Climate Policy
     - EU ETS, European Commission Climate Targets



**Processing Methods**

.. admonition:: Data Harmonization & Preparation
   :class: tip

   The input datasets were processed into **consistent OSeMOSYS-ready formats** to ensure transparency, comparability, and reproducibility.  
   The main steps included:

   - **Unit Harmonization** → All energy and capacity data converted into consistent units (PJ, TWh, bcm, GW).  
   - **Code Mapping** → Alignment of national ISO codes with the OSeMOSYS regional and technology structure.  
   - **Gap-Filling** → Missing data filled using proxies from trusted sources (IEA, IRENA, UN datasets).  
   - **Transformation Pipelines** → Automated Python scripts standardize raw data into clean CSV templates ready for the model.  

Zenodo Repository
-----------------

.. important::

   All processed datasets and scenario outputs are openly available on Zenodo:  
   `AETOS Dataset <https://zenodo.org/records/17007181>`_  

   Please cite this repository alongside the model documentation when using AETOS in your research.  
