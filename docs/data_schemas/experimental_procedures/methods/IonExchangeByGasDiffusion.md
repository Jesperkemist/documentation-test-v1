### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "substrate_temperature"
    The temperature of the substrate/sample during the activity. 

    * type: float
    * unit: C
    * example: 35    

??? "gas_temperature"
    The temperature of the reaction gas during the activity. 

    * type: float
    * unit: C
    * example: 35 

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "gases"
    Repeating section. Details about the gases involved.
    {% include "data_schemas/experimental_procedures/subsections/gas_component.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}      

### Method data
??? "m_def"
    A keyword that needs to be included to be abel to utilize normalization features in NOMAD
    For methods that has been defined in NOMAD, this should be on the form
    perovskite_solar_cell_database.schema_packages.tandem.device_stack.METHOD

    * type: str
    * example: 
        * perovskite_solar_cell_database.schema_packages.tandem.device_stack.IonExchangeByGasDiffusion        