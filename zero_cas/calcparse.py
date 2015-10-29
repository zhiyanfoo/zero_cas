import ply.yacc as yacc
from calclex import tokens

identifiers = dict()

def p_assign_expression(p):
    'statement : IDENTIFIER ASSIGN expression'
    identifiers[p[1]] = p[3]

def p_statement(p):
    'statement : expression'
    p[0] = p[1]


def p_expression_plus(p):
    'expression : expression PLUS factor'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS factor'
    p[0] = p[1] - p[3]

def p_expression_factor(p):
    'expression : factor'
    p[0] = p[1]

def p_factor_parenthesis(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_multiplication(p):
    'factor : factor TIMES term'
    p[0] = p[1] * p[3]
    

def p_factor_divide(p):
    'factor : factor DIVIDE term'
    p[0] = p[1] / p[3]

def p_factor_term(p):
    'factor : term'
    p[0] = p[1]

def p_term_parenthesis(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]

def p_term_negative_unary(p):
    'term : MINUS unary'
    p[0] = -p[2]

def p_term_unary(p):
    'term : unary'
    p[0] = p[1]

def p_unary_parenthesis(p):
    'unary : LPAREN expression RPAREN'
    p[0] = p[2]

def p_unary_exponential(p):
    'unary : exponential'
    p[0] = p[1]

def p_exponential_parenthesis(p):
    'exponential : LPAREN expression RPAREN'
    p[0] = p[2]

def p_exponential_exponential(p):
    'exponential : NUMBER EXPONENT term'
    p[0] = p[1] ** p[3]

def p_to_number(p):
    'exponential : NUMBER'
    p[0] = p[1]

calcparser = yacc.yacc()



