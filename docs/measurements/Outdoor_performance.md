# Outdoor performance

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "./subsections/measurement_base_section.md" %}

??? "load_cycling"
    TRUE if the load have been cycled during the stability measurements

    * type: boolean
    * options: TRUE, FALSE 

??? "stability_protocol"
    The measurement protocol. For definitions and classifications of stability protocols, see https://www.nature.com/articles/s41560-019-0529-5   

    * type: str
    * options: 
        * ISOS-O-1
        * ISOS-O-2
        * ISOS-O-3
        * Other    

### Results
Key performance metrics related to stability measurements. Typically, only a subset of these metrics can be extracted from a single stability measurement

???+ "results"
    {% include "./subsections/stability_metrics.md" %}          

### Outdoor performance conditions
Measurement details for the JV scan

???+ "measurement_conditions"
    {% include "./subsections/outdoor_performance_details.md" %}      

### Measurement conditions
Measurement details for the JV scan

???+ "measurement_conditions"
    {% include "./subsections/stability_details.md" %}       

### Environmental conditions
A description of the environment

???+ "environmental_conditions"
    {% include "./subsections/environmental_conditions_outdoor.md" %}    


### Load cycling
Details about how the load of the cell have varied during the stability measurement

???+ "load_cycling_conditions"
    {% include "./subsections/load_cycling_conditions.md" %}     

### Sample History
A description of the conditions under which the sample have been stored between the finalization of the device and the described measurement

???+ "sample_history"
    {% include "./subsections/environmental_conditions.md" %}


### Certification details
Certification details

???+ "certification_details"
    {% include "./subsections/certification_details.md" %}


### JV measurements done during the stability measurement
??? "jv_measurements"
    A list if all JV measurements done during the stability measurement
    {% include "./JV.md" %}

### Raw data
The raw data for the measurement
TODO. Left to implement    