# noqa: INP001

"""This module provides examples of various Python constructs with Google-style docstrings.

It includes examples of a function, a class with methods, an enum, a data class,
an abstract class, and a generator function.
"""

from abc import ABC, abstractmethod
from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum


def example_function(param1: int, param2: str) -> bool:
  """This function demonstrates a simple example of a function with parameters.

  Args:
      param1: The first parameter, an integer.
      param2: The second parameter, a string.

  Returns:
      bool: Returns True if param1 is positive, otherwise False.

  Raises:
      ValueError: If param1 is negative.
  """
  if not param2:
    error_message = 'param1 must be non-negative'
    raise ValueError(error_message)
  return param1 > 0


class ExampleEnum(Enum):
  """An example enum to represent some constant values."""

  VALUE_ONE = 1
  VALUE_TWO = 2
  VALUE_THREE = 3


@dataclass
class ExampleDataClass:
  """An example data class that holds data."""

  id: int
  name: str
  active: bool = True


class ExampleClass:
  """A class that demonstrates methods, read-only and read-write attributes."""

  def __init__(self, name: str, age: int) -> None:
    """Initializes the ExampleClass with a name and age.

    Args:
        name: The name of the person.
        age: The age of the person.

    Raises:
        ValueError: If age is negative.
    """
    if age < 0:
      error_message = 'Age cannot be negative'
      raise ValueError(error_message)
    self._name = name
    self._age = age
    self._read_write_attr = 'Default Value'

  @property
  def name(self) -> str:
    """str: The read-only name attribute."""
    return self._name

  @property
  def age(self) -> int:
    """int: The read-write age attribute."""
    return self._age

  @age.setter
  def age(self, value: int) -> None:
    """Sets the age attribute.

    Args:
        value: The new age value.

    Raises:
        ValueError: If the new age value is negative.
    """
    if value < 0:
      error_message = 'Age cannot be negative'
      raise ValueError(error_message)
    self._age = value

  @property
  def read_write_attr(self) -> str:
    """str: A read-write attribute."""
    return self._read_write_attr

  @read_write_attr.setter
  def read_write_attr(self, value: str) -> None:
    """Sets the read-write attribute.

    Args:
        value: The new value for the attribute.
    """
    self._read_write_attr = value

  def greet(self) -> str:
    """Generates a greeting string.

    Returns:
        str: A greeting message that includes the name and age.
    """
    return f'Hello, my name is {self.name} and I am {self.age} years old.'


def example_generator(n: int) -> Generator[int, None, None]:
  """A generator function that yields numbers from 0 to n-1.

  Args:
      n: The upper limit for generating numbers (exclusive).

  Yields:
      int: The next number in the sequence.
  """
  yield from range(n)


class AbstractExample(ABC):
  """An abstract class that defines a template for subclasses."""

  @abstractmethod
  def do_something(self) -> str:
    """Abstract method that must be implemented by subclasses.

    Returns:
        str: A description of the action performed.
    """


class ConcreteExample(AbstractExample):
  """A concrete implementation of the AbstractExample class."""

  def do_something(self) -> str:
    """Performs a specific action.

    Returns:
        str: A description of the action performed.
    """
    return 'Doing something concrete!'
