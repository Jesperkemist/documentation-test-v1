??? "area"
    The area of the layer.  

    ??? "value"
        The area of the layer. Most layers may have the same area as the substrate, but they cna also be smaller than the substrate area

        * type: float
        * unit: cm^2
        * example: 2.5

??? "band_gap"
    The band gap of the layer. 

    ??? "value"
        The band gap of the layer

        * type: float
        * unit: eV
        * example: 1.56

    ??? "graded"
        TRUE if the band gap varies as a function of the vertical position in the layer 

        * type: boolean
        * options: TRUE, FALSE 

    ??? "determined_by"
        The method by which the band gap was estimated.
        The band gap can be estimated from absorption data, 
        EQE-data, UPS-data, or it can be estimated based on literature values 
        for the recipe, or it could be inferred from the composition and what 
        we know of similar but not identical compositions. 

        * type: str
        * options:
            * absorption
            * absorption_tauc-plot
            * composition
            * eqe
            * literature
            * ups
            * xps
            * other


??? "conductivity"
    The conductivity of the layer.  

    ??? "value"
        The conductivity of the layer

        * type: float
        * unit: S/m
        * example: 12.5

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "four_point_probe"


??? "crystallinity"
    The crystallinity of the layer.  

    ??? "value"
        The crystallinity of the layer

        * type: str
        * options:
            * amorphous
            * polycrystalline
            * single_crystal
            * nanoparticles
            * nanorods
            * qunatum_dots
            * other

    ??? "average_grain_size"
        The band gap of the layer

        * type: float
        * unit: nm
        * example: 230

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "sem"


??? "electron_mobility"
    The electron mobility of the layer. 

    ??? "value"
        The electron mobility of the layer.

        * type: float
        * unit: cm**2/(V*s)
        * example: 250

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "hall_measurement"

??? "hole_mobility"
    The hole mobility of the layer. 

    ??? "value"
        The hole mobility of the layer. 

        * type: float
        * unit: cm**2/(V*s)
        * example: 250

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "hall_measurement"


??? "photoluminesence"
    The photoluminesence of the layer. 

    ??? "pl_max"
        The wavelength of the maximum PL intensity'. 

        * type: float
        * unit: nm
        * example: 550

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "spectrometer"



??? "refractive_index"
    The refractive index of the layer.  

    ??? "refractive_index"
        The real part of the refractive index of the layer. 

        * type: float
        * example:1.75

    ??? "extinction_coefficient"
        The imaginary part of the refractive index of the layer. 

        * type: float
        * example:1.75

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "ellipsoetry"

??? "sheet_resistance"
    The sheet resistance of the layer.  

    ??? "value"
        The sheet resistance of the layer

        * type: float
        * unit: ohm
        * example: 25

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "four_point_probe"


??? "surface_roughness"
    The root mean square value of the surface roughness.  

    ??? "value"
        The root mean square value of the surface roughness

        * type: float
        * unit: nm
        * example: 25

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "AFM"


??? "thickness"
    The thickness of the layer.

    ??? "value"
        The thickness of the layer.

        * type: float
        * unit: nm
        * example: 560

    ??? "determined_by"
        The measurement or estimation method used to determine the property.

        * type: str
        * example: "sem"      

