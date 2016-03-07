###Grammar for the language

##Parser

\<program> ? main ( ) \<EOL> \<statement_block><br/>
\<statement_block> ? \<indent> \<statement_list> \<dedent><br/>
\<statement_list> ? \<statement> | \<statement> \<statement_list><br/>
\<statement> ? \<if_statement> | \<assignment_statement> | \<while_statement> | \<print_statement><br/>
\<if_statement> ? if \<boolean_expression> : \<EOL> \<statement_block> \<remaining_if><br/>
\<remaining_if> -> \<else_clause> | \<elif_clause> \<remaining_if><br/>
\<else_clause> ->  else : \<EOL> \<statement_block><br/>
\<elif_clause> -> elif \<boolean_expression> : \<EOL> \<statement_block><br/>
\<while_statement> ? while \<boolean_expression> : \<EOL> \<statement_block><br/>
\<assignment_statement> -> id \<assignment_operator> \<arithmetic_expression> \<EOL><br/>
\<print_statement> ? print ( arithmetic_expression ) \<EOL><br/>
\<boolean_expression> ? \<relative_op> \<arithmetic_expression> \<arithmetic_expression><br/>
\<relative_op> ? le_operator | lt_operator | ge_operator | gt_operator | eq_operator | ne_operator<br/>
\<arithmetic_expression> ? \<id> | \<literal_integer> | \<arithmetic_op> \<arithmetic_expression> \<arithmetic_expression><br/>
\<arithmetic_op> ? add_operator | sub_operator | mul_operator | div_operator<br/>
<br/>
<br/>
##Lexical Analyzer<br/>
id ? letter<br/>
literal_integer ? digit literal_integer | digit<br/>
assignment_operator ? =<br/>
le_operator ? \<=<br/>
lt_operator ? \<<br/>
ge_operator ? >=<br/>
gt_operator ? ><br/>
eq_operator ? ==<br/>
ne_operator ? !=<br/>
add_operator ? +<br/>
sub_operator ? -<br/>
mul_operator ? *<br/>
div_operator ? /<br/>
