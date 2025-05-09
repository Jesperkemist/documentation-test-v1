### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "drop_volume"
    Drop volume.

    * type: float
    * unit: µl
    * example: 5

??? "print_resolution"
    The print resolution.

    * type: float
    * unit: dpi
    * example: 20

??? "print_speed"
    The speed of the printer head.

    * type: float
    * unit: mm/s
    * example: 20

??? "print_height"
    The distance from the nozzle and the substrate.

    * type: float
    * unit: mm
    * example: 4

??? "substrate_temperature"
    The temperature of the substrate/sample during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "ink_temperature"
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
    {% include "experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "experimental_procedures/subsections/environmental_conditions_deposition.md" %}      