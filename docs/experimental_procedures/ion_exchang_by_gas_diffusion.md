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
    {% include "experimental_procedures/subsections/gas_component.md" %} 

??? "environmental_conditions"
    {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}      