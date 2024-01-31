from common.AAAAAA import *

def FROM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'FROM'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'from', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_FROM(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
