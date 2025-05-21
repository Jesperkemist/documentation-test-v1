??? "scan_direction"
    The scan direction of the JV measurement. Forward or reverse. 

    * type: str
    * options: 
        * forward
        * reverse

??? "scan_speed"
    Speed of the voltage scan. 

    * type: float
    * unit: mV/s
    * example: 10   

??? "voltage_step"
    Voltage step of the scan.

    * type: float
    * unit: mV
    * example: 2.5  

??? "delay_time"
    Delay time before the scan.

    * type: float
    * unit: milliseconds
    * example: 2.5      

??? "integration_time"
    Integration time of the scan.

    * type: float
    * unit: milliseconds
    * example: 2.5 

??? "source_meter"
    Brand name and model of the Source-meter used for the measurement.

    * type: str
    * example: "Keithley 2600"      