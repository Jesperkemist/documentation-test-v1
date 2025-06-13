### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "substrate_temperature"
    The temperature of the sample during the activity. 

    * type: float
    * unit: C
    * example: 35    

??? "substrate_rotation_speed"
    The rotation speed of the substrate during the activity.

    * type: float
    * unit: rpm
    * example: 15   

### Categorical quantities
??? "type_of_sputering"
    The carrier gas.

    * type: str
    * examples:
        * DC_sputtering
        * RF_sputtering
        * Magnetron_sputtering
        * Reactive_sputtering
        * Pulsed_DC_sputtering
        * other

??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system   

### Subsections
??? "segments"
    Repeating section. Details about the sputtering steps.
    {% include "data_schemas/experimental_procedures/subsections/sputtering_segment.md" %}

??? "target"
    Details about the sputtering target
    {% include "data_schemas/experimental_procedures/subsections/sputtering_target.md" %} 

??? "gases"
    Repeating section. Details about the gases involved. Primary ofr reactive sputtering
    {% include "data_schemas/experimental_procedures/subsections/gas_component.md" %}       