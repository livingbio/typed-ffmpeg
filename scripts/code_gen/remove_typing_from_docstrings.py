import re


def remove_typing_from_docstrings(text: str) -> str:
    # 移除括號內的型別註解，並且移除多餘的空格
    text = re.sub(r"\s*\([a-zA-Z_, |]*\)\s*:", ":", text)
    # 移除方括號內的型別註解
    text = re.sub(r"\[[a-zA-Z_, |]*\]", "", text)
    # 移除 dict, list, set 型別註解，並且移除多餘的冒號
    text = re.sub(r"\b(dict|list|set)\b[a-zA-Z_, |]*\s*:", "", text)
    return text
