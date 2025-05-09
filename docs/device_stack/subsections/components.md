??? "components"
    Repeating section. List all substances in the layer

    ### Top level data
    ??? "name"
        The common trade name of the material.

        * type: str
        * example:
            * TiO2
            * PEDOT:PSS

    ??? "abbreviation"
        Standard arreviation of the compound.

        * type: str
        * example:
            * MA
            * PEA        

    ??? "functionality"
        The primary functionality of the compound

        * type: str
        * options:
            * majority_phase
            * secondary_phase
            * additive
            * dopant
            * impurity
            * solvent
            * other

    ??? "aggregation_state"
        The aggregation state of the compound

        * type: str
        * options:
            * solid
            * liquid
            * gas
            * solution
            * suspension
            * other

    ??? "origin"
        The origin of the compound

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

    ### Subsections
    ??? "identity"
        {% include "device_stack/subsections/compound_identity.md" %}

    ??? "amount"
        {% include "device_stack/subsections/compound_amount.md" %}

    ??? "supplier"
        {% include "device_stack/subsections/compound_supplier.md" %}

    ??? "nanostructuration"
        {% include "device_stack/subsections/compound_nanostructuration.md" %}

    ??? "synthesis"
        For compounds not sourced from commercial suppliers.
        {% include "device_stack/subsections/compound_synthesis.md" %} 