# layers
A list of the layers in the device
Should start with the layer in the bottom of the device (i.e. the layer that is furthest from the sun)
Below are a description of key-value pairs and subsections for each layer

### Top level
??? "name"
    A sensible name for the layer. A good default is the trade name of the material, possibly with an addition of the microstructure.  

    * type: str
    * examples: 
        * TiO2-mp
        * PEDOT:PSS
        * Spiro-MeOTAD
        * SLG
        * ITO

??? "device_subset"
    If the device not is monolithic, this describes which individual subcell the layer belongs to.  

    - 0 = the layer belongs to a monolithic device 
    - 1 = the layer belongs to the bottom subcell, 
    - 2 = the layer belongs to the second subcell (top cell in a 2-junction device)
    - 3 = the layer belongs to the third subcell (top cell in a 3-junction device)

        * type: int
        * example: 0

??? "functionality"
    The primary functionality the layer has in the device stack.

    * type: str
    * options:
        * air_gap
        * anti_reflection
        * back_contact
        * back_reflector
        * buffer_layer
        * down_conversion
        * edge_sealing
        * electrolyte
        * encapsulation
        * electron_transport_layer
        * front_contact
        * hole_transport_layer
        * interface_modifier
        * mesoporous_scaffold
        * middle_contact
        * organic_dye
        * optical_spacer
        * photoabsorber
        * recombination_layer
        * refractive_index_matching
        * self_assembled_monolayer
        * spectral_splitter
        * subcell_spacer
        * substrate
        * transparent_conducting_oxide
        * up_conversion
        * window_layer
        * other


## Photoabsorber properties
Photoabsorbers have been given somewhat more elaborate data sections that other layer. For photoabsorber layers, use those sections, which provides additional data compared to the more general sections used for the other layers. 

??? "perovskite"
    {% include "data_schemas/device_stack/photoabsorbers/perovskite.md" %}

??? "silicon"
    {% include "data_schemas/device_stack/photoabsorbers/silicon.md" %}

??? "CIGS"
    {% include "data_schemas/device_stack/photoabsorbers/CIGS.md" %}

??? "CZTS"
    {% include "data_schemas/device_stack/photoabsorbers/CZTS.md" %}

??? "OPV"
    {% include "data_schemas/device_stack/photoabsorbers/OPV.md" %}

??? "DSSC"
    {% include "data_schemas/device_stack/photoabsorbers/DSSC.md" %}

??? "quantum_dot"
    {% include "data_schemas/device_stack/photoabsorbers/quantum_dot.md" %}

??? "GaAs"
    {% include "data_schemas/device_stack/photoabsorbers/GaAs.md" %}

## Subsections    
<!-- ### Components in layer -->
{% include "data_schemas/device_stack/materials/components.md" %}

<!-- ### Deposition procedure -->
{% include "data_schemas/device_stack/deposition_procedure.md" %}             

<!-- ### Post deposition procedure -->
{% include "data_schemas/device_stack/subsections/post_deposition_procedures.md" %} 

<!-- ### Sample History -->
<!-- ??? "sample_history"
    A description of the conditions under which the sample have been stored between the finalization of the previous layer and this layer
    {% include "data_schemas/device_stack/subsections/sample_history.md" %} -->

<!-- ### Layer properties -->
??? "properties"
    Properties of the layer. Each property is encapsulated in its own subsection
    {% include "data_schemas/device_stack/properties.md" %}

## Derived properties
??? "layer_index"
    The position in the device stack for the layer. Counted from the bottom. Can be populated automatically 

    * unit: int
    * example: 3  