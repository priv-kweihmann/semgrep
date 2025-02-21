from typing import Any, Dict, List, Sequence, Set, Tuple, Optional, Collection

# dump the AST of the targets or pattern using semgrep-core internally
def dump_parsed_ast(
    to_json: bool, language: str, pattern: Optional[str], targets_str: Sequence[str]
) -> None: ...
