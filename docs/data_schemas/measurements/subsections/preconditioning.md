??? "protocol"
    Protocol for the preconditioning. Light soaking, potential biasing, etc. 
   
    * type: str
    * options: 
        * Light_soaking
        * Potential_biasing
        * Current_biasing
        * Temperature_biasing
        * Other

??? "duration"
    Time of the preconditioning program.

    * type: float
    * unit: s
    * example: 120

??? "potential"
    Potential during the activity..

    * type: float
    * unit: V
    * example: 0.9

??? "light_intensity"
    Light intensity during the activity.

    * type: float
    * unit: 'W/m^2'
    * example: 1000

??? "current_density"
    Current density during the activity..

    * type: float
    * unit: mA/cm^2
    * example: 25    


??? "environmental_conditions"
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}

     