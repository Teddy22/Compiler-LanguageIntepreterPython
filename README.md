# Compiler-LanguageIntepreterPython
A compiler/Interpreter for a defined minimal programmign language implemented using Python 

The minimal fictional programming language is represented by this grammar:

Grammar for the language

Parser

<program> ? main ( ) <EOL> <statement_block>
<statement_block> ? <indent> <statement_list> <dedent>
<statement_list> ? <statement> | <statement> <statement_list>
<statement> ? <if_statement> | <assignment_statement> | <while_statement> | <print_statement>
<if_statement> ? if <boolean_expression> : <EOL> <statement_block> <remaining_if>
<remaining_if> -> <else_clause> | <elif_clause> <remaining_if>
<else_clause> ->  else : <EOL> <statement_block>
<elif_clause> -> elif <boolean_expression> : <EOL> <statement_block>
<while_statement> ? while <boolean_expression> : <EOL> <statement_block>
<assignment_statement> -> id <assignment_operator> <arithmetic_expression> <EOL>
<print_statement> ? print ( arithmetic_expression ) <EOL>
<boolean_expression> ? <relative_op> <arithmetic_expression> <arithmetic_expression>
<relative_op> ? le_operator | lt_operator | ge_operator | gt_operator | eq_operator | ne_operator
<arithmetic_expression> ? <id> | <literal_integer> | <arithmetic_op> <arithmetic_expression> <arithmetic_expression>
<arithmetic_op> ? add_operator | sub_operator | mul_operator | div_operator


Lexical Analyzer
id ? letter
literal_integer ? digit literal_integer | digit
assignment_operator ? =
le_operator ? <=
lt_operator ? <
ge_operator ? >=
gt_operator ? >
eq_operator ? ==
ne_operator ? !=
add_operator ? +
sub_operator ? -
mul_operator ? *
div_operator ? /
