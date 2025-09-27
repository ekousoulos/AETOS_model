Model Architecture
==================

Model Structure
---------------

The AETOS model builds on the OSeMOSYS framework to provide a 
transparent, open-source tool for cross-continental energy system analysis.  
Its design philosophy emphasizes reproducibility, comparability across regions, 
and scalability from national to continental level.

Framework & Philosophy
^^^^^^^^^^^^^^^^^^^^^^


- Fully based on the OSeMOSYS open-source modeling framework.  
- Emphasis on transparency, open data, and reproducibility.  
- Designed for multi-regional, long-term scenario exploration.  

The diagram below shows the **AETOS input–output structure**, linking key datasets to model outputs:

.. image:: /_static/AETOS-IO2.svg
   :alt: AETOS IO
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 1. <em>AETOS Input Output.</em></p>

Regions & Countries
^^^^^^^^^^^^^^^^^^^^

AETOS covers **78 countries** across Africa and Europe, with each country modeled individually.:  

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item::

      **Africa (48)**

      .. list-table::
         :header-rows: 1
         :widths: 70 30
         :class: no-scroll

         * - Country
           - ISO
         * - Algeria
           - :bdg-primary:`DZ`
         * - Malawi
           - :bdg-primary:`MW`
         * - Angola
           - :bdg-primary:`AO`
         * - Mali
           - :bdg-primary:`ML`
         * - Benin
           - :bdg-primary:`BJ`
         * - Mauritania
           - :bdg-primary:`MR`
         * - Botswana
           - :bdg-primary:`BW`
         * - Morocco
           - :bdg-primary:`MA`
         * - Burkina Faso
           - :bdg-primary:`BF`
         * - Mozambique
           - :bdg-primary:`MZ`
         * - Burundi
           - :bdg-primary:`BI`
         * - Namibia
           - :bdg-primary:`NA`
         * - Cameroon
           - :bdg-primary:`CM`
         * - Niger
           - :bdg-primary:`NE`
         * - Central African Rep.
           - :bdg-primary:`CF`
         * - Nigeria
           - :bdg-primary:`NG`
         * - Chad
           - :bdg-primary:`TD`
         * - Rwanda
           - :bdg-primary:`RW`
         * - Côte d'Ivoire
           - :bdg-primary:`CI`
         * - Senegal
           - :bdg-primary:`SN`
         * - Djibouti
           - :bdg-primary:`DJ`
         * - Sierra Leone
           - :bdg-primary:`SL`
         * - DR Congo
           - :bdg-primary:`CD`
         * - Somalia
           - :bdg-primary:`SO`
         * - Egypt
           - :bdg-primary:`EG`
         * - South Africa
           - :bdg-primary:`ZA`
         * - Equatorial Guinea
           - :bdg-primary:`GQ`
         * - South Sudan
           - :bdg-primary:`SS`
         * - Eritrea
           - :bdg-primary:`ER`
         * - Sudan
           - :bdg-primary:`SD`
         * - Eswatini
           - :bdg-primary:`SZ`
         * - Tanzania
           - :bdg-primary:`TZ`
         * - Ethiopia
           - :bdg-primary:`ET`
         * - Togo
           - :bdg-primary:`TG`
         * - Gabon
           - :bdg-primary:`GA`
         * - Tunisia
           - :bdg-primary:`TN`
         * - Gambia
           - :bdg-primary:`GM`
         * - Uganda
           - :bdg-primary:`UG`
         * - Ghana
           - :bdg-primary:`GH`
         * - Zambia
           - :bdg-primary:`ZM`
         * - Guinea
           - :bdg-primary:`GN`
         * - Zimbabwe
           - :bdg-primary:`ZW`
         * - Guinea-Bissau
           - :bdg-primary:`GW`
         * - Kenya
           - :bdg-primary:`KE`
         * - Lesotho
           - :bdg-primary:`LS`
         * - Liberia
           - :bdg-primary:`LR`
         * - Libya
           - :bdg-primary:`LY`

   .. grid-item::

      **Europe (30)**

      .. list-table::
         :header-rows: 1
         :widths: 70 30
         :class: no-scroll

         * - Country
           - ISO
         * - Austria
           - :bdg-primary:`AT`
         * - Lithuania
           - :bdg-primary:`LT`
         * - Belgium
           - :bdg-primary:`BE`
         * - Luxembourg
           - :bdg-primary:`LU`
         * - Bulgaria
           - :bdg-primary:`BG`
         * - Latvia
           - :bdg-primary:`LV`
         * - Switzerland
           - :bdg-primary:`CH`
         * - Malta
           - :bdg-primary:`MT`
         * - Cyprus
           - :bdg-primary:`CY`
         * - Netherlands
           - :bdg-primary:`NL`
         * - Czechia
           - :bdg-primary:`CZ`
         * - Norway
           - :bdg-primary:`NO`
         * - Germany
           - :bdg-primary:`DE`
         * - Poland
           - :bdg-primary:`PL`
         * - Denmark
           - :bdg-primary:`DK`
         * - Portugal
           - :bdg-primary:`PT`
         * - Estonia
           - :bdg-primary:`EE`
         * - Romania
           - :bdg-primary:`RO`
         * - Spain
           - :bdg-primary:`ES`
         * - Sweden
           - :bdg-primary:`SE`
         * - Finland
           - :bdg-primary:`FI`
         * - Slovenia
           - :bdg-primary:`SI`
         * - France
           - :bdg-primary:`FR`
         * - Slovakia
           - :bdg-primary:`SK`
         * - Greece
           - :bdg-primary:`GR`
         * - United Kingdom
           - :bdg-primary:`UK`
         * - Croatia
           - :bdg-primary:`HR`
         * - Hungary
           - :bdg-primary:`HU`
         * - Ireland
           - :bdg-primary:`IE`
         * - Italy
           - :bdg-primary:`IT`


Technologies & Fuels
^^^^^^^^^^^^^^^^^^^^^^

The AETOS model represents **3,283 technologies**, spanning all major fuels and system components.

.. list-table:: Fuels
   :header-rows: 1
   :widths: 25 75
   :class: source-table

   * - Category
     - Fuels

   * - Fossil
     - Coal, Lignite, Natural Gas, Fuel Oil / Heavy Fuel, Light Fuel, Diesel Oil, Refinery Gas, Derived Gas

   * - Renewables
     - Solar, Wind, Hydropower, Biomass, Geothermal, Tidal, Ocean/Wave, Waste

   * - Secondary / Vectors
     - Nuclear, Battery, Electricity


Temporal Resolution
^^^^^^^^^^^^^^^^^^^^^^

- **Horizon:** 2021–2060 (yearly time steps).  
- **Intra-annual resolution:** 16 time-slices (4 seasons × 4 daily periods), ensuring seasonal and daily demand peaks are fully captured.  

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

System Design
-------------

Reference Energy System
^^^^^^^^^^^^^^^^^^^^^^^

These Reference Energy Systems (RES) provide a schematic view of how **energy resources, technologies, and demand sectors** are connected within the model.  
They illustrate flows from **primary resources** (fossil, renewable, imports) through **conversion technologies** (power plants, trade infrastructure, storage) to meet **final electricity and gas demand**. 

.. list-table:: 
   :widths: 50 50
   :header-rows: 0
   :class: res-table

   * - .. image:: /_static/RES-AU.svg
          :width: 100%
     - .. image:: /_static/RES-EU.svg
          :width: 100%

.. raw:: html

   <p class="mycaption">Figure 2. <em>Reference Energy System – Africa (left) and Europe (right).</em></p>
 

Interconnection Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

The model represents electricity interconnections explicitly.  
Each link between two countries is modeled as a **bidirectional interconnector** with two modes:

- **Mode 1:** Power flow from *Country 1 → Country 2*  
- **Mode 2:** Power flow from *Country 2 → Country 1*  

This structure allows detailed accounting of **imports, exports, and trade balances**, while consistently linking power plants, demand, and regional grids.
 

.. image:: /_static/Interconnector.svg
   :alt: Interconnection diagram
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 3. <em>Interconnection architecture between African and European regions.</em></p>


Storage Structure
^^^^^^^^^^^^^^^^^

The model represents storage explicitly by separating **technology operation** and **storage content** into two linked components:  

- **STOR_T (Technology):** governs charging and discharging of energy.  
- **STOR_S (Storage):** tracks stored energy across time periods.  

Two modes are used:  

- **Mode 1:** Charging (from grid/plant → storage).  
- **Mode 2:** Discharging (from storage → grid/plant).   

.. image:: /_static/storage.svg
   :alt: Storage diagram
   :align: center
   :width: 65%

.. raw:: html

   <p class="mycaption">Figure 4. <em>Storage Infrustructure.</em></p>


Natural Gas Network Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model represents natural gas flows through **pipelines**, **LNG terminals** and **domestic extraction technologies**.
  
- Pipelines are modeled as **bidirectional links** (Mode 1 = export, Mode 2 = import).  
- LNG imports and exports are included as separate technologies.  
- Domestic extraction is captured explicitly via NG00X00 technologies.  

.. image:: /_static/NGN.svg
   :alt: Natural Gas System diagram
   :align: center
   :width: 90%

.. raw:: html

   <p class="mycaption">Figure 5. <em>Natural Gas System Infrustructure.</em></p>


Naming Manual
-------------

This manual explains the **AETOS naming conventions** for technologies, fuels, backstops, and infrastructure.  
Codes are **systematic, compact, and interpretable**, ensuring reproducibility and transparency.

Technologies
^^^^^^^^^^^^

.. admonition:: Technology Structure

   :bdg-primary:`COUNTRY` :bdg-warning:`FUEL` :bdg-success:`TECHNOLOGY` :bdg-secondary:`CLASS`

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Fuel Codes**

      .. list-table::
         :header-rows: 1
         :widths: 25 75
         :class: source-table

         * - **Fuel Code**
           - **Fuel Name**
         * - :bdg-warning:`NU`
           - Nuclear
         * - :bdg-warning:`CO`
           - Coal
         * - :bdg-warning:`LI`
           - Lignite
         * - :bdg-warning:`NG`
           - Natural Gas
         * - :bdg-warning:`SO`
           - Solar
         * - :bdg-warning:`WI`
           - Wind
         * - :bdg-warning:`HYD`
           - Hydropower
         * - :bdg-warning:`BM`
           - Biomass
         * - :bdg-warning:`BATT`
           - Battery
         * - :bdg-warning:`WS`
           - Waste
         * - :bdg-warning:`DG`
           - Derived Gas
         * - :bdg-warning:`HF`
           - Fuel Oil / Heavy Fuel
         * - :bdg-warning:`LF`
           - Light Fuel
         * - :bdg-warning:`RG`
           - Refinery Gas
         * - :bdg-warning:`DS`
           - Diesel Oil
         * - :bdg-warning:`GO`
           - Geothermal
         * - :bdg-warning:`TID`
           - Tidal
         * - :bdg-warning:`OCWV`
           - Ocean / Wave

   .. grid-item::

      **Technology Codes**

      .. list-table::
         :header-rows: 1
         :widths: 25 75
         :class: source-table

         * - **Tech Code**
           - **Description**
         * - :bdg-success:`CHP`
           - Combined Heat & Power
         * - :bdg-success:`STP`
           - Steam Turbine Plant
         * - :bdg-success:`CCP`
           - Combined Cycle Plant
         * - :bdg-success:`GCP`
           - Gas Turbine Plant
         * - :bdg-success:`GCC`
           - Gas Combined Cycle
         * - :bdg-success:`HPF`
           - Internal Combustion Engine
         * - :bdg-success:`CCS`
           - Carbon Capture Storage
         * - :bdg-success:`ON`
           - Wind Onshore
         * - :bdg-success:`OF`
           - Wind Offshore
         * - :bdg-success:`UTP` / :bdg-success:`U1P`
           - Solar Utility Plant
         * - :bdg-success:`STH` / :bdg-success:`C1P`
           - Solar Thermal
         * - :bdg-success:`MP` / :bdg-success:`MS`
           - Hydro Reservoir
         * - :bdg-success:`SP`
           - Pumped Storage
         * - :bdg-success:`RP`
           - Hydro Run-of-River
         * - :bdg-success:`RCP`
           - Reciprocating Engine
         * - :bdg-success:`CVP`
           - Geothermal
         * - :bdg-success:`SCP`
           - Sub-critical Pulverised Coal
         * - :bdg-success:`NDP`
           - Wind (Africa)


**Class Codes**

.. list-table::
   :header-rows: 1
   :widths: 25 75
   :class: source-table

   * - **Class Code**
     - **Meaning**
   * - :bdg-secondary:`H1`
     - Historical
   * - :bdg-secondary:`N1`
     - New

**Example**

:bdg-primary:`CY` :bdg-warning:`SO` :bdg-success:`UTP` :bdg-secondary:`H1`  
= Cyprus, Solar Utility Plant, Historical


Backstops
^^^^^^^^^

.. admonition:: Backstops Structure

	:bdg-primary:`COUNTRY` :bdg-danger:`BACKSTOP_TYPE`

**Backstop Codes**

.. list-table::
   :header-rows: 1
   :widths: 30 70
   :class: source-table

   * - **Backstop**
     - **Meaning**
   * - :bdg-danger:`BACKSTOP`
     - Technology capacity issues
   * - :bdg-danger:`CO2BACKSTOP`
     - Emissions issues
   * - :bdg-danger:`NGBACKSTOP`
     - Natural gas supply issue

**Example**  
:bdg-primary:`CY` :bdg-danger:`CO2BACKSTOP`  
= Cyprus, CO₂ emissions backstop


Feed-in Fuel Technologies
^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Feed-in-Fuels Structure
 
	:bdg-primary:`COUNTRY` :bdg-warning:`FUEL` :bdg-success:`00I00`

**Example**  
:bdg-primary:`CY` :bdg-warning:`NG` :bdg-success:`00I00`  
= Cyprus, Natural Gas Import node


Transmission
^^^^^^^^^^^^

.. admonition:: Transmission Structure

	:bdg-primary:`COUNTRY` :bdg-info:`EL00T00`

**Example**  
:bdg-primary:`CY` :bdg-info:`EL00T00`  
= Cyprus, Electricity Transmission


Distribution
^^^^^^^^^^^^^

.. admonition:: Distribution Structure
 
	:bdg-primary:`COUNTRY` :bdg-info:`EL00D00`

**Example**  
:bdg-primary:`CY` :bdg-info:`EL00D00`  
= Cyprus, Electricity Distribution


LNG Imports
^^^^^^^^^^^

.. admonition:: LNG Imports Structure

	:bdg-primary:`COUNTRY`:bdg-success:`LG00I00`

**Example**  
:bdg-primary:`CY` :bdg-success:`LG00I00`  
= Cyprus LNG Import


LNG Exports
^^^^^^^^^^^

.. admonition:: LNG Exports Structure
	
	:bdg-primary:`COUNTRY` :bdg-success:`LG00E00`

**Example**  
:bdg-primary:`CY` :bdg-success:`LG00E00`  
= Cyprus LNG Export


Natural Gas Extraction
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Natural Gas Extraction Structure
	
	:bdg-primary:`COUNTRY` :bdg-success:`NG00X00`

**Example**  
:bdg-primary:`DZ` :bdg-success:`NG00X00`  
= Algeria, NG Extraction


Natural Gas Pipelines
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Natural Gas Pipelines Structure

	:bdg-primary:`COUNTRY1` :bdg-warning:`NG` :bdg-primary:`COUNTRY2` :bdg-success:`PI0`

**Example**  
:bdg-primary:`DZ` :bdg-warning:`NG` :bdg-primary:`IT` :bdg-success:`PI0`  
= Algeria → Italy NG Pipeline

Grid Interconnections
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Grid Interconnections Structure
  
	:bdg-primary:`COUNTRY1` :bdg-warning:`EL` :bdg-primary:`COUNTRY2` :bdg-success:`PH1`

**Example**  
:bdg-primary:`AO` :bdg-warning:`EL` :bdg-primary:`NA` :bdg-success:`PH1`  
= Angola ↔ Namibia Electricity Interconnection

Storages
^^^^^^^^

.. admonition:: Storage Structure

   :bdg-primary:`COUNTRY` :bdg-info:`STORAGE_TYPE` :bdg-secondary:`CLASS`

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: source-table

   * - **Storage Code**
     - **Description**
   * - :bdg-info:`BATT`
     - Battery Storage
   * - :bdg-info:`HYDSP`
     - Hydrogen Storage
   * - :bdg-info:`HYDSS`
     - Hydro Reservoir Storage

**Example**  
:bdg-primary:`MA` :bdg-info:`BATT` :bdg-secondary:`N1`  
= Morocco, Battery, New


Fuels
^^^^^^^

.. admonition:: Fuels Structure
  
	:bdg-primary:`COUNTRY` :bdg-warning:`FUEL`

**Fuel Codes**

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: source-table

   * - **Fuel Code**
     - **Description**
   * - :bdg-warning:`E1`
     - Electricity Transmission
   * - :bdg-warning:`E2`
     - Electricity Distribution
   * - :bdg-warning:`E3`
     - Electricity Supply
   * - :bdg-warning:`BATF`
     - Battery Fuel
   * - :bdg-warning:`NGE`
     - Natural Gas Export

**Example**  
:bdg-primary:`CY` :bdg-warning:`E1`  
= Cyprus, Electricity Transmission


Emissions
^^^^^^^^^^

.. admonition:: Emissions Structure

	:bdg-primary:`COUNTRY`:bdg-danger:`CO2`

**Example**  
:bdg-primary:`CY` :bdg-danger:`CO2`  
= Cyprus, CO₂ emissions
