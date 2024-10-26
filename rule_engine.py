## his module contains the ASTNode class along with the create_rule and evaluate_rule functions. It’s the core logic for rule creation and evaluation.

import ast
import operator as op

# ASTNode class for representing rule nodes
class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"{self.node_type}: {self.value}"

# Function to create the AST (rule creation)
def create_rule(rule_string):
    # Supported operators for evaluation
    operators = {
        ast.And: lambda x, y: x and y,
        ast.Or: lambda x, y: x or y,
        ast.Eq: op.eq,
        ast.NotEq: op.ne,
        ast.Gt: op.gt,
        ast.Lt: op.lt,
        ast.GtE: op.ge,
        ast.LtE: op.le,
    }

    class RuleTransformer(ast.NodeTransformer):
        def visit_Compare(self, node):
            left = self.visit(node.left)
            right = self.visit(node.comparators[0])
            op_type = type(node.ops[0])
            return ASTNode("operand", value=(left.id, operators[op_type], right.n))

        def visit_BoolOp(self, node):
            op_type = type(node.op)
            operator = "AND" if op_type is ast.And else "OR"
            left = self.visit(node.values[0])
            right = self.visit(node.values[1])
            return ASTNode("operator", left=left, right=right, value=operator)

    # Parse the rule into an AST
    tree = ast.parse(rule_string, mode='eval')
    return RuleTransformer().visit(tree.body)

# Function to evaluate the rule against provided data
def evaluate_rule(ast_tree, data):
    if ast_tree.node_type == "operator":
        left_result = evaluate_rule(ast_tree.left, data)
        right_result = evaluate_rule(ast_tree.right, data)
        if ast_tree.value == "AND":
            return left_result and right_result
        elif ast_tree.value == "OR":
            return left_result or right_result
    elif ast_tree.node_type == "operand":
        left, operator_func, right = ast_tree.value
        return operator_func(data[left], right)
