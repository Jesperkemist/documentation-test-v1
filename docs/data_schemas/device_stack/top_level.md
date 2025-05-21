# device_stack

### Layers
The main object in the device_stack subsection is a list of all the layers in the device.
The layer object can be a deeply nested object, and is described in more detail under "layers" in the menu to the left.  
??? "layers"
    A list of all the layers in the device stack with all the relevant properties for each layer. Should start with the layer in the bottom of the device (i.e. the layer that is furthest from the sun). 

    * type: list of layer objects
    * example: [{"name":"TiO2-mp"},{"name":"Perovskite"},{"name":"C60}] 


### Derived quantities
!!! tip "Tip : The following data can be populated automatically" 

??? "n_layers"
    The number of layers in the device.

    * type: int
    * example: 10 

<!-- ??? "stack_sequence"
    A list of the materials in the layers of the stack. <br/>  
    If a proper device stack section is provided, the stack sequence can be generated from that one.

    * Start with the layer in the bottom of the device (i..e that is furthest from the sun) and work up from that.
    * If two materials, e.g. A and B, are mixed in one layer, list the materials in alphabetic order and separate them with semicolons, as in (A; B)
    * The perovskite layer is stated as “Perovskite”, regardless of composition, mixtures, dimensionality etc. Those details are provided elsewhere. 
    * Use common abbreviations when possible but spell them out when there is risk for confusion. <br/> <br/>  

        * type: list of strings
        * examples: 
            * [Ag, MoO3, OPV, PFNBr, Ag, MoO3, P3HT, Perovskite, SnO2, ITO, SLG]
            * [Ag, AZO, Silicon, ITO, 2PACz, Perovskite, LiF, C60, SnO2, AZO, Ag-grid, LiF] -->



??? "stack_sequence"
    A single string describing the stack sequence of the cell. <br/>
    Is constructed by concatenation the name of each layer in the stack sequence, which is handy for searching and filtering the data. The name of the layer should typically be the material in the layer. Should start with the layer in the bottom of the device (i.e. the layer that is furthest from the sun)
    If a proper device stack section is provided, the stack sequence can be generated automatically. <br/> 

    * type: str
    * examples: 
        * "Ag | AZO | Silicon | ITO | 2PACz | Perovskite | LiF | C60 | SnO2 | AZO | Ag-grid | LiF"
        * "Ag | MoO3 | OPV | PFNBr | Ag | MoO3 | P3HT | Perovskite | SnO2 | ITO | SLG"            