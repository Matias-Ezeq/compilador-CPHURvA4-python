def compilar(assembler):

    instructionSet = {
        "LOAD" : {
            "R0" : "A0",
            "R1" : "A1",
            "R2" : "A2",
            "R3" : "A3",
            "SP" : "A4"
        },
        "IN" : {
            "R0" : "BA",
            "R1" : "BB",
            "R2" : "BC",
            "R3" : "BD"
        },
        "STORE" : {
            "R0" : "C0",
            "R1" : "C1",
            "R2" : "C2",
            "R3" : "C3"
        },
        "OUT" : {
            "R0" : "CA",
            "R1" : "CB",
            "R2" : "CC",
            "R3" : "CD"
        },
        "ADD" : {
            "R0, R1" : "D1",
            "R0, R2" : "D2",
            "R0, R3" : "D3"
        },
        "ADDC" : {
            "R0, R1" : "1D",
            "R0, R2" : "2D",
            "R0, R3" : "3D"
        },
        "NOT" : {
            "R0" : "E0",
            "R1" : "E1",
            "R2" : "E2",
            "R3" : "E3"
        },
        "INC" : {
            "R0" : "F0",
            "R1" : "F1",
            "R2" : "F2",
            "R3" : "F3"
        },
        "DEC" : {
            "R0" : "F4",
            "R1" : "F5",
            "R2" : "F6",
            "R3" : "F7"
        },
        "PUSH" : {
            "R0" : "A5",
            "R1" : "A6",
            "R2" : "A7",
            "R3" : "A8"
        },
        "POP" : {
            "R0" : "5A",
            "R1" : "6A",
            "R2" : "7A",
            "R3" : "8A"
        },
        "JMP" : "50",
        "JZ" : "60",
        "JNZ" : "70",
        "JN" : "80",
        "JNN" : "90",

        "JO" : "40",
        "JNO" : "04",
        "JC" : "41",
        "JNC" : "14",

        "JSR" : "05",
        "RET" : "55",

        "RETI" : "65",
        
        "AND" : {
            "R0, R1" : "E4",
            "R0, R2" : "E5",
            "R0, R3" : "E6"
        },

        "OR" : {
            "R0, R1" : "E7",
            "R0, R2" : "E8",
            "R0, R3" : "E9"
        },

        "XNOR" : {
            "R0, R1" : "7E",
            "R0, R2" : "8E",
            "R0, R3" : "9E"
        },

        "SHFTL" : {
            "R0" : "EA",
            "R1" : "EB",
            "R2" : "EC",
            "R3" : "ED"
        },

        "SHFTL" : {
            "R0" : "AE",
            "R1" : "BE",
            "R2" : "CE",
            "R3" : "DE"
        }
    }

    codigo = assembler.split("\n")
    print(codigo)