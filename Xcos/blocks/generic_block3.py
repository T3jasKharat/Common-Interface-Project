def generic_block3(outroot, attribid, ordering, geometry, parameters):
    func_name = 'generic_block3'

    if parameters[17] == 'y':
        depends_u = '1'
    else:
        depends_u = '0'

    if parameters[18] == 'y':
        depends_t = '1'
    else:
        depends_t = '0'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[0], 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU=depends_u,
                         dependsOnT=depends_t)

    addExprsNode(outnode, TYPE_STRING, 19, parameters)

    return outnode


def get_from_generic_block3(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
