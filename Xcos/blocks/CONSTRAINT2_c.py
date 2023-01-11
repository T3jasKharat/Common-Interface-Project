def CONSTRAINT2_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONSTRAINT2_c'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      blockType='c',
                      simulationFunctionName='constraint_c',
                      simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_CONSTRAINT2_c(cell):
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
