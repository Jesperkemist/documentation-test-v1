??? "gas"
    The gas used for the quenching.

    * type: str
    * options: 
        * air
        * dry_air
        * N2
        * Ar
        * He
        * O2
        * H2
        * other

??? "start_time"
    Time of the start of the dispensing in seconds after the start of the spin-coating program.

    * type: float
    * unit: s
    * example: 25

??? "duration"
    The length of the qas quenching.

    * type: float
    * unit: s
    * example: 10

??? "pressure"
    The pressure of the gas.

    * type: float
    * unit: Pa
    * example: 20000

??? "temperature"
    The temperature of the gas.

    * type: float
    * unit: C
    * example: 25

??? "distance_between_nozzle_and_substrate"
    Distance between the nozzle and the substrate

    * type: float
    * unit: mm
    * example: 2.5