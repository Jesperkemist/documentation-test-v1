??? "power_conversion_efficiency_start"
    Power conversion efficiency at the start of the measurement. 

    * type: float
    * unit: %
    * example: 22.3

??? "power_conversion_efficiency_end"
    Power conversion efficiency at the end of the measurement. 

    * type: float
    * unit: %
    * example: 18.2

??? "burn_in"
    TRUE if if an initial burn in period is observed. FALSE otherwise.

    * type: boolean
    * options: TRUE, FALSE

??? "burn_in_length"
    Length of the burn in period

    * type: float
    * unit: h
    * example: 2.5

??? "power_conversion_efficiency_after_burn_in"
    Power conversion efficiency at the end of the burn in phase. 

    * type: float
    * unit: %
    * example: 20.3    

??? "power_conversion_efficiency_1000h"
    Power conversion efficiency after 1000h. 

    * type: float
    * unit: %
    * example: 17.5

??? "T95"
    The time after which the cell have degraded to 95 % of the initial efficiency.  

    * type: float
    * unit: h
    * example: 150    

??? "T95s"
    The time after which the cell have degraded to 95 % of the efficiency reached after the initial burn in period. 

    * type: float
    * unit: h
    * example: 150  

??? "T80"
    The time after which the cell have degraded to 80 % of the initial efficiency 

    * type: float
    * unit: h
    * example: 150    

??? "T80s"
    The time after which the cell have degraded to 80 % of the efficiency reached after the initial burn in period 

    * type: float
    * unit: h
    * example: 150  

??? "energy_yield"
    The energy yield during the measurement. 

    * type: float
    * unit: 'kWh/m^2'
    * example: 230    

??? "energy_yield_average"
    The yearly average energy yield during the measurement. 

    * type: float
    * unit: 'kWh/m^2/year'
    * example: 1100       