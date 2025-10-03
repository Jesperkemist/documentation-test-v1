
### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: minute
    * example: 60

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

??? "free_text_comment"
    Any additional description not captured by any other field.

    * type: str
    * example: "An elaborate cleaning protocol" 

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
        * perovskite_solar_cell_database.schema_packages.tandem.device_stack.Cleaning          