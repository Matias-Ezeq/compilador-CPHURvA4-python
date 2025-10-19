instructionSet = {
        "LOAD" : {
            "registro" : {
                "R0" : {
                    "R1" : "01",
                    "R2" : "02",
                    "R3" : "03"
                },
                "R1" : {
                    "R0" : "10",
                    "R2" : "12",
                    "R3" : "13"
                },
                "R2" : {
                    "R0" : "20",
                    "R1" : "21",
                    "R3" : "23"
                },
                "R3" : {
                    "R0" : "30",
                    "R1" : "31",
                    "R2" : "32"
                },
            },
            "inmediato" : {
                "R0" : "A0",
                "R1" : "A1",
                "R2" : "A2",
                "R3" : "A3"
            },
            "directo" : {
                "R0" : "B0",
                "R1" : "B1",
                "R2" : "B2",
                "R3" : "B3"
            },
            "indirecto" : {
                "R0" : "R0",
                "R1" : "R1",
                "R2" : "R2",
                "R3" : "R3"
            },
            "SP" : "A4"
        },
        "IN" : {
            "R0" : "BA",
            "R1" : "BB",
            "R2" : "BC",
            "R3" : "BD"
        },

        "STORE" : {
            "directo" : {
                "R0" : "C0",
                "R1" : "C1",
                "R2" : "C2",
                "R3" : "C3"
            },
            "indirecto" : {
                "R0" : "0C",
                "R1" : "1C",
                "R2" : "2C",
                "R3" : "3C"
            }
        },
        "OUT" : {
            "R0" : "CA",
            "R1" : "CB",
            "R2" : "CC",
            "R3" : "CD"
        },
        "ADD" : {
            "R0 R1" : "D1",
            "R0 R2" : "D2",
            "R0 R3" : "D3"
        },
        "ADDC" : {
            "R0 R1" : "1D",
            "R0 R2" : "2D",
            "R0 R3" : "3D"
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
            "R0 R1" : "E4",
            "R0 R2" : "E5",
            "R0 R3" : "E6"
        },

        "OR" : {
            "R0 R1" : "E7",
            "R0 R2" : "E8",
            "R0 R3" : "E9"
        },

        "XNOR" : {
            "R0 R1" : "7E",
            "R0 R2" : "8E",
            "R0 R3" : "9E"
        },

        "SHFTL" : {
            "R0" : "EA",
            "R1" : "EB",
            "R2" : "EC",
            "R3" : "ED"
        },

        "SHFTR" : {
            "R0" : "AE",
            "R1" : "BE",
            "R2" : "CE",
            "R3" : "DE"
        }
    }


codigo = "LOAD R0, 08\nLOAD R1, 08\nADD R0, R1\nSTORE R0, [10]"


def compilar(assembler):
    codigo = assembler.split("\n")
    for i in codigo:
        #remueve la coma y convierte la instrucción en un array iterable
        #donde el primer elemento es la instrucción en sí y el resto sus argumentos
        instruccion = i.replace(",","").split(" ")
        print(compilarInstruccion(instruccion))



def compilarInstruccion(instruccion) :
    try:
        if len(instruccion) == 3 :
            if (instruccion[0] == "LOAD" or instruccion[0] == "STORE") :
                return instructionSet[instruccion[0]][direccionamiento(instruccion[2])][instruccion[1]] + " " + sanitizarArgumento(instruccion[2])
            else :
                return instructionSet[instruccion[0]][instruccion[1] + " " + instruccion[2]]
        else :
            return instructionSet[instruccion[0]] + " " + sanitizarArgumento(instruccion[2])
    except:
        print ("error: instrucción inválida")

def sanitizarArgumento(argumento) :
    replacements = str.maketrans({"[" : "","]" :""})
    return argumento.translate(replacements)


def direccionamiento(argumento) :
    if "[[" in argumento:
        return "indirecto"
    elif "[" in argumento:
        return "directo"
    elif "R" in argumento:
        return "registro"
    else: 
        return "inmediato"