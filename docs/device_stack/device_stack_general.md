# Summary
This section contains a few useful quantities describing the stack sequence. <br/>
These can be populated automatically if proper data is added for all layers in the device"   

!!! tip "Tip : The following data can be populated automatically" 

??? "number_of_layers"
    The number of layers in the device.

    * type: int
    * example: 10 

??? "stack_sequence"
    A list of the materials in the layers of the stack. <br/>  
    If a proper device stack section is provided, the stack sequence can be generated from that one.

    * Start with the layer in the bottom of the device (i..e that is furthest from the sun) and work up from that.
    * If two materials, e.g. A and B, are mixed in one layer, list the materials in alphabetic order and separate them with semicolons, as in (A; B)
    * The perovskite layer is stated as “Perovskite”, regardless of composition, mixtures, dimensionality etc. Those details are provided elsewhere. 
    * Use common abbreviations when possible but spell them out when there is risk for confusion. <br/> <br/>  

        * type: list of strings
        * examples: 
            * [Ag, MoO3, OPV, PFNBr, Ag, MoO3, P3HT, Perovskite, SnO2, ITO, SLG]
            * [Ag, AZO, Silicon, ITO, 2PACz, Perovskite, LiF, C60, SnO2, AZO, Ag-grid, LiF]