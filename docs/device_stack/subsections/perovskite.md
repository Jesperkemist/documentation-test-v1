### Top level quantities
??? "lead_free"
    True if the perovskite does not contain any lead

    * type: boolean
    * options: TRUE, FALSE 

??? "inorganic"
    True if the perovskite is inorganic

    * type: boolean
    * options: TRUE, FALSE  

??? "double_perovskite"
    True if it is a double perovskite structure. A double perovksite is strictly not a perovskite, but as if in terms of PV development often is treated as a perovskite, it is worth including it but with a flag indicating the structure.

    * type: boolean
    * options: TRUE, FALSE  

??? "has_a_2D_perovskite_capping_layer"
    True if the perovskite has a thin capping layer of a 2D perovskite.

    * type: boolean
    * options: TRUE, FALSE 

### Perovskite composition
??? "composition"
    Section for describing the perovskite composition.
    This section is described in more detail in a separate publication: ...

    ??? "composition_estimation"
        A categorical description of how the composition is estimated.  

        * type: str
        * options: 
            * literature_value
            * estimated_from_XRD_data
            * estimated_from_spectroscopic_data
            * theoretical_simulation
            * other

    ??? "sample_type"
        A categorical description of the type of sample the data describes.         

        * type: str
        * options: 
            * polycrystalline_film
            * single_crystal
            * quantum_dots
            * nano_rods
            * colloidal_solution
            * amorphous
            * other

    ??? "dimensionality"
        A categorical description of the dimensionality of the perovskite. “2D/3D” refers to a situation cases where a 2D phase is intermixed with a 3D phase but where the overall composition is given by the value in long_form.          

        * type: str
        * options: 
            * 0D 
            * 1D
            * 2D
            * 3D
            * 2D/3D

    ??? "band_gap"
        The band gap of the perovskite.           

        * type: float
        * unit: eV
        * example: 1.56

    ### Derived quantities
    The following values for the composition are extracted from data provided about the perovskite ions in the subsections

    ??? "long_form"
        The perovskite composition according to IUPAC recommendations, where standard abbreviations are used for all ions.  A-site ions are listed in alphabetic order, followed by the B-site ions in alphabetic order, followed by the X-site ions in alphabetic order, all with their stoichiometric coefficients. For increased clarity, we recommend enclosing all ions whose abbreviations are 3 letters or longer in parentheses. 

        * type: str
        * examples: 
            * Cs0.05FA0.78MA0.17PbBr0.5I2.5

    ??? "short_form"
        The long_form stripped of the numeric coefficients. This is a useful key for searching and groping perovskite data.  

        * type: str
        * examples: 
            * CsFAMAPbBrI
            * MAPbI

    ### Subsections
    All of the following sections are repeating sections listing all relevant substances of that type 
    ??? "ions_a_site"        
        {% include "device_stack/subsections/perovskite_ion.md" %}

    ??? "ions_b_site"
        {% include "device_stack/subsections/perovskite_ion.md" %}

    ??? "ions_x_site" 
        {% include "device_stack/subsections/perovskite_ion.md" %}

    ??? "additives"
        {% include "device_stack/subsections/additive_impurity.md" %}

    ??? "impurities"
        {% include "device_stack/subsections/additive_impurity.md" %}

