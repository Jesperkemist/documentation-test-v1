#### Top level
??? "name"
    The common trade name of the substance.

    * type: str
    * examples: 
        * methylamine 
        * I2 
        * H2O 

??? "functionality"
    The role of this specific substance in the gas mixture-

    * type: str
    * options: 
        * reactant 
        * product 
        * carrier_gas
        * none
        * other 

??? "origin"
    The origin of the substance

    * type: str
    * options: 
        * commercial_supplier 
        * made_in_house 
        * made_by_collaborator
        * collected_in_nature
        * other        

??? "partial_pressure"
    The partial pressure of the gas.

    * type: float
    * unit: Pa
    * example: 2000         

#### Subsections
??? "identity"
    {% include "data_schemas/device_stack/materials/compound_identity.md" %}

??? "supplier"
    {% include "data_schemas/device_stack/materials/compound_supplier.md" %}

??? "synthesis"
    For compounds not sourced from commercial suppliers.
    {% include "data_schemas/device_stack/materials/compound_synthesis.md" %} 
