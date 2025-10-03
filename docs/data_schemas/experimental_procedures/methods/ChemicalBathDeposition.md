### Numerical quantities
??? "duration"
    The total time of the procedure.

    * type: float
    * unit: minute
    * example: 15

??? "time_in_solution"
    The total time of all the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "sample_temperature"
    The temperature of the substrate during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "solution_temperature"
    The temperature of the solution during the activity. 

    * type: float
    * unit: C
    * example: 35

### Categorical quantities
??? "drying_procedure"
    The method by which the liquid is removed from the sample after dipping.

    * type: str
    * options:
        * gas_blowing
        * self_drying
        * heating
        * tissue_paper
        * none
        * other

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "solution"
    Details about the solution.
    {% include "data_schemas/experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}      

### Method data
??? "m_def"
    A keyword that needs to be included to be abel to utilize normalization features in NOMAD
    For methods that has been defined in NOMAD, this should be on the form
    perovskite_solar_cell_database.schema_packages.tandem.device_stack.METHOD

    * type: str
    * example: 
        * perovskite_solar_cell_database.schema_packages.tandem.device_stack.ChemicalBathDeposition   