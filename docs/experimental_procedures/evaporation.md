### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: minute
    * example: 60

??? "number_of_sources"
    The number of sources used for the evaporation. 

    * type: int
    * example: 1

??? "substrate_temperature"
    The temperature of the substrate during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "substrate_rotation_speed"
    The rotation speed of the substrate during the activity.

    * type: float
    * unit: rpm
    * example: 10

??? "deposition_rate"
    The rate of deposition.

    * type: float
    * unit: nm/s
    * example: 0.1

??? "chamber_pressure"
    The pressure in the reaction chamber.

    * type: float
    * unit: Pa
    * example: 0.1   

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "sources"
    Repeating section. Details about the evaporation sources
    {% include "experimental_procedures/subsections/evaporation_source.md" %}  

??? "environmental_conditions"
    Mostly relevant if the evaporation not is done in a vacuum chamber
    {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}      