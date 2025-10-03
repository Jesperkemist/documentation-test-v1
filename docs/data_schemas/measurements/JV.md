# JV

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "data_schemas/measurements/subsections/measurement_base_section.md" %}

??? "light_regime"
    The light regime during the JV measurement e.g. Standard light (AM 1.5), Dark, Concentrated light, Indoor light, Other 
   
    * type: str
    * options: 
        * standard_light
        * concentrated_light
        * indoor_light
        * dark
        * other

??? "preconditioned"
    TRUE if the device has been preconditioned before the measurement, FALSE otherwise. <br/>
    If TRUE, additional details are found in the preconditioning subsection
    
    * type: boolean
    * options: TRUE, FALSE

### Subsections
??? "results"
    Key performance metrics that can be extracted from the IV-curve
    {% include "data_schemas/measurements/subsections/JV_metrics.md" %}

<!-- ### Measurement conditions -->
??? "measurement_conditions"
    Measurement details for the JV scan
    {% include "data_schemas/measurements/subsections/JV_details.md" %}

<!-- ### Environmental conditions -->
??? "environmental_conditions"
    A description of the environment
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}

<!-- ### Light source -->
??? "light_source"
    Details about the light source used for the measurement.
    {% include "data_schemas/measurements/subsections/light_source.md" %}

<!-- ### Illumination -->
??? "illumination"
    Details about the illumination used for the measurement.
    {% include "data_schemas/measurements/subsections/illumination.md" %}

<!-- ### Preconditioning -->
??? "preconditioning_conditions"
    Details about any preconditioning program done before the measurement
    {% include "data_schemas/measurements/subsections/preconditioning.md" %}

<!-- ### Sample History -->
??? "sample_history"
    A description of the conditions under which the sample have been stored between the finalization of the device and the described measurement
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}

<!-- ### Certification details -->
??? "certification_details"
    Certification details
    {% include "data_schemas/measurements/subsections/certification_details.md" %}

### Raw data
The raw data for the measurement
The raw data can at the moment not be uploaded directly in the graphical interface. To add raw data, the data needs to be added manually to teh JSON file before being uploaded to NOMAD
??? "current"
    A list of the current density trace
    
    * type: list of floats
    * Example: [1, 2, 3, 4, ...]

??? "voltage"
    A list of the voltage trace
    
    * type: list of floats
    * Example: [1, 2, 3, 4, ...]
