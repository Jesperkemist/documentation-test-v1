### Boolean quantities
??? "uv_illuminated"
    TRUE if the if the samples is illuminated by UV-light. FALSE if samples only are treated with ozone. 

    * type: boolean
    * options: TRUE, FALSE 

### Numerical quantities
??? "duration"
    The total time of the procedure. 

    * type: float
    * unit: s
    * example: 60

??? "substrate_temperature"
    The temperature of the substrate/sample during the activity. 

    * type: float
    * unit: C
    * example: 35    

??? "uv_wavelength"
    The wavelength of the UV light.

    * type: float
    * unit: W/m^2
    * example: 50  

??? "uv_intensity"
    Intensity of the illumination.

    * type: float
    * unit: W/m^2
    * example: 50   


### Categorical quantities
??? "equipment"
    Brand name and model of the equipment used for the activity.

    * type: str
    * example: homebuilt_system

### Subsections
??? "environmental_conditions"
    {% include "data_schemas/experimental_procedures/subsections/environmental_conditions_deposition.md" %}      