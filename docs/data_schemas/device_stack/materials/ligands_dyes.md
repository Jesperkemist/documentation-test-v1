## Top level data
??? "name"
    The common trade name of the material.

    * type: str
    * example:Dodecanethiol 

??? "abbreviation"
    Standard arreviation of the compound.

    * type: str
    * example: DDT
       
??? "origin"
    The origin of the compound

    * type: str
    * options:
        * commercial_supplier
        * made_in_house
        * made_by_collaborator
        * collected_in_nature
        * other

## Subsections
??? "identity"
    {% include "data_schemas/device_stack/materials/compound_identity.md" %}

??? "supplier"
    {% include "data_schemas/device_stack/materials/compound_supplier.md" %}

??? "synthesis"
    For compounds not sourced from commercial suppliers.
    {% include "data_schemas/device_stack/materials/compound_synthesis.md" %} 