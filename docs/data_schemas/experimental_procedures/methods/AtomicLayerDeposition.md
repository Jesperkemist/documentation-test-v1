### Numerical quantities
??? "duration"
    The total time of the procedure.

    * type: float
    * unit: minute
    * example: 15

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
??? "steps"
    Details about the four ALD steps.
    {% include "data_schemas/experimental_procedures/subsections/ald_segment.md" %} 

### Method data
??? "m_def"
    A keyword that needs to be included to be abel to utilize normalization features in NOMAD
    For methods that has been defined in NOMAD, this should be on the form
    perovskite_solar_cell_database.schema_packages.tandem.device_stack.METHOD

    * type: str
    * example: 
        * perovskite_solar_cell_database.schema_packages.tandem.device_stack.AtomicLayerDeposition  