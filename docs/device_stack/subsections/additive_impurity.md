???+ tip "Tip"
    Most of the data identifying the substance can be populated automatically if the substance is present within hte PubChem database 

??? "abbreviation"
    Standard abbreviation

    * type: str
    * example: RbI 

??? "concentration"
    Concentration. 

    * type: float
    * unit: cm^-3 
    * examples: 1e16

??? "mass_fraction"
    Mass fraction of the substance in the layer. 

    * type: float
    * examples: 0.001

??? "common_name"
    The common or trivial name of the substance. It is common for substances to have more than one common name wherefor the data in this field could vary. Nevertheless, the trade name is worth reporting as this is the way it will be referred to in speech. 

    * type: str
    * example: Rubidium iodide 

??? "molecular_formula"
    The molecular formula which indicates the numbers of each type of atom in a molecule, with no information about the structure.

    * type: str
    * examples: Fe+2

??? "smiles"
    The canonical SMILES string of the substance. 

    * type: str
    * examples: [Fe+2]

??? "iupac_name"
    The preferred systematic IUPAC name of the substance.

    * type: str
    * example: iron(2+)"

??? "cas_number"
    The CAS number for the substance. 

    * type: str
    * example: 1317-63-1
