<!-- Base section {% include "data_schemas/experimental_procedures/subsections/deposition_segment.md" %}  -->

### Boolean quantities
??? "dynamic_spin_coating"
    TRUE if the if the liquid is added on a spinning substrate. FALSE if the liquid is applied before the substrate starts spinning. 

    * type: boolean
    * options: TRUE, FALSE  

??? "antisolvent"
    True if an antisolvent is used during spin-coating. 

    * type: boolean
    * options: TRUE, FALSE  

??? "gas_quenching"
    True if an gas quenching is used during spin-coating. 

    * type: boolean
    * options: TRUE, FALSE 


### Numeric quantities
??? "substrate_temperature"
    The temperature of the substrate during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "duration"
    The total time of all the spin-coating procedure. 

    * type: float
    * unit: s
    * example: 60

??? "solvent_volume"
    volume of the precursor solution used for spin coating.

    * type: float
    * unit: ml
    * example: 0.6

??? "dispense_start_time"
    Time of the start of the dispensing in seconds after the start of the spin-coating program. For static spin-coating where the solution is added before the spinning starts, this is 0.

    * type: float
    * unit: s
    * example: 5

??? "dispense_speed"
    The dispense speed of the precursor solution.

    * type: float
    * unit: ml/s
    * example: 1.5

??? "dispense_speed"
    The dispense speed of the precursor solution.

    * type: float
    * unit: ml/s
    * example: 1.5

??? "distance_between_tip_and_substrate"
    Distance between the pipet tip and the substrate

    * type: float
    * unit: mm
    * example: 2.5

### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Sub sections
??? "spin_coating_segments"
    A spin-coating program can be composed of several different steps. This is a repeating section for describing all the spin-coating steps.

    ??? "duration"
        The length of the step. 

        * type: float
        * unit: s
        * example: 60

    ??? "speed_start"
        The spin speed of the start of the step.

        * type: float
        * unit: rpm
        * example: 0

    ??? "speed_end"
        The spin speed of the end of the step.

        * type: float
        * unit: rpm
        * example: 4000

    ??? "acceleration"
        The acceleration of the rotations.

        * type: float
        * unit: rpm/s
        * example: 1000

??? "solution"
    Details about the solution.
    {% include "data_schemas/experimental_procedures/subsections/solution.md" %} 

??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}  

??? "antisolvent_details" 
    {% include "data_schemas/experimental_procedures/subsections/antisolvent_details.md" %} 

??? "gas_quenching_details"
    {% include "data_schemas/experimental_procedures/subsections/gas_quenching_details.md" %} 