from common.AAAAAA import *

def DFLIPFLOP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DFLIPFLOP'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_DFLIPFLOP(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
