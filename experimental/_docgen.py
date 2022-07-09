# The purpose of this file is to automatically generate API
# documentation *WHILE THE PUBLIC API IS STILL IN FLUX*. It is
# purely a convenience type thing right now, and should be deleted
# as soon as the API is in a stable state.

from __future__ import annotations

from momlib.linalg.matrix import Matrix as matrix_
from momlib.linalg.vector import Vector as vector_
import momlib.linalg.tools as linalg_tools_

from momlib.graph.graph import Graph as graph_
from momlib.graph.digraph import DiGraph as digraph_
import momlib.graph.tools as graph_tools_

from typing import Any, Dict, Literal, List
from types import FunctionType
from inspect import signature, Signature, cleandoc


def get_doc_string(thing: Any) -> str:
    try:
        ds: str | None = thing.__doc__
        if ds is None:
            return ""
        else:
            return cleandoc(ds).strip()
    except:
        return ""


def generate_documentation():

    DOC_ROOT = "C:/Users/baren/source/repos/momlib/docs/api/"
    DOC_LINALG = DOC_ROOT + "linalg/"
    DOC_GRAPH = DOC_ROOT + "graph/"

    def package_as_dict(
        name: str, signature: Signature, docstr: str
    ) -> Dict[Literal["name", "sig", "doc"], str]:
        return {
            "name": name.replace("_", r"\_"),
            "sig": str(signature),
            "doc": cleandoc(docstr).strip(),
        }

    vector_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []
    matrix_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []
    linalg_tools_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []

    graph_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []
    digraph_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []
    graph_tools_doc: List[Dict[Literal["name", "sig", "doc"], str]] = []

    for name, item in matrix_.__dict__.items():
        if isinstance(item, FunctionType):
            if name[0] != "_":
                matrix_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )
    for name, item in vector_.__dict__.items():
        if isinstance(item, FunctionType):
            if name[0] != "_":
                vector_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )
    for name, item in linalg_tools_.__dict__.items():
        if isinstance(item, FunctionType):
            if name in linalg_tools_.__all__:
                linalg_tools_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )

    for name, item in graph_.__dict__.items():
        if isinstance(item, FunctionType):
            if name[0] != "_":
                graph_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )
    for name, item in digraph_.__dict__.items():
        if isinstance(item, FunctionType):
            if name[0] != "_":
                digraph_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )
    for name, item in graph_tools_.__dict__.items():
        if isinstance(item, FunctionType):
            if name in graph_tools_.__all__:
                graph_tools_doc.append(
                    package_as_dict(
                        name,
                        signature(item),
                        item.__doc__,  # type: ignore
                    )
                )

    matrix_doc.sort(key=lambda i: i["name"])
    vector_doc.sort(key=lambda i: i["name"])
    linalg_tools_doc.sort(key=lambda i: i["name"])

    graph_doc.sort(key=lambda i: i["name"])
    digraph_doc.sort(key=lambda i: i["name"])
    graph_tools_doc.sort(key=lambda i: i["name"])

    with open(DOC_LINALG + "matrix.md", "w") as f:
        f.write("# Matrix Object API\n\n")
        f.write(get_doc_string(matrix_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in matrix_doc:
            f.write(f"- [{i['name']}](#matrix{i['name']})\n")
        for i in matrix_doc:
            f.write("\n---\n\n")
            f.write(f"## Matrix.{i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")

    with open(DOC_LINALG + "vector.md", "w") as f:
        f.write("# Vector Object API\n\n")
        f.write(get_doc_string(vector_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in vector_doc:
            f.write(f"- [{i['name']}](#vector{i['name']})\n")
        for i in vector_doc:
            f.write("\n---\n\n")
            f.write(f"## Vector.{i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")

    with open(DOC_LINALG + "tools.md", "w") as f:
        f.write("# Linear Algebra Methods\n\n")
        f.write(get_doc_string(linalg_tools_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in linalg_tools_doc:
            f.write(f"- [{i['name']}](#{i['name']})\n")
        for i in linalg_tools_doc:
            f.write("\n---\n\n")
            f.write(f"## {i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")

    with open(DOC_GRAPH + "graph.md", "w") as f:
        f.write("# Graph Object API\n\n")
        f.write(get_doc_string(graph_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in graph_doc:
            f.write(f"- [{i['name']}](#graph{i['name']})\n")
        for i in graph_doc:
            f.write("\n---\n\n")
            f.write(f"## Graph.{i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")

    with open(DOC_GRAPH + "digraph.md", "w") as f:
        f.write("# Directed Graph Object API\n\n")
        f.write(get_doc_string(digraph_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in digraph_doc:
            f.write(f"- [{i['name']}](#digraph{i['name']})\n")
        for i in digraph_doc:
            f.write("\n---\n\n")
            f.write(f"## DiGraph.{i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")

    with open(DOC_GRAPH + "tools.md", "w") as f:
        f.write("# Graph Theory Methods\n\n")
        f.write(get_doc_string(graph_tools_))
        f.write("\n\n")
        f.write(f"## Contents\n\n")
        for i in graph_tools_doc:
            f.write(f"- [{i['name']}](#{i['name']})\n")
        for i in graph_tools_doc:
            f.write("\n---\n\n")
            f.write(f"## {i['name']}\n")
            f.write(f"```python\n{i['sig']}\n```\n")
            f.write(i["doc"])
            f.write("\n")
        f.write("\n<!--This file has been automatically generated-->\n")


if __name__ == "__main__":
    generate_documentation()
