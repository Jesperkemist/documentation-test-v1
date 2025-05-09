# Module data
This section provides data needed to describe module properties, if the device is a module or contains subcells that are modules

### Top level data

??? "monolithic_module"
    TRUE if the device is a monolithic module 

    * type: boolean
    * options: TRUE, FALSE


??? "contains_monolithic_subcell"
    TRUE if one or more of the subcells are modules

    * type: boolean
    * options: TRUE, FALSE


### Module specific data
Data that describes each module in the stack. <br/>
Data is stored in a list in case there are more than one module in the device stack. 

??? "subcell_association"
    The subcells that are part of this module. Enumerate the cells from 1 to n, where n is the number of subcells to
    in the module. Start counting from the bottom. For example, if the module is made of subcells 1 and 2, then the value should be 1,2. <br/>
    If the module is made of subcells 2 and 3, then the value should be 2,3.
    For a monolithic module, the values should be 1, .., n, where n is the number of subcells in the device

    * type: str
    * example: 
        * '1'
        * '2'
        * '1, 2'
        * '2, 3'
        * '1, 2, 3'

??? "number_of_cells"
    The number of cells in the module.

    * type: int
    * example:4   

??? "total_area"
    The total area of the module. 

    * type: float
    * unit: cm^2
    * example: 6.35 

??? "active_area"
    The active area of the module. 

    * type: float
    * unit: cm^2
    * example: 1.0 

??? "cell_area"
    The total area of each individual cell.

    * type: float
    * unit: cm^2
    * example: 0.16 

??? "scribe_width"
    The width of the scribe lines separating the cells.

    * type: float
    * unit: mm
    * example: 1.5
      