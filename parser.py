class ASTNode:
    pass

class SetNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

class PrintNode(ASTNode):
    def __init__(self, variable):
        self.variable = variable

class AddNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

def parser(tokens):
    ast = []
    i = 0
    
    def parse_additions(start_idx):
        values = [tokens[start_idx][1]]
        j = start_idx + 1
        
        while j < len(tokens) and tokens[j][0] == 'ARTI':
            values.append(tokens[j+1][1])
            j += 2
            
        return values, j
    
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'TANIMLA':
            if i + 3 < len(tokens):
                if tokens[i+1][0] != 'DEGISKEN':
                    raise SyntaxError(f"Expected variable name, got {tokens[i+1][1]}")
                variable = tokens[i+1][1]
                
                if i + 5 < len(tokens) and tokens[i+4][0] == 'ARTI':
                    values, new_i = parse_additions(i+3)
                    
                    temp_var = f"_temp_{i}"
                    ast.append(AddNode(temp_var, (values[0], values[1])))
                    
                    # Diğer toplamalar için
                    for k in range(2, len(values)):
                        new_temp = f"_temp_{i}_{k}"
                        ast.append(AddNode(new_temp, (temp_var, values[k])))
                        temp_var = new_temp
                    
                    # Son sonucu hedef değişkene ata
                    ast.append(SetNode(variable, temp_var))
                    i = new_i
                else:
                    value = tokens[i+3][1]
                    ast.append(SetNode(variable, value))
                    i += 4
            else:
                print("Hata: TANIMLA için yeterli token yok.")
                i += 1
                
        elif token[0] == 'GOSTER':
            if i + 1 < len(tokens):
                if i + 3 < len(tokens) and tokens[i+2][0] == 'ARTI':
                    values, new_i = parse_additions(i+1)
                    
                    temp_var = f"_temp_{i}"
                    ast.append(AddNode(temp_var, (values[0], values[1])))
                    
                    # Diğer toplamalar için
                    for k in range(2, len(values)):
                        new_temp = f"_temp_{i}_{k}"
                        ast.append(AddNode(new_temp, (temp_var, values[k])))
                        temp_var = new_temp
                    
                    ast.append(PrintNode(temp_var))
                    i = new_i
                else:
                    value = tokens[i+1][1]
                    ast.append(PrintNode(value))
                    i += 2
            else:
                print("Hata: GOSTER için yeterli token yok.")
                i += 1
        else:
            i += 1
    return ast
