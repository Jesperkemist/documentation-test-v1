# General

This section stores general data that classifies the type of device. <br/>
This data is useful for filtering the database


### Categorical classes
These are categorical key-value pairs defining the type of device

??? "architecture"
    The general architecture of the tandem device. <br/> 
    4-terminal devices and other configurations where independent sub cells simply are stacked on top of each other should be define as “stacked”

    * type: str
    * options: 
        * Monolithic
        * Stacked
        * Laminated
        * Spectral_splitter
        * Wide_bandgap_cell_used_as_reflector
        * Other

??? "number_of_terminals"
    The number of terminals in the device. The most common configurations are 2 and 4

    * type: int
    * example: 2

??? "number_of_junctions"
    The number of junctions in the device

    * type: int
    * example: 2

??? "photoabsorbers"
    List of the photoabsorbers. <br/> 
    The list should start from bottom of the device stack and going upwards, i.e. The photo absorber with the lowest band gap is typically first. 

    * type: List of strings
    * examples: 
        * ["CIGS", "Perovskite"]
        * ["Silicon", "Perovskite"]
        * ["Perovskite", "Perovskite"]
        * ["Silicon", "Perovskite", "Perovskite"]
        * ["OPV", "Perovskite"]

??? "photoabsorbers_bandgaps"
    List of the band gap values of the respective photoabsorbers. <br/>
    - The order of band gaps should line up with the list of photoabsorbers. <br/>
    - If there are uncertainties, state the best estimate, e.g write 1.5 and not 1.45-1.55 <br/>
    - Every photo absorber has a band gap. If it is unknown, state it as ‘nan’

    * type: list of floats
    * unit: eV
    * examples:
        * [1.1, 1.65]
        * [1.1, 1.60, 1.93]

??? "subcell_origin"
    A list of the origin of each subcell, i.e. if it is lab made or commercially bought. <br/>
    The list should start with the bottom cell (i.e. the cell furthers from the sun) and work upwards. <br/> 
    For a monolithic device, there is no hard boundary between the top and the bottom cell, but it is usually quite clear if one part was bought commercially. <br/> 
    Each entry (subcell) in the list comes with the following key-value pairs.

    ??? "commercial"
        TRUE if the sub cell was bought commercially, FALSE if it is a lab-made unit. <br/>
        
        * type: boolean
        * options: TRUE, FALSE

    ??? "supplier"
        Supplier of the subcell. i.e. the name of the company (if commercial) or the lab/research group if lab made

        * type: str
        * example: 
            * First-solar
            * Hysprint lab, HZB

??? "production_date"
    Date the device was finalized.

    * type: datetime
    * example: 2025-02-08


### Physical footprint
These are key-value pairs describing the physical footprint of the device
??? "substrate_area"
    The total area of the substrate on which the device is deposited. 

    * type: float
    * unit: cm^2
    * example: 6.35 

??? "cell_area"
    The total area of the cell. The dark area. Is typically defined as the overlap between the front and back contacts. 

    * type: float
    * unit: cm^2
    * example: 1.0 

??? "active_area"
    The effective area of the cell during IV and stability measurements under illumination. If measured with a mask, this corresponds to the area of the hole in the mask. Otherwise this area is the same as the cell area.

    * type: float
    * unit: cm^2
    * example: 0.16 

??? "number_of_cells"
    The number of individual solar cells, or pixels, on the substrate on which the reported cell is made.

    * type: int
    * example:4 


### Boolean categories
These are boolean filters that simplify data search and filtering. More detailed data for cases where the flag is TRUE is found in specialized sections   

??? "flexible"
    TRUE if the device is flexible and bendable, FALSE if it is rigid. <br/>
    Further details in the measurement section 

    * type: boolean
    * options: TRUE, FALSE

??? "semitransparent"
    TRUE if the device is semitransparent. That is usually only the case when there are no thick completely covering metal electrodes. FALSE if it is opaque <br/>
    Further details in the measurement section    

    * type: boolean
    * options: TRUE, FALSE

??? "encapsulated"
    True if the cell is encapsulated. <br/>
    
    * type: boolean
    * options: TRUE, FALSE

??? "contains_textured_layers"
    TRUE if the device contains textured layers with the purpose of light management. <br/>
    Further details in subsections for the specific textured layers    

    * type: boolean
    * options: TRUE, FALSE

??? "contains_antireflective_coating"
    TRUE if the device contains one or more anti reflective coatings or other layers specifically dealing with light management. <br/>
    Further details in subsections for the specific textured layers        

    * type: boolean
    * options: TRUE, FALSE

??? "bifacial"
    True if the cell is bifacial, i.e. design to absorb light from both sides. <br/>
    
    * type: boolean
    * options: TRUE, FALSE

??? "module"
    TRUE if device is a module composed of several identical cells located side by side, either in series or in parallel. <br/>
    Should only one of the subcells in a stacked monolithic device be a module, mark this as true, and provide more details in the dedicated module section.  
    Further details in the module section    

    * type: boolean
    * options: TRUE, FALSE    


### Derived quantities
Useful quantities that automatically can be derived from other data

??? "photoabsorbers_string"
    A single string describing the combination of photoabsorbers in the cell. <br/> 
    Concatenate the photoabsorber names with a - <br/> 
    Can be generated automatically from the photoabsorbers field.

    * str
    * examples: 
        * 'CIGS-Perovskite'
        * 'Perovskite-OPV'
        * 'Silicon-Perovskite'
        * 'Perovskite-Perovskite'
        * 'Silicon-Perovskite-Perovskite'


??? "stack_sequence_string"
    A single string describing the stack sequence of the cell. <br/> 
    If a proper device stack section is provided, the stack sequence can be generated from that one. <br/> 
    This is a concatenation of the stack sequence, which is handy for searching and filtering the data. 

    * type: list of strings
    * examples: 
        * "Ag | AZO | Silicon | ITO | 2PACz | Perovskite | LiF | C60 | SnO2 | AZO | Ag-grid | LiF"
        * "Ag | MoO3 | OPV | PFNBr | Ag | MoO3 | P3HT | Perovskite | SnO2 | ITO | SLG"
      