???+ tip "Tip"
    Given standard abbreviations, and coefficients, the remaining data can be populated automatically if data for that ion is present in the NOMAD database

??? "abbreviation"
    The abbreviation used for the ion when writing the perovskite composition in the variable long_form. 

    * type: str
    * examples: 
        * Cs
        * MA
        * FA
        * PEA

??? "coefficient"
    The stoichiometric coefficient of the ion. Implemented as a string such as “0.75”, or “1-x”. The rational for representing the coefficients as strings and not as floating-point numbers is to allow for situations where the coefficients are unknown. 

    * type: str
    * examples: 0.75

??? "molecular_formula"
    The molecular formula which indicates the numbers of each type of atom in a molecule, with no information about the structure.

    * type: str
    * examples: 
        * Cs+
        * CH5N2+
        * C8H12N+
        * Pb+2

??? "smiles"
    The canonical SMILES string of the ion. With this data, the organic ions can easily be visualised or used in computational software. 

    * type: str
    * examples: 
        * [Cs+]
        * C(=[NH2+])N
        * C1=CC=C(C=C1)CC[NH3+]
        * [Pb+2]
    

??? "common_name"
    The common or trivial name of the ion. It is common for ions to have more than one common name wherefor the data in this field could vary. Nevertheless, the trade name is worth reporting as this is the way it will be referred to in speech. 

    * type: str
    * examples: 
        * Cesium ion
        * Formamidinium
        * Phenylethylammonium
        * Lead ion

??? "iupac_name"
    The preferred systematic IUPAC name of the ion.

    * type: str
    * examples:
        * Cesium(1+)
        * Formamidinium
        * 2-phenylethylazanium
        * lead(2+) 

??? "cas_number"
    The CAS number for the ion. There are cases where CAS numbers not yet have been defined.

    * type: str
    * examples: 
        * 18459-37-5
        * 17000-00-9

??? "source_compound_smiles"
    The smiles of the neutral parent or source compound. The source compound can vary and is thus not unique, but having data for a neutral source compound solves several problems. It deals with the ambiguity of the charge for diamines, which can be either +1 or +2, CAS numbers are more often defined for source compounds than for their ions, and it provides an entry point to what often is a commercially available starting material in the synthesis. For tertiary amines, there is no unique parent compound, but the I, Br, or Cl salts can often take that role.

    * type: str
    * examples: 
        * [Cs]
        * C(=N)N
        * C1=CC=C(C=C1)CCN

??? "source_compound_molecular_formula"
    The molecular formula for a neutral source compound.

    * type: str
    * examples: C8H11N

??? "source_compound_cas_number"
    The CAS-number for a neutral source compound.

    * type: str
    * examples: 64-04-0

??? "source_compound_iupac_name"
    The systematic IUPAC name for a neutral source compound.

    * type: str
    * examples: 2-phenylethanamine