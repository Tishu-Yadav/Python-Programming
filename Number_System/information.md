## Information

-repr('Tishu')
Purpose: Returns the “official” string representation of an object. This representation is mainly used for debugging and development. The goal is to be unambiguous.
Output: Includes details like escape characters or quotes, so it is clear what the object is.
 repr('Tishu')  # Output: "'Tishu'"

-str('Tishu')
Purpose: Returns the “informal” or nicely printable string representation of an object. The goal is to be readable.
Output: Simplified and user-friendly string representation.
 str('Tishu')  # Output: 'Tishu'

-print('Tishu')
Purpose: Displays the string to the console or standard output. It internally calls the str() representation of the object.
Output: Produces a clean output, suitable for the user.
 print('Tishu')  # Output: Tishu

# Key Points
 .Use repr() when you want to inspect an object, especially in a debugging or development context.
 .Use str() when you want a clean and readable string format.
 .Use print() to display content to the user.

# Libraries

- random , math , from decimal import Decimal , from fraction import Fraction , Numpy , copy , deepcopy

..Python Can Handle Large Numbers.

..Slicing Operator [:]

