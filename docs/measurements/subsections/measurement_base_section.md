??? "time_stamp"
    Date the measurement was performed (or started in in case of multi-day measurements). 

    * type: datetime
    * example: 2020-07-08

??? "age_of_device"
    Age of the device at the time of measurement start.

    * type: float
    * unit: h
    * example: 48

??? "duration"
    Duration of the measurement.

    * type: float
    * unit: minute
    * example: 2.5

??? "certified"
    TRUE if the measurement was certified by an external certification institute, FALSE otherwise.

    * type: boolean
    * options: TRUE, FALSE

??? "device_subset"
    Describes if the measurement was done on the compleat device or on an individual subcell.  

    - 0 = measurement was done on the complete device, 
    - 1 = measurement was done on the bottom subcell, 
    - 2 = measurement was done on the second subcell (top cell in a 2-junction device)
    - 3 = measurement was done on the third subcell (top cell in a 3-junction device)

        * type: int
        * example: 0
 