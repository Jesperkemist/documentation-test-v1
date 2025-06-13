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

