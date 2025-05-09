??? "blend"
    The name of the OPV blend. Often in the form - "name of acceptor:"name of donor" 

    type: str
    example: P3HT:PCBM

??? "cell_type"
    The type of opv cell.  

    * type: str
    * options: 
        * singel_layer
        * bilayer
        * heterojunction
        * bulk_heterojunction
        * other

??? "peak_absorption_wavelength"
    The wavelength at maximum absorption 

    type: float
    unit: nm
    example: 550

??? "molar_extinction_coefficient"
    The molar extinction coefficient

    type: float
    unit: L*mol^1*cm^-1
    example: 10000   

??? "homo_level"
    The energy of the HOMO level

    type: float
    unit: eV
    example: 2.1 

??? "lumo_level"
    The energy of the LUMO level

    type: float
    unit: eV
    example: 2.3

