# EQE

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "./subsections/measurement_base_section.md" %}

??? "preconditioned"
    TRUE if the device has been preconditioned before the measurement, FALSE otherwise. <br/>
    If TRUE, additional details are found in the preconditioning subsection
    
    * type: boolean
    * options: TRUE, FALSE

??? "bias_light"
    TRUE if the measurement is done under bias light, FALSE otherwise.

    * type: boolean
    * options: TRUE, FALSE

### Results
Key performance metrics that can be extracted from the measurement

???+ "EQE_conditions"
    {% include "./subsections/EQE_metrics.md" %}

### EQE details
Measurement details for the EQE measurement

???+ "measurement_details"
    {% include "./subsections/EQE_details.md" %}

### Bias light
Details about the light source used for the bias light.

???+ "bias_light_source"
    {% include "./subsections/light_source.md" %}

### Bias illumination
Details about the bias light source used for the measurement.

???+ "illumination"
    {% include "./subsections/illumination.md" %}

### Environmental conditions
A description of the environment

???+ "environmental_conditions"
    {% include "./subsections/environmental_conditions.md" %}

### Preconditioning
Details about any preconditioning program done before the measurement

???+ "preconditioning"
    {% include "./subsections/preconditioning.md" %}    

### Sample History
A description of the conditions under which the sample have been stored between the finalization of the device and the described measurement

???+ "sample_history"
    {% include "./subsections/environmental_conditions.md" %}

### Certification details
Certification details

???+ "certification_details"
    {% include "./subsections/certification_details.md" %}

### Raw data
The raw data for the measurement

TODO. Left to implement        