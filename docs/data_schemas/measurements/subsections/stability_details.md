??? "potential_bias_regime"
    The potential regime during the measurement e.g. open circuit, constant potential, constant current,  maximum powerpoint tracking, etc. 

    * type: str
    * options: 
        * Maximum_powerpoint_tracking
        * open_circuit
        * constant_potential
        * constant_current
        * constant_resistance
        * other

??? "periodic_jv_measurements"
    TRUE if there has been a periodicity to the load of the cell in terms of for example potential, current, resistance, or temperature during the stability measurements

    * type: boolean
    * options: TRUE, FALSE 

??? "evaluation_periodicity"
    If the device is evaluated by periodically doing JV-measurements (as common for evaluation of stability in the dark, state the length between the measurements) 

    * type: float
    * unit: h
    * example: 24


??? "potential"
    The potential the device is held at (if measured at constant potential)

    * type: float
    * unit: V
    * example: 0.95

??? "current_density"
    The current density the device is held at (if measured at constant current density)

    * type: float
    * unit: mA/cm^2
    * example: 21.5

??? "resistance"
    The resistance the device is held at (if measured at constant resistance)

    * type: float
    * unit: ohm
    * example: 21.5    

??? "source_meter"
    Brand name and model of the Source-meter used for the measurement.

    * type: str
    * example: "Keithley 2600" 

