??? "time_stamp_start"
    Date and time the measurement was started. 

    * type: datetime
    * example: 2020-07-08

??? "time_stamp_end"
    Date and time the measurement was ended. 

    * type: datetime
    * example: 2020-07-08    

??? "illuminated"
    TRUE if the device is illuminated during the stability evaluation. FALSE if the stability reefer to stability under dark conditions.

    * type: boolean
    * options: TRUE, FALSE 

??? "country"
    The country where the measurement was done.

    * type: str
    * example: "Sweden"     

??? "city"
    The city where the measurement was done.

    * type: str
    * example: "Uppsala"     

??? "latitude"
    The latitude of the measurement location.

    * type: str
    * units: degrees
    * example: 56.0425      

??? "longitude"
    The longitude of the measurement location.

    * type: str
    * units: degrees
    * example: 56.0425     

??? "tilt"
    The tilt of the device during the measurement.

    * type: str
    * units: degrees
    * example: 45     

??? "direction"
    The direction of the device during the measurement.
    * 0 is north
    * 90 is east
    * 180 is south
    * 270 is west

        * type: str
        * units: degrees
        * example: 45  

??? "number_of_solar_tracking_axes"
    The number of solar tracking axes. 0 means a stationary device.

    * type: int
    * example: 0 