from utils import get_function
from utils import get_references
from utils import is_numeric
from utils import CycleDetected


EVALUATING = 'EVALUATING'


def evaluate(sheet):
    evaluated = {}
    sheet = sheet.copy()
    for key in sheet:
        _evaluate_rooted_tree(key, sheet)
    return sheet


def _evaluate_rooted_tree(root, sheet):
    contents = sheet[root]

    if contents == EVALUATING:
        raise CycleDetected

    if is_numeric(contents):
        return contents
    else:
        fn, child_nodes = get_function(contents), get_references(contents)
        sheet[root] = EVALUATING
        values = [_evaluate_rooted_tree(child_node, sheet)
                  for child_node in child_nodes]
        sheet[root] = fn(values)
        return sheet[root]


if __name__ =='__main__':
    from testers import run_evaluation_tests
    run_evaluation_tests(evaluate)
