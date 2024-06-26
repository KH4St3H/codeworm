grammar nsc;

// Lexer rules
ID : [a-zA-Z] [a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;
STRING : '"' .*? '"' ;
WS : [ \t\n\r]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
function_arg: ID;

// Parser rules
program : statements ;
statements : statement* ;
statement
    : assign_statement
    | begin_end_statement
    | if_else_statement
    | while_statement
    | for_statement
    | loop_statement
    | print_simple
    | print_literal
    | function_declration_statement
    | function_call_statement
    | return_statement
    ;


// Expression with separated operators
expr: cumTerm (cumopr cumTerm)*; 
cumTerm: term (additive term)*;
term: factor (multiplicative factor)*;
factor: exponent ('^' exponent)*;
exponent: '(' expr ')' # ParenthesizedExpression
    | ID # Identifier
    | NUMBER # Number
    | function_call # FunctionCall
    | '-'  expr # UnaryMinus
    ;

function_call: ID '(' ((expr ',')* expr)? ')';

assign_statement: ID '=' expr ';';
begin_end_statement: 'begin' statements 'end';
print_simple: 'print' ID ';';
print_literal: 'print' STRING ',' ID ';';
if_else_statement: 'if' expr 'then' statement ('else' statement)?;
while_statement: 'while' expr 'do' statement;
for_statement: 'for' ID 'of' NUMBER 'to' NUMBER 'do' statement;
loop_statement: 'loop' ID ':' NUMBER 'do' statement;
function_declration_statement: 'fn' ID '(' ((function_arg ',')* function_arg)? ')' begin_end_statement;
function_call_statement: function_call ';';
return_statement: 'return' expr ';';

// Operator rules
cumopr : '>' | '<=' | '>=' | '==' | '!=' | '<' ;
multiplicative : '*' | '/' | '%';
additive : '+' | '-' ;
