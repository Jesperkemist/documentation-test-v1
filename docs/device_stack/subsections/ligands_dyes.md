### Top level data
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

### Subsections
??? "identity"
    {% include "device_stack/subsections/compound_identity.md" %}

??? "supplier"
    {% include "device_stack/subsections/compound_supplier.md" %}

??? "synthesis"
    For compounds not sourced from commercial suppliers.
    {% include "device_stack/subsections/compound_synthesis.md" %} 