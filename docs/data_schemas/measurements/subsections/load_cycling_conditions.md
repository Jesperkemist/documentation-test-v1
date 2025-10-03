??? "number_of_cycles"
    The number of load cycles during the measurement.

    * type: int
    * example: 10  

??? "number_of_steps_in_cycle"
    The number of steps in the load cycle.

    * type: int
    * example: 10 

??? "segments"
    A repeating section detailing the conditions in each load step

    ??? "duration"
        The duration of the step

        * type: float
        * unit: minute
        * example: 60


    ??? "potential_bias_regime"
        The potential regime during the measurement e.g. open circuit, constant potential, constant current,  maximum powerpoint tracking, etc. 

        * type: str
        * options: 
            * MPPT
            * open_circuit
            * constant_potential
            * constant_current
            * constant_resistance
            * other

    ??? "potential"
        The potential the device is held at (if held at constant potential)

        * type: float
        * unit: V
        * example: 0.95

    ??? "current_density"
        The current density the device is held at (if held at constant current density)

        * type: float
        * unit: mA/cm^2
        * example: 21.5

    ??? "resistance"
        The resistance the device is held at (if held at constant resistance)

        * type: float
        * unit: mA/cm^2
        * example: 21.5 

    ??? "environmental_conditions"
        {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}  

    ??? "light_source"
        {% include "data_schemas/measurements/subsections/light_source.md" %}    

    ??? "illumination"
        {% include "data_schemas/measurements/subsections/illumination.md" %}          