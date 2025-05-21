??? "intensity"
    Intensity of the illumination. AM 1.5 is 1000 W/m^2

    * type: float
    * unit: 'W/m^2'
    * example: 1000


??? "illuminance"
    Illuminance of the illumination. Mostly important for low light indoor measurements.

    * type: float
    * unit: 'lx'
    * example: 320   

??? "direction"
    Direction of the illumination with respect to the device

    * type: str
    * options:
        * substrate 
        * superstrate

??? "mask"
    TRUE if a shadow mask used during the measurement.
    
    * type: boolean
    * options: TRUE, FALSE

??? "mask_area"
    Area of the shadow mask used during the measurement.

    * type: float
    * unit: 'cm^2'
    * example: 0.16   

??? "uv_filter"
    TRUE if a UV-filter is used. FALSE otherwise.
    
    * type: boolean
    * options: TRUE, FALSE

??? "top_cell_filter"
    TRUE if the measurement is done on a subcell and the light is filtered trough the remaining subcells. e.g. a silicon bottom cell is measured under light flittered by a perovskite top cell. 
    
    * type: boolean
    * options: TRUE, FALSE