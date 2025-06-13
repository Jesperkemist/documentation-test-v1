???+ "m_def"
    Should be: "perovskite_solar_cell_database.schema_packages.tandem.device_stack.Photoabsorber_GaAs" <br>
    This is needed to be able to take advantage of normalization functionality in the NOMAD database

<!-- ### Layer -->
{% include "data_schemas/device_stack/layers/layer.md" %}   

## Subsections
<!-- ### Deposition procedure -->
{% include "data_schemas/device_stack/deposition_procedure.md" %}             

<!-- ### Post deposition procedure -->
{% include "data_schemas/device_stack/subsections/post_deposition_procedures.md" %} 

<!-- ### Layer properties -->
??? "properties"
    Properties of the layer. Each property is encapsulated in its own subsection
    {% include "data_schemas/device_stack/properties.md" %}

<!-- ### Components in layer -->
{% include "data_schemas/device_stack/materials/components.md" %}

## Derived properties
??? "molecular formula"
    GaAs

    * type: 
    * example: GaAs

??? "layer_index"
    The position in the device stack for the layer. Counted from the bottom. Can be populated automatically 

    * type: int
    * example: 3  