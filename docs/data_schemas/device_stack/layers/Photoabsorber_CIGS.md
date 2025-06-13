???+ "m_def"
    Should be: "perovskite_solar_cell_database.schema_packages.tandem.device_stack.Photoabsorber_CIGS" <br>
    This is needed to be able to take advantage of normalization functionality in the NOMAD database

<!-- ### Layer -->
{% include "data_schemas/device_stack/layers/layer.md" %}   


## Composition
??? "composition"
    The composition of the CIGS

    ## Stoichiometric coefficients
    ??? "Cu"
        The stoichiometric coefficient for Cu

        * type: float
        * example: 1

    ??? "In"
        The stoichiometric coefficient for In

        * type: float
        * example: 1

    ??? "Ga"
        The stoichiometric coefficient for Ga

        * type: float
        * example: 1

    ??? "Se"
        The stoichiometric coefficient for Se

        * type: float
        * example: 2

    ## Derived quantities
    ??? "molecular_formula"
        The molecular formula. Can be derived automatically based on the stoichiometric coefficients


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