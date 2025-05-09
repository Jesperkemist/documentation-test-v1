# JV

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "./subsections/measurement_base_section.md" %}

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

### Results
Key performance metrics that can be extracted from the IV-curve

???+ "results"
    {% include "./subsections/JV_metrics.md" %}

### Measurement conditions
Measurement details for the JV scan

???+ "measurement_conditions"
    {% include "./subsections/JV_details.md" %}


### Environmental conditions
A description of the environment

???+ "environmental_conditions"
    {% include "./subsections/environmental_conditions.md" %}

### Light source
Details about the light source used for the measurement.

???+ "light_source"
    {% include "./subsections/light_source.md" %}

### Illumination
Details about the illumination used for the measurement.

???+ "illumination"
    {% include "./subsections/illumination.md" %}

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

