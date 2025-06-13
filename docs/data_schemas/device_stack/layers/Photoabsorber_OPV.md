???+ "m_def"
    Should be: "perovskite_solar_cell_database.schema_packages.tandem.device_stack.Photoabsorber_OPV" <br>
    This is needed to be able to take advantage of normalization functionality in the NOMAD database

<!-- ### Layer -->
{% include "data_schemas/device_stack/layers/layer.md" %}   

??? "blend"
    The name of the OPV blend. Often in the form - "name of acceptor:"name of donor"

    * type: str
    * example: PM6:Y6

??? "cell_type"
    The type of opv cell

    * type: str
    * options: 
        * singel_layer
        * bilayer
        * polymer
        * heterojunction
        * bulk_heterojunction
        * polymer bulk heterojunction
        * homojunction

??? "peak_absorption_wavelength"
    The wavelength at maximum absorption 

    * type: float
    * unit: nm
    * example: 550

??? "molar_extinction_coefficient"
    The molar extinction coefficient

    * type: float
    * unit: L*mol^1*cm^-1
    * example: 10000    

??? "homo_level"
    The energy of the HOMO level

    * type: float
    * unit: eV
    * example: 2.1 

??? "lumo_level"
    The energy of the LUMO level

    * type: float
    * unit: eV
    * example: 2.3

??? "oxidation_potential"
    The oxidation potential vs the normal hydrogen electrode

    * type: float
    * unit: V
    * example: 0.5

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

    * type: int
    * example: 3  