### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "blade_speed"
    The speed of the blade.

    * type: float
    * unit: mm/s
    * example: 15

??? "blade_angle"
    The angle of the blade.

    * type: float
    * unit: degrees
    * example: 20

??? "blade_height"
    The height of the blade.

    * type: float
    * unit: mm
    * example: 4

??? "ink_volume"
    The volume of the ink used.

    * type: float
    * unit: ml
    * example: 2.5

??? "sample_temperature"
    The temperature of the sample during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "solution_temperature"
    The temperature of the solution during the activity. 

    * type: float
    * unit: C
    * example: 35

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "ink"
    Details about the ink.
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
        * perovskite_solar_cell_database.schema_packages.tandem.device_stack.SlotDieCoating        