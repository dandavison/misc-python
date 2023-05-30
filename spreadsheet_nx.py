from itertools import chain

import networkx as nx

from solution import _evaluate_rooted_tree

from utils import CycleDetected
from utils import get_function
from utils import get_references
from utils import is_numeric


def evaluate(sheet):
    sheet = sheet.copy()

    sorted_keys = _postorder_nodes(_make_dag(sheet))
    for key in sorted_keys:
        sheet[key] = _evaluate_contents(sheet[key], sheet)

    return sheet


def recalc(unevaluated_sheet, evaluated_sheet, changes):
    """
    Evaluate `unevaluated_sheet` after applying `changes`.

    1. The set of affected nodes is the set of changed nodes plus all their
       predecessors.

    2. We form our working sheet by:
       1. Start with the previous evaluated sheet
       2. Apply the changes to changed cells
       3. Reset affected-but-not-directly changed cells to their unevaluated
          contents.

    3. At every affected node, evaluate the DAG rooted at that node taking
    contents from our working sheet.

    The number of formula evaluations is the minimum possible.

    If the successors of node v contain no affected nodes, and v is not the
    immediate child of an affected node, then v will not be visited. In other
    words, the algorithm does not waste time in "subtrees" which are unaffected
    by the changes.
    """
    sheet_for_dag_construction = unevaluated_sheet.copy()
    sheet_for_dag_construction.update(changes)
    reversed_dag = _make_dag(sheet_for_dag_construction).reverse()
    affected_nodes = set(chain.from_iterable(
        nx.dfs_postorder_nodes(reversed_dag, key)
        for key in changes))

    sheet_for_evaluation = evaluated_sheet.copy()
    for key in affected_nodes:
        if key in changes:
            sheet_for_evaluation[key] = changes[key]
        else:
            sheet_for_evaluation[key] = unevaluated_sheet[key]

    for key in affected_nodes:
        _evaluate_rooted_tree(key, sheet_for_evaluation)

    return sheet_for_evaluation


def _postorder_nodes(dag):
    return _topological_sort(dag, reverse=True)


def _topological_sort(dag, reverse):
    try:
        return nx.topological_sort(dag, reverse=reverse)
    except nx.NetworkXUnfeasible:
        raise CycleDetected


def _evaluate_contents(contents, evaluated_sheet):
    if is_numeric(contents):
        return contents
    else:
        fn, child_keys = get_function(contents), get_references(contents)
        return fn([evaluated_sheet[_key] for _key in child_keys])


def _make_dag(sheet):
    dag = nx.DiGraph()
    for key, contents in sheet.iteritems():
        if is_numeric(contents):
            dag.add_node(key)
        else:
            for child_key in get_references(contents):
                dag.add_edge(key, child_key)
    return dag


if __name__ =='__main__':
    from testers import run_evaluation_tests
    from testers import run_recalc_tests
    run_evaluation_tests(evaluate)
    run_recalc_tests(recalc)
