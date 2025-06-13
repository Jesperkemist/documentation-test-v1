### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: minute
    * example: 35

### Categorical quantities
??? "heating_medium"
    The way by which the temperature is controlled

    * type: str
    * options:
        * hotplate
        * furnace
        * liquid_bath
        * gas
        * other

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system        

### Subsections
??? "temperature_segments"
    Repeating section. Describing each temperature step in the program
    {% include "data_schemas/experimental_procedures/subsections/temperature_segment.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}       