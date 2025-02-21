from typing import Any, Dict, List, Sequence, Set, Tuple, Optional, Collection
from pathlib import Path
import semgrep.error as error
from semgrep.rule_match import RuleMatch

def run_join_rule(
    join_rule: Dict[str, Any],
    targets: List[Path],
) -> Tuple[List[RuleMatch], List[error.SemgrepError]]:
    """
    Run a 'join' mode rule.

    Join rules are comprised of multiple Semgrep rules and a set
    of conditions which must be satisfied in order to return a result.
    These conditions are typically some comparison of metavariable contents
    from different rules.

    'join_rule' is a join rule definition in dictionary form. The required keys are
    {'id', 'mode', 'severity', 'message', 'join'}.

    'join' is dictionary with the required keys {'refs', 'on'}.

    'refs' is dictionary with the required key {'rule'}. 'rule' is identical to
    a Semgrep config string -- the same thing used on the command line. e.g.,
    `semgrep -f p/javascript.lang.security.rule` or `semgrep -f path/to/rule.yaml`.

    'refs' has optional keys {'renames', 'as'}. 'renames' is a list of objects
    with properties {'from', 'to'}. 'renames' are used to rename metavariables
    of the associated 'rule'. 'as' lets you alias the collection of rule results
    for use in the conditions, similar to a SQL alias. By default, collection names
    will be the rule ID.

    'on' is a list of strings of the form <collection>.<property> <operator> <collection>.<property>.
    These are the conditions which must be satisifed for this rule to report results.
    All conditions must be satisfied.

    See semgrep/tests/e2e/rules/join_rules/user-input-with-unescaped-extension.yaml
    for an example.
    """
