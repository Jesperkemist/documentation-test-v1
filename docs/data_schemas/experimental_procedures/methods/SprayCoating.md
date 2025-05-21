### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "nozzle_speed"
    The speed of the nozzle.

    * type: float
    * unit: mm/s
    * example: 15

??? "nozzle_angle"
    The angle of the nozzle.

    * type: float
    * unit: degrees
    * example: 20

??? "nozzle_height"
    The distance between thesample and the nozzle.

    * type: float
    * unit: mm
    * example: 4

??? "solution_volume"
    The volume of the solution used.

    * type: float
    * unit: ml
    * example: 2.5

??? "solution_temperature"
    The temperature of the solution during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "sample_temperature"
    The temperature of the sample during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "sample_area"
    The area of the samples being sprayed.

    * type: float
    * unit: cm^2
    * example: 35

??? "gas_pressure"
    The gas pressure.

    * type: float
    * unit: Pa
    * example: 35

### Categorical quantities
??? "carrier_gas"
    The carrier gas.

    * type: str
    * examples:
        * air
        * dry_air
        * N2
        * Ar
        * He
        * O2
        * H2
        * other

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "solution"
    Details about the ink.
    {% include "data_schemas/experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}      