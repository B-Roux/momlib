from typing import Literal
import momlib
from types import FunctionType, ModuleType
from inspect import signature, cleandoc


def gen_doc(input: ModuleType | object):
    contents: list[dict[Literal["name", "sig", "doc"], str]] = []
    for name, item in input.__dict__.items():
        if (
            isinstance(item, FunctionType)
            and (name[0] != "_" or name[1] == "_")
            and (not isinstance(input, ModuleType) or name in input.__all__)
        ):
            contents.append(
                {
                    "name": name,
                    "sig": str(signature(item)),
                    "doc": cleandoc(
                        item.__doc__ if item.__doc__ is not None else ""
                    ).replace("_", "\\_"),
                }
            )
    return (
        # not the best practice for efficiency, but this script does not
        # need to be efficient as it will be run very rarely.
        "\n"
        + cleandoc(input.__doc__ if input.__doc__ is not None else "").replace(
            "_", "\\_"
        )
        + "\n\n## Contents\n\n"
        + "\n".join(
            "- [" + i["name"].replace("_", "\\_") + f"](#{i['name']})"
            for i in contents
        )
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(
            (
                "# "
                + i["name"].replace("_", "\\_")
                + "\n\n"
                + f"```python\n{i['sig']}\n```\n\n{i['doc']}"
            )
            for i in contents
        )
        + "\n\n<!--this file has been automatically generated-->"
    )


def main():
    PATH = "./docs/"
    LINALG_PATH = PATH + "linalg/"
    GRAPH_PATH = PATH + "graph/"

    # Linear Algebra
    with open(LINALG_PATH + "matrix.md", "w") as f:
        print("# Matrix Object Instance Methods", file=f)
        print(gen_doc(momlib.linalg.Matrix), file=f)
    with open(LINALG_PATH + "vector.md", "w") as f:
        print("# Vector Object Instance Methods", file=f)
        print(gen_doc(momlib.linalg.Vector), file=f)
    with open(LINALG_PATH + "tools.md", "w") as f:
        print("# Linear Algebra Tools", file=f)
        print(gen_doc(momlib.linalg.tools), file=f)

    # Graph Theory
    with open(GRAPH_PATH + "graph.md", "w") as f:
        print("# Graph Object Instance Methods", file=f)
        print(gen_doc(momlib.graph.Graph), file=f)
    with open(GRAPH_PATH + "digraph.md", "w") as f:
        print("# DiGraph Object Instance Methods", file=f)
        print(gen_doc(momlib.graph.DiGraph), file=f)
    with open(GRAPH_PATH + "tools.md", "w") as f:
        print("# Graph Theory Tools", file=f)
        print(gen_doc(momlib.graph.tools), file=f)


if __name__ == "__main__":
    main()
