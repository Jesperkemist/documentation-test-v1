#### Top level
??? "name"
    The common trade name of the substance.

    * type: str
    * examples: 
        * DMF 
        * DMSO 
        * TiO2-mp 
        * PEDOT:PSS 
        * Spiro-MeOTAD

??? "functionality"
    The role of this specific substance in the solution.

    * type: str
    * options: 
        * solvent 
        * solute 
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

??? "nanostructured"
    TRUE if the compound is nanostructured, e.g. nanoparticles, nanorods etc.

    * type: boolean
    * options: TRUE, FALSE         

#### Subsections
??? "identity"
    {% include "data_schemas/device_stack/materials/compound_identity.md" %}

??? "amount"
    {% include "data_schemas/device_stack/materials/compound_amount.md" %}

??? "supplier"
    {% include "data_schemas/device_stack/materials/compound_supplier.md" %}

??? "nanostructuration"
    {% include "data_schemas/device_stack/materials/compound_nanostructuration.md" %}

??? "synthesis"
    For compounds not sourced from commercial suppliers.
    {% include "data_schemas/device_stack/materials/compound_synthesis.md" %} 
