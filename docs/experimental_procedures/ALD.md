### Numerical quantities
??? "time_in_solution"
    The total time of all the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "substrate_temperature"
    The temperature of the substrate during the activity. 

    * type: float
    * unit: C
    * example: 35

??? "flow_rate"
    The flow rate.

    * type: float
    * unit: sccm
    * example: 35

??? "number_of_cycles"
    The number of deposition cycles

    * type: int
    * example: 50    

### Categorical quantities
??? "carrier_gas"
    The carrier gas.

    * type: str
    * examples:
        * air
        * dry_air
        * N2
        * Ar

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "segments"
    Details about the four ALD segments.
    {% include "experimental_procedures/subsections/ald_segment.md" %} 
   