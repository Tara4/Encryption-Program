import pytest
import security
from io import StringIO
s = security.Security()

#Caesar Encryptor Tests
@pytest.mark.set1
def test1_caesarEncryptor(monkeypatch):
    userInput = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert isinstance(s.CaesarEncryptor("abc"), str) 

@pytest.mark.set1
def test2_caesarEncryptor(monkeypatch):
    userInput = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert s.CaesarEncryptor("abc") != "abc"

#Caesar Decryptor Tests
@pytest.mark.set2
def test1_caesarDecryptor(monkeypatch):
    userInput = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert isinstance(s.CaesarDecryptor("abc"), str) 

@pytest.mark.set2
def test2_caesarDecryptor(monkeypatch):
    userInput = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert s.CaesarDecryptor("abc") != "abc"

#PolySub Encryptor Tests
@pytest.mark.set3
def test1_polysubEncryptor(monkeypatch):
    userInput = StringIO('test\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert isinstance(s.PolySubEncryptor("abc"), str) 

@pytest.mark.set3
def test2_polysubEncryptor(monkeypatch):
    userInput = StringIO('test\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert s.PolySubEncryptor("abc") != "abc"

#PolySub Decryptor Tests
@pytest.mark.set4
def test1_polysubDecryptor(monkeypatch):
    userInput = StringIO('test\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert isinstance(s.PolySubDecryptor("abc"), str) 

@pytest.mark.set4
def test2_polysubDecryptor(monkeypatch):
    userInput = StringIO('test\n')
    monkeypatch.setattr('sys.stdin', userInput)
    assert s.PolySubDecryptor("abc") != "abc"
