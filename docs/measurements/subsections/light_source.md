??? "spectrum"
    Spectrum of the illumination 
   
    * type: str
    * options: 
        * Dark 
        * AM1.5 
        * AM1.5G 
        * AM0 
        * AM1.0 
        * UVA 
        * UVB 
        * Monochromatic 
        * Ambient_indoor 
        * Ambient_outdoor 
        * Other


??? "light_source"
    Type of illumination.
   
    * type: str
    * options: 
        * Dark_conditions
        * Solar_simulator_unspecified 
        * Metal_halide
        * Sulfur_plasma 
        * LED
        * Withe_led 
        * Xenon 
        * Halogen 
        * Laser 
        * Incandescent 
        * Fluorescent
        * Ambient_indoor 
        * Ambient_outdoor 
        * UV
        * Other


??? "solar_simulator_class"
    Type of illumination.
   
    * type: str
    * options
        * AAA
        * AAB
        * AAC
        * ABA
        * ABB
        * ABC
        * ACA
        * ACB
        * ACC
        * BAA
        * BAB
        * BAC
        * BBA
        * BBB
        * BBC
        * BCA
        * BCB
        * BCC
        * CAA
        * CAB
        * CAC
        * CBA
        * CBB
        * CBC
        * CCA
        * CCB
        * CCC
        * Unknown
        * Other

??? "light_source_model"
    The brand name and model of the light source/solar simulator used

    * type: str
    * example: "Newport 94023A"

??? "peak_wavelength"
    Peak wavelength of the light. Mostly relevant when monochromatic light is used

    * type: float
    * unit: nm
    * example: 560
