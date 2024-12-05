from parser import SetNode, PrintNode, AddNode

def interpreter(ast):
    variables = {}
    for node in ast:
        if isinstance(node, SetNode):
            if isinstance(node.value, str):
                if node.value.startswith('_temp_'):
                    if node.value not in variables:
                        raise NameError(f"Temporary variable {node.value} not found")
                    variables[node.variable] = variables[node.value]
                elif node.value in variables:
                    variables[node.variable] = variables[node.value]
                else:
                    try:
                        variables[node.variable] = int(node.value)
                    except ValueError:
                        raise ValueError(f"Cannot convert {node.value} to integer")
        elif isinstance(node, PrintNode):
            if node.variable in variables:
                print(variables[node.variable])
            else:
                try:
                    print(int(node.variable))
                except ValueError:
                    print(node.variable)
        elif isinstance(node, AddNode):
            if node.variable not in variables:
                variables[node.variable] = 0
            
            value1, value2 = node.value
            try:
                num1 = variables[value1] if value1 in variables else int(value1)
                num2 = variables[value2] if value2 in variables else int(value2)
                variables[node.variable] = num1 + num2
            except ValueError:
                raise ValueError(f"Cannot add non-numeric values: {value1}, {value2}")

