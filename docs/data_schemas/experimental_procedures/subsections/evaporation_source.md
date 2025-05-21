### Top level data
??? "amount"
    The amount of the compound in the evaporation source.

    * type: float
    * unit: g
    * example: 2.3

??? "substrate_distance"
    The distance between the substrate and the evaporation source.

    * type: float
    * unit: cm
    * example: 12.5

??? "name"
    The common trade name of the material.

    * type: str
    * example:
        * Au
        * Ag
        * C60 
        * PCBM60
        * LiF
        * MoO3

??? "aggregation_state"
    The aggregation state of the compound

    * type: str
    * options:
        * solid
        * liquid
        * other

??? "crucible_material"
    The aggregation state of the compound

    * type: str
    * examples:
        * Mo
        * W
        * Glass

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
    {% include "data_schemas/device_stack/materials/compound_identity.md" %}

??? "supplier"
    {% include "data_schemas/device_stack/materials/compound_supplier.md" %}

??? "synthesis"
    For compounds not sourced from commercial suppliers.
    {% include "data_schemas/device_stack/materials/compound_synthesis.md" %} 