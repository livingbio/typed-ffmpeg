import ast
import re


def remove_typing_from_docstrings(text: str) -> str:
    # 解析 Python 源碼
    module = ast.parse(text)

    # 找到所有的 docstrings
    for node in ast.walk(module):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            docstring = ast.get_docstring(node, clean=False)
            if docstring:
                # 移除括號內的型別註解，並且移除多餘的空格
                docstring = re.sub(r"\s*\([a-zA-Z_, |]*\)\s*:", ":", docstring)
                # 移除方括號內的型別註解
                docstring = re.sub(r"\[[a-zA-Z_, |]*\]", "", docstring)
                # 移除 dict, list, set 型別註解，並且移除多餘的冒號
                docstring = re.sub(r"\b(dict|list|set)\b[a-zA-Z_, |]*\s*:", "", docstring)
                # 替換原始 docstring
                text = text.replace(ast.get_docstring(node, clean=False), docstring)

    return text
