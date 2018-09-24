# Monads

## Category Theory
* "Natural extension of our notion of sets and functions"
    - generalization of a set in a category is an object
    - generalization of a function is a morphism
        - a morphism (i.e. function) goes from one object (set) to another and it can be composed
            - i.e. `A->B` and `B->C` can be composed into morphism `A->C`
    - function composition: eg. `(g f)(x) = g(f(x))`

## Monads
* Design pattern
* Allow function composition for incompatible types


## Important Monadic Functions
* bind() - a way to coerce functions into a desired format
    - `bind :: Number -> (Number, String) function -> (Number, String)`
* unit() - takes a value and wraps it in a basic container so the functions we are working on can consume it
    - `unit :: Number -> (Number, String)` (function is taking in a number and returning (number, string) so we need to use 'unit')

* bind and unit work together to wrap and unwrap values
    - *NOTE:* python objects are nullable, so does not not need 'unit' for wrapping (i.e. `return None = return`)


## Identity Monad
*pythonic syntax, but not necessary in python*
```
def unit(x):
    return x
```

## Abstracting with 'Bind'
Unwieldly as cases expand:
```
def risk_analysis(company):
    if not company: return
    credit = get_credit_score(company)

    if not credit: return
    net_worth = get_net_worth(credit)

    risk_level = get_risk_level(net_worth)
    return risk_level

```
With bind:
```
def bind(val, fxn):
    return fxn(val) if val else None

def risk_analysis(company):
    credit = bind(company, get_credit_score)
    net_worth = bind(credit, get_net_worth)
    risk_level = bind(net__worth, get_risk_level)
    return risk_level

>> risk_analysis(Company(34343, "Enigma"))
low
```
A better bind:
```
def bind(val, fxn):
    return fxn(val) if val else None

def pipe(val, *fxns):
    _val = val
    for fn in fxns:
        _val = bind(_val, fn)
    return _val


>> pipe(Comapny(34343, "Enigma"), get_credit_score, get_net_worth, get_risk_level)
low
```
What about handling errors?
* Return a tuple of info: (risk/score, message). Example:
```
def get_risk_level(net_worth):
    if net_worth > 1000 and net_worth < 2000:
        return ('high', None)
    elif net_worth >= 2000:
        return ('low', None)
    else:
        return (None, 'Company is off the charts')
```
Bind cannot handle tuples, so cannot compose anymore, so we change to:
```
def unit(val):
    return (val, None)

def bind(val, fn):
    return fn(val[0]) if val[0] else val

def pipe(val, *fns):
    _val = unit(val)
    for fn in fns:
        _val = bind(_val, fn)
    return _val
```

## Hipster Monads
* With monads, you can easily add more business logic without having to add extra plumbing
* Why are they not mainstream if they are so powerful?
    * They can blow up the stack since they are macros on top of deeply nested closures
    * Most popular languages aren't tail recursive and tail-call stack elimination is essentially required... rewinding the stack in a language like Python is slow
* Most theoretical math concepts never really caught on in a software as well as a mainstream language capable of expressing them
    * Common Lisp could express this

## Sources to Look into
1. http://www.leonardoborges.com/writings/2012/11/30/monads-in-small-bites-part-i-functors/
2. http://adambard.com/blog/acceptable-error-handling-in-clojure/
3. http://senko.net/maybe-monad-in-python
4. http://bodil.org/hipster/
