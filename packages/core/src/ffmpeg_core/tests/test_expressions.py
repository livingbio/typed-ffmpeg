from ..expressions import (
    Expression,
    abs,
    acos,
    asin,
    atan,
    atan2,
    between,
    bitand,
    bitor,
    ceil,
    clip,
    cos,
    cosh,
    eq,
    exp,
    floor,
    gauss,
    gcd,
    gt,
    gte,
    hypot,
    if_,
    ifnot,
    isinf,
    isnan,
    ld,
    lerp,
    log,
    lt,
    lte,
    max,
    min,
    mod,
    not_,
    pow,
    print,
    random,
    randomi,
    root,
    round,
    sgn,
    sin,
    sinh,
    sqrt,
    squish,
    st,
    tan,
    tanh,
    taylor,
    time,
    trunc,
    while_,
)


def test_expression_str() -> None:
    e = Expression("x+1")
    assert str(e) == "x+1"
    assert repr(e) == "Expression(x+1)"


def test_expression_arithmetic() -> None:
    e = Expression("x")
    assert str(e + 1) == "x+1"
    assert str(e - 2) == "x-2"
    assert str(e * 3) == "x*3"
    assert str(e / 4) == "x/4"
    assert str(e % 5) == "x%5"


def test_expression_unary() -> None:
    e = Expression("x")
    assert str(-e) == "-x"
    assert str(+e) == "+x"


def test_expression_pow() -> None:
    e = Expression("x")
    assert str(e**2) == "x^2"


def test_unary_functions() -> None:
    assert str(abs("x")) == "abs(x)"
    assert str(acos("x")) == "acos(x)"
    assert str(asin("x")) == "asin(x)"
    assert str(atan("x")) == "atan(x)"
    assert str(ceil("x")) == "ceil(x)"
    assert str(cos("x")) == "cos(x)"
    assert str(cosh("x")) == "cosh(x)"
    assert str(exp("x")) == "exp(x)"
    assert str(floor("x")) == "floor(x)"
    assert str(gauss("x")) == "gauss(x)"
    assert str(isinf("x")) == "isinf(x)"
    assert str(isnan("x")) == "isnan(x)"
    assert str(log("x")) == "log(x)"
    assert str(not_("x")) == "not(x)"
    assert str(round("x")) == "round(x)"
    assert str(sgn("x")) == "sgn(x)"
    assert str(sin("x")) == "sin(x)"
    assert str(sinh("x")) == "sinh(x)"
    assert str(sqrt("x")) == "sqrt(x)"
    assert str(squish("x")) == "squish(x)"
    assert str(tan("x")) == "tan(x)"
    assert str(tanh("x")) == "tanh(x)"
    assert str(trunc("x")) == "trunc(x)"


def test_single_arg_functions() -> None:
    assert str(atan2("x")) == "atan2(x)"


def test_binary_functions() -> None:
    assert str(bitand("x", "y")) == "bitand(x,y)"
    assert str(bitor("x", "y")) == "bitor(x,y)"
    assert str(eq("x", "y")) == "eq(x,y)"
    assert str(gcd("x", "y")) == "gcd(x,y)"
    assert str(gt("x", "y")) == "gt(x,y)"
    assert str(gte("x", "y")) == "gte(x,y)"
    assert str(hypot("x", "y")) == "hypot(x,y)"
    assert str(lt("x", "y")) == "lt(x,y)"
    assert str(lte("x", "y")) == "lte(x,y)"
    assert str(max("x", "y")) == "max(x,y)"
    assert str(min("x", "y")) == "min(x,y)"
    assert str(mod("x", "y")) == "mod(x,y)"
    assert str(pow("x", "y")) == "pow(x,y)"
    assert str(st("idx", "x")) == "st(idx,x)"


def test_ternary_functions() -> None:
    assert str(between("x", 0, 10)) == "between(x,0,10)"
    assert str(clip("x", 0, 10)) == "clip(x,0,10)"
    assert str(lerp("x", "y", "z")) == "lerp(x,y,z)"
    assert str(randomi("idx", 0, 10)) == "randomi(idx,0,10)"


def test_if_functions() -> None:
    assert str(if_("x", "y")) == "if(x,y)"
    assert str(if_("x", "y", "z")) == "if(x,y,z)"
    assert str(ifnot("x", "y")) == "ifnot(x,y)"
    assert str(ifnot("x", "y", "z")) == "ifnot(x,y,z)"


def test_other_functions() -> None:
    assert str(ld("idx")) == "ld(idx)"
    assert str(random("idx")) == "random(idx)"
    assert str(root("x", 10)) == "root(x,10)"
    assert str(print("t")) == "print(t)"
    assert str(print("t", 1)) == "print(t,1)"
    assert str(taylor("x", "y")) == "taylor(x,y)"
    assert str(taylor("x", "y", "idx")) == "taylor(x,y,idx)"
    assert str(time("x")) == "time(x)"
    assert str(while_("cond", "expr")) == "while(cond,expr)"


def test_expression_returns_expression() -> None:
    result = abs("x")
    assert isinstance(result, Expression)
