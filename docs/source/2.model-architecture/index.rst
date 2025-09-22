Model Architecture
==================

Model Structure
---------------

The AETOS model builds on the OSeMOSYS framework to provide a 
transparent, open-source tool for cross-continental energy system analysis.  
Its design philosophy emphasizes reproducibility, comparability across regions, 
and scalability from national to continental level.

Framework & Philosophy
----------------------

- Fully based on the OSeMOSYS open-source modeling framework.  
- Emphasis on transparency, open data, and reproducibility.  
- Designed for multi-regional, long-term scenario exploration.  

.. image:: /_static/AETOS-IO2.svg
   :alt: AETOS IO
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 1. <em>AETOS Input Output.</em></p>


Regions & Countries
-------------------

AETOS covers **78 countries**:  

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item::

      **Africa (48)**

      .. list-table::
         :header-rows: 1
         :widths: 50 50
         :class: no-scroll

         * - Country
           - 
         * - Algeria (DZ)
           - Malawi (MW)
         * - Angola (AO)
           - Mali (ML)
         * - Benin (BJ)
           - Mauritania (MR)
         * - Botswana (BW)
           - Morocco (MA)
         * - Burkina Faso (BF)
           - Mozambique (MZ)
         * - Burundi (BI)
           - Namibia (NA)
         * - Cameroon (CM)
           - Niger (NE)
         * - Central African Rep. (CF)
           - Nigeria (NG)
         * - Chad (TD)
           - Rwanda (RW)
         * - Côte d'Ivoire (CI)
           - Senegal (SN)
         * - Djibouti (DJ)
           - Sierra Leone (SL)
         * - DR Congo (CD)
           - Somalia (SO)
         * - Egypt (EG)
           - South Africa (ZA)
         * - Equatorial Guinea (GQ)
           - South Sudan (SS)
         * - Eritrea (ER)
           - Sudan (SD)
         * - Eswatini (SZ)
           - Tanzania (TZ)
         * - Ethiopia (ET)
           - Togo (TG)
         * - Gabon (GA)
           - Tunisia (TN)
         * - Gambia (GM)
           - Uganda (UG)
         * - Ghana (GH)
           - Zambia (ZM)
         * - Guinea (GN)
           - Zimbabwe (ZW)
         * - Guinea-Bissau (GW)
           - Kenya (KE)
         * - Lesotho (LS)
           - Liberia (LR)
         * - Libya (LY)
           -  

   .. grid-item::

      **Europe (30)**

      .. list-table::
         :header-rows: 1
         :widths: 50 50
         :class: no-scroll

         * - Country
           - 
         * - Austria (AT)
           - Lithuania (LT)
         * - Belgium (BE)
           - Luxembourg (LU)
         * - Bulgaria (BG)
           - Latvia (LV)
         * - Switzerland (CH)
           - Malta (MT)
         * - Cyprus (CY)
           - Netherlands (NL)
         * - Czechia (CZ)
           - Norway (NO)
         * - Germany (DE)
           - Poland (PL)
         * - Denmark (DK)
           - Portugal (PT)
         * - Estonia (EE)
           - Romania (RO)
         * - Spain (ES)
           - Sweden (SE)
         * - Finland (FI)
           - Slovenia (SI)
         * - France (FR)
           - Slovakia (SK)
         * - Greece (GR)
           - United Kingdom (UK)
         * - Croatia (HR)
           - Hungary (HU)
         * - Ireland (IE)
           - Italy (IT)


Technologies & Fuels
--------------------

The AETOS model captures a wide range of technologies and fuels. AETOS covers **3283 technologies**:   

.. list-table:: Technologies
   :header-rows: 1
   :widths: 25 75
   :class: no-scroll

   * - Category
     - Technologies
   * - Power Generation
     - Coal, Gas, Oil, Nuclear, Solar PV, CSP, Onshore Wind,
       Offshore Wind, Hydro, Biomass, Geothermal, Ocean, CCS
   * - Storage
     - Batteries, Pumped Hydro, Hydrogen Storage (future development)
   * - Trade
     - Grid Interconnectors, NG Pipelines, LNG Regasification, LNG Liquefaction


.. list-table:: Fuels
   :header-rows: 1

   * - Type
     - Fuels
   * - Fossil
     - Coal, Oil, Natural Gas
   * - Renewables
     - Solar, Wind, Hydro, Biomass, Geothermal
   * - Secondary / Vectors
     - Electricity, Hydrogen, Synthetic Fuels
   * - Other
     - Heat, Waste


Temporal Resolution
-------------------

- **Horizon:** 2021–2060 (yearly time steps).  
- **Intra-annual resolution:** 16 time-slices (4 seasons × 4 daily periods).  

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Seasons (S)**

      .. list-table::
         :header-rows: 1
         :widths: 15 15 15

         * - **Code**
           - **Season**
           - **Days**
         * - S1
           - Winter
           - 90
         * - S2
           - Spring
           - 92
         * - S3
           - Summer
           - 92
         * - S4
           - Autumn
           - 91
         * -
           - **Total**
           - **365**

   .. grid-item::

      **Daily parts (P)**

      .. list-table::
         :header-rows: 1
         :widths: 15 15 15 15

         * - **Code**
           - **Start (h)**
           - **End (h)**
           - **Duration (h)**
         * - P1
           - 0
           - 7
           - 7
         * - P2
           - 7
           - 17
           - 10
         * - P3
           - 17
           - 21
           - 4
         * - P4
           - 21
           - 24
           - 3
         * -
           -
           - **Total**
           - **24**


Refernece Energy System
-----------------------

.. list-table:: 
   :widths: 50 50
   :header-rows: 0
   :class: res-table

   * - .. image:: /_static/RES-AU.svg
          :width: 100%
     - .. image:: /_static/RES-EU.svg
          :width: 100%

.. centered:: Reference Energy System – Africa (left) and Europe (right)



Interconnection Structure
-------------------------

- Electricity interconnectors between African and European regions.  
- Cross-border trade within Africa and within Europe.  
- Distance-based cost tiers for new infrastructure.  

.. image:: /_static/interconnector.svg
   :alt: Interconnection diagram
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 1. <em>Interconnection architecture between African and European regions.</em></p>



Storage Structure
-----------------

- Explicit modeling of short-term (batteries, pumped hydro) 
  and seasonal (hydrogen, hydro reservoirs) storage.  
- Allows analysis of flexibility requirements under high RES penetration.  

.. image:: /_static/Storage.svg
   :alt: Storage diagram
   :align: center
   :width: 75%

.. raw:: html

   <p class="mycaption">Figure 4. <em>Storage Infrustructure.</em></p>


Natural Gas (NG) Network
------------------------

- Cross-border pipelines within Africa and Europe.  
- LNG terminals (liquefaction and regasification nodes).  
- Distance-based CAPEX assumptions, linked to trade volumes.  

.. image:: /_static/NGN.svg
   :alt: Natural Gas System diagram
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 3. <em>Natural Gas System Infrustructure.</em></p>



Equations & Constraints
-----------------------

- Standard OSeMOSYS energy balance, capacity expansion, and operation equations.  
- Extended trade constraints for electricity, natural gas, and hydrogen.  
- Net Zero constraint option: ensures carbon neutrality by 2050.  

.. toctree::
   :maxdepth: 1


