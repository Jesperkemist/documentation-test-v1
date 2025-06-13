???+ "m_def"
    Should be: "perovskite_solar_cell_database.schema_packages.tandem.device_stack.Photoabsorber_Silicon" <br>
    This is needed to be able to take advantage of normalization functionality in the NOMAD database

<!-- ### Layer -->
{% include "data_schemas/device_stack/layers/layer.md" %}   

??? "cell_type"
    The type of silicon cell

    * type: str
    * options:
        * Amorphous 
        * Al-BSF
        * c-type 
        * HIT
        * HJT
        * Heterojunction
        * Homojunction
        * IBC 
        * n-type
        * p-type
        * PERC        
        * PERL
        * SC/nFAB
        * TOPCon
        * other

??? "type_of_silicon"
    The type of silicon

    * type: str
    * options: 
        * Amorphous
        * Monocrystalline 
        * Polycrystalline
        * CZ
        * Float-zone
        * other

??? "doping_sequence"
    Description of the doping sequence

    * type: str
    * example: np

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
??? "layer_index"
    The position in the device stack for the layer. Counted from the bottom. Can be populated automatically 

    * unit: int
    * example: 3  