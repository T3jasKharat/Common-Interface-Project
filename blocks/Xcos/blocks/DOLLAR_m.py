from common.AAAAAA import *

def DOLLAR_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DOLLAR_m'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'dollar4', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_DOLLAR_m(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = 1 if float(parameters[1]) == 0.0 else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
