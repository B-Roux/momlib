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
                    ),
                }
            )
    return (
        # not the best practice for efficiency, but this script does not
        # need to be efficient as it will be run very rarely.
        "\n"
        + cleandoc(input.__doc__ if input.__doc__ is not None else "")
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
    PATH = "./docs/reference/"

    # Linear Algebra
    with open(PATH + "matrix.md", "w") as f:
        print("# Matrix Object Instance Methods", file=f)
        print(gen_doc(momlib.Matrix), file=f)
    with open(PATH + "vector.md", "w") as f:
        print("# Vector Object Instance Methods", file=f)
        print(gen_doc(momlib.Vector), file=f)
    with open(PATH + "linalg.md", "w") as f:
        print("# Linear Algebra Tools", file=f)
        print(gen_doc(momlib._linalg), file=f)  # type: ignore


if __name__ == "__main__":
    main()
