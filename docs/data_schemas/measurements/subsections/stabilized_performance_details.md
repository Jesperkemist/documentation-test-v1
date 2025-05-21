??? "type_of_measurement"
    Type of measurement 

    * type: str
    * options: 
        * Constant_potential
        * Constant_current
        * Maximum_powerpoint_tracking
 
??? "potential"
    The potential (if measured at constant potential)'

    * type: float
    * unit: V
    * example: 1.05  

??? "current_density"
    The current density (if measured at constant current)

    * type: float
    * unit: mA/cm^2'
    * example: 17.8     

??? "source_meter"
    Brand name and model of the Source-meter used for the measurement.

    * type: str
    * example: "Keithley 2600"