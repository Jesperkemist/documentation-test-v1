# Stability

### Measurement classification
Data that describe the type of measurement and on what it has been performed on

{% include "data_schemas/measurements/subsections/measurement_base_section.md" %}

??? "illuminated"
    TRUE if the device is illuminated during the stability evaluation. FALSE if the stability reefer to stability under dark conditions

    * type: boolean
    * options: TRUE, FALSE

??? "load_cycling"
    TRUE if the load have been cycled during the stability measurements

    * type: boolean
    * options: TRUE, FALSE    


??? "stability_protocol"
    The measurement protocol. For definitions and classifications of stability protocols, see https://www.nature.com/articles/s41560-019-0529-5   

    * type: str
    * options: 
        * ISOS-D-1
        * ISOS-D-1I
        * ISOS-D-2
        * ISOS-D-2I
        * ISOS-D-3
        * ISOS-V-1
        * ISOS-V-1I
        * ISOS-V-2
        * ISOS-V-2I
        * ISOS-V-3
        * ISOS-L-1
        * ISOS-L-1I
        * ISOS-L-2
        * ISOS-L-2I
        * ISOS-L-3
        * ISOS-O-1
        * ISOS-O-2
        * ISOS-O-3
        * ISOS-T-1
        * ISOS-T-1I
        * ISOS-T-2
        * ISOS-T-2l
        * ISOS-T-3
        * ISOS-T-3I
        * ISOS-LC-1
        * ISOS-LC-1I
        * ISOS-LC-2
        * ISOS-LC-2I
        * ISOS-LC-3
        * ISOS-LC-3I
        * ISOS-LT-1
        * ISOS-LT-2
        * ISOS-LT-3
        * IEC 61215
        * Other    

### Subsections
<!-- ### Results -->
??? "results"
    Key performance metrics related to stability measurements. Typically, only a subset of these metrics can be extracted from a single stability measurement
    {% include "data_schemas/measurements/subsections/stability_metrics.md" %}    

<!-- ### Measurement conditions -->
??? "measurement_conditions"
    Measurement details for the JV scan
    {% include "data_schemas/measurements/subsections/stability_details.md" %}    

<!-- ### Environmental conditions -->
??? "environmental_conditions"
    A description of the environment
    {% include "data_schemas/measurements/subsections/environmental_conditions.md" %}    

<!-- ### Illumination -->
??? "illumination"
    Details about the illumination used for the measurement.
    {% include "data_schemas/measurements/subsections/illumination.md" %} 

<!-- ### Light source -->
??? "light_source"
    Details about the light source used for the measurement.
    {% include "data_schemas/measurements/subsections/light_source.md" %}       


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
TODO. Left to implement