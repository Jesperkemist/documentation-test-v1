# Outdoor performance

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "data_schemas/measurements/subsections/measurement_base_section.md" %}

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

### Subsections
<!-- ### Results -->
??? "results"
    Key performance metrics related to stability measurements. Typically, only a subset of these metrics can be extracted from a single stability measurement
    {% include "data_schemas/measurements/subsections/stability_metrics.md" %}          

<!-- ### Outdoor performance conditions -->
??? "outdoor_performance_details"
    Measurement details related to teh outdoor setting
    {% include "data_schemas/measurements/subsections/outdoor_performance_details.md" %}      

<!-- ### Measurement conditions -->
??? "measurement_conditions"
    Measurement details
    {% include "data_schemas/measurements/subsections/stability_details.md" %}       

<!-- ### Environmental conditions -->
??? "environmental_conditions"  
    A description of the environment
    {% include "data_schemas/measurements/subsections/environmental_conditions_outdoor.md" %}    


<!-- ### Load cycling -->
??? "load_cycling_conditions"
    Details about how the load of the cell have varied during the stability measurement
    {% include "data_schemas/measurements/subsections/load_cycling_conditions.md" %}     

<!-- ### Sample History -->
??? "sample_history"
    A description of the conditions under which the sample have been stored between the finalization of the device and the described measurement
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}


<!-- ### Certification details -->
??? "certification_details"
    Certification details
    {% include "data_schemas/measurements/subsections/certification_details.md" %}


<!-- ### JV measurements done during the stability measurement -->
??? "jv_measurements"
    A list if all JV measurements done during the stability measurement
    {% include "./JV.md" %}

### Raw data
The raw data for the measurement
The raw data can at the moment not be uploaded directly in the graphical interface. To add raw data, the data needs to be added manually to teh JSON file before being uploaded to NOMAD
??? "power_conversion_efficiency"
    A list of the PCE trace
    
    * type: list of floats
    * Example: [1, 2, 3, 4, ...]

??? "time"
    A list of the time trace
    
    * type: list of floats
    * Example: [1, 2, 3, 4, ...]