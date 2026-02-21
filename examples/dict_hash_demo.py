"""Demonstration of how Python dict handles keys with duplicate hash values.

Run: python3 examples/dict_hash_demo.py

This file contains three short cases demonstrating the two-step lookup
process used by Python dictionaries:

  1) compute hash(key)  -> find candidate slot
  2) check equality     -> confirm key identity

When two keys produce the same hash value, Python probes (searches) for
an available slot and uses equality (==) to decide whether the stored key
is the same key (overwrite) or a different key (store both under collision).

The examples below intentionally craft keys with identical hashes to make
the behavior obvious.  Keep this file as a reference for how dicts resolve
hash collisions and equality checks.
"""


class A:
    """Small helper class where we can control __hash__ and __eq__.

    - __hash__ returns a constant so many objects collide.
    - __eq__ compares the internal value so we can demonstrate both
      collision-without-equality and collision-with-equality.
    """

    def __init__(self, v):
        self.v = v

    def __hash__(self):
        # Deliberately poor hash: every A instance has the same integer hash.
        # This forces hash collisions so the dict's probing and equality
        # comparison logic become visible.
        return 42

    def __eq__(self, other):
        # Equality is based on the payload 'v'. If two objects have the
        # same 'v' they are considered equal, otherwise not.
        return isinstance(other, A) and self.v == other.v

    def __repr__(self):
        return f"A({self.v})"


def case1():
    """Case 1: same hash value, but objects are NOT equal.

    Expectation: dict stores both keys separately. Lookup by either key
    returns the correct, distinct value.
    """

    print("Case 1: same hash, not equal")
    a1 = A(1)
    a2 = A(2)

    # Both A(1) and A(2) return the same hash(), but they are not equal.
    d = {}
    d[a1] = "one"
    d[a2] = "two"

    print("hash(a1)=", hash(a1), "hash(a2)=", hash(a2))
    print("a1 == a2?", a1 == a2)
    print("dict keys:", list(d.keys()))
    print("lookup a1:", d[a1])
    print("lookup a2:", d[a2])
    print()


def case2():
    """Case 2: same hash value, and objects compare equal.

    Expectation: dict treats the two keys as the same key; the second
    insertion overwrites the first's value.
    """

    print("Case 2: same hash, equal")
    b1 = A(3)
    b2 = A(3)  # different object but same payload -> b1 == b2 is True

    d2 = {}
    d2[b1] = "first"
    d2[b2] = "second"  # overwrites because equality is True

    print("hash(b1)=", hash(b1), "hash(b2)=", hash(b2))
    print("b1 == b2?", b1 == b2)
    print("dict items:", list(d2.items()))
    print()


def case3():
    """Case 3: built-in immutable keys (strings).

    Shows that two distinct string objects with the same contents are equal
    and therefore considered the same dict key (second assignment wins).
    """

    print("Case 3: strings equal but different ids")
    s1 = "The Python Coding Stack"
    # build a new string object with identical contents
    s2 = " ".join(["The", "Python", "Coding", "Stack"])  # new str object

    print("s1==s2?", s1 == s2)
    print("id(s1)=", id(s1), "id(s2)=", id(s2))
    print("hashes:", hash(s1), hash(s2))

    d3 = {}
    d3[s1] = "pub1"
    # This overwrites the entry because s1 == s2 evaluates to True
    d3[s2] = "pub2"

    print("d3 items:", list(d3.items()))
    print()


if __name__ == "__main__":
    # Run each case in order; the printed output and inline comments
    # are safe to read and keep as a small reference for dict behavior.
    case1()
    case2()
    case3()
