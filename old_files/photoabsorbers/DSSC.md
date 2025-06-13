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

??? "oxidation_potential"
    The oxidation potential vs the normal hydrogen electrode

    type: float
    unit: V
    example: 0.5

??? "dye"
    Information about the dye
    {% include "data_schemas/device_stack/materials/ligands_dyes.md" %}