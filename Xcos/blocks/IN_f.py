def IN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'IN_f'

    outnode = addNode(outroot, BLOCK_EXPLICIT_IN, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_IN_f(cell):
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
