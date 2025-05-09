# Layers in the device
* A list of layers
* Elaborate on how to numerate layers. Starting from the bottom

## Top layer quantities for the layer
??? "name"
    A sensible name for the layer. A good default is the trade name of the material, possibly with an addition of the microstructure.  

    * type: str
    * examples: 
        * TiO2-mp
        * PEDOT:PSS
        * Spiro-MeOTAD
        * SLG
        * ITO

??? "sub_device_identity"
    If the device not is monolithic, this describes which individual subcell the layer belongs to.  

    - 0 = the layer belongs to a monolithic device 
    - 1 = the layer belongs to the bottom subcell, 
    - 2 = the layer belongs to the second subcell (top cell in a 2-junction device)
    - 3 = the layer belongs to the third subcell (top cell in a 3-junction device)

        * type: int
        * example: 0

??? "functionality"
    The primary functionality of the layer in the device stack.

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
        * optical_spacer
        * photoabsorber
        * recombination_layer
        * refractive_index_matching
        * self_assembled_monolayer
        * subcell_spacer
        * substrate
        * upconversion
        * window_layer
        * other


## Photoabsorber properties
Photoabsorbers have been given somewhat more elaborate data sections that other layer. For photoabsorber layers, use those sections, which overwrites some of the more general sections used for the other layers. 

<!-- ### Perovskites -->
??? "perovskite"
    {% include "device_stack/subsections/perovskite.md" %}

<!-- ### Silicon -->
??? "silicon"
    {% include "device_stack/subsections/photoabsorber_silicon.md" %}

<!-- ### CIGS -->
??? "CIGS"
    {% include "device_stack/subsections/photoabsorber_CIGS.md" %}

??? "CZTS"
    {% include "device_stack/subsections/photoabsorber_CZTS.md" %}

??? "OPV"
    {% include "device_stack/subsections/photoabsorber_OPV.md" %}

??? "DSSC"
    {% include "device_stack/subsections/photoabsorber_DSSC.md" %}

??? "quantum_dot"
    {% include "device_stack/subsections/photoabsorber_qd.md" %}

## Subsections    
<!-- ### Components in layer -->
{% include "device_stack/subsections/components.md" %}

<!-- ### Deposition procedure -->
{% include "device_stack/subsections/deposition_procedure.md" %}             

<!-- ### Post deposition procedure -->
{% include "device_stack/subsections/post_deposition_procedures.md" %}   

<!-- ### Sample History -->
??? "sample_history"
    A description of the conditions under which the sample have been stored between the finalization of the previous layer and this layer
    {% include "device_stack/subsections/sample_history.md" %}

<!-- ### Layer properties -->
??? "properties"
    Properties of the layer. Each property is encapsulated in its own subsection
    {% include "device_stack/subsections/layer_properties.md" %}

## Derived properties
??? "layer_index"
    The position in the device stack for the layer. Counted from the bottom. Can be populated automatically 

    * unit: int
    * example: 3  