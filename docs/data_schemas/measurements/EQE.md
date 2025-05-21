# EQE

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "data_schemas/measurements/subsections/measurement_base_section.md" %}

??? "preconditioned"
    TRUE if the device has been preconditioned before the measurement, FALSE otherwise. <br/>
    If TRUE, additional details are found in the preconditioning subsection
    
    * type: boolean
    * options: TRUE, FALSE

??? "bias_light"
    TRUE if the measurement is done under bias light, FALSE otherwise.

    * type: boolean
    * options: TRUE, FALSE

### Subsections
<!-- ### Results -->
??? "results"
    Key performance metrics that can be extracted from the measurement
    {% include "data_schemas/measurements/subsections/EQE_metrics.md" %}

<!-- ### EQE details -->
??? "measurement_conditions"
    Measurement details for the EQE measurement
    {% include "data_schemas/measurements/subsections/EQE_details.md" %}

<!-- ### Bias light -->
??? "bias_light_source"
    Details about the light source used for the bias light.
    {% include "data_schemas/measurements/subsections/light_source.md" %}

<!-- ### Bias illumination -->
??? "bias_illumination"
    Details about the bias light source used for the measurement.
    {% include "data_schemas/measurements/subsections/illumination.md" %}

<!-- ### Environmental conditions -->
??? "environmental_conditions"
    A description of the environment
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}

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

TODO. Left to implement        