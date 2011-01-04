"""Utility functions used throughout pymantic."""

__all__ = ['en', 'de', 'one_or_none', 'normalize_iri']

import re

import rdflib

def en(value):
    """Returns an RDF literal from the en language for the given value."""
    return rdflib.Literal(value, lang='en')

def de(value):
    """Returns an RDF literal from the de language for the given value."""
    return rdflib.Literal(value, lang='de')

def one_or_none(values):
    """Fetch the first value from values, or None if values is empty. Raises
    ValueError if values has more than one thing in it."""
    if not values:
        return None
    if len(values) > 1:
        raise ValueError('Got more than one value.')
    return values[0]

percent_encoding_re = re.compile(r'(%[a-fA-F0-9][a-fA-F0-9])+')

def percent_decode(regmatch):
    encoded = ''
    for group in regmatch.groups():
        encoded += chr(int(group, 16))
    uni = encoded.decode('utf-8')
    reserved = ["%", ":", "/", "?", "#", "[", "]", "@", "!", "$", "&", "'", "(",\
                ")", "*", "+", ",", ";", "="]
    for res in reserved:
        uni = uni.replace(res, '%%%02X' % ord(res))
    return uni

def normalize_iri(iri):
    """Normalize an IRI using the Case Normalization (5.3.2.1) and
    Percent-Encoding Normalization (5.3.2.3) from RFC 3987. The IRI should be a
    unicode object."""
    return percent_encoding_re.sub(percent_decode, iri)
