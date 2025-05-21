??? "ambient_conditions"
    TRUE if the activity is occurring in in uncontrolled ambient conditions. FALSE otherwise   
     
    * type: boolean
    * options: TRUE, FALSE

??? "in_glove_box"
    True if the the activity was performed in a glove box, False otherwise.
    
    * type: boolean
    * options: TRUE, FALSE

??? "atmosphere"
    Atmosphere during the activity.

    * type: str
    * options:
        * air 
        * dry_air 
        * N2 
        * Ar 
        * He 
        * O2 
        * H2 
        * vacuum 
        * other

??? "pressure"
    The atmospheric pressure during the activity.

    * type: float
    * unit: Pa
    * example: 101325

??? "ambient_temperature"
    Ambient temperature during the activity.

    * type: float
    * unit: C
    * example: 25

??? "device_temperature"
    The temperature of the device during the activity

    * type: float
    * unit: C
    * example: 25

??? "relative_humidity"
    Relative humidity during the activity.

    * type: float
    * unit: %
    * example: 45

??? "oxygen_concentration"
    The oxygen concentration during the activity.

    * type: float
    * unit: %
    * example: 0.001
