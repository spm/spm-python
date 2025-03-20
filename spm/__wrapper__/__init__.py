from .runtime import Runtime
from .matlab_class import MatlabClass
from .matlab_function import MatlabFunction
from .cell import Cell
from .struct import Struct
from .array import Array
from .sparse_array import SparseArray


# ----------------------------------------------------------------------
# Questions
# ----------------------------------------------------------------------

# """
# * MATLAB does not have 1D arrays (they are always 2D).
#   A 1D python array is interpreted as a row arrays, so the round trip
#   goes [1, 2, 3] -> [[1, 2, 3]].
#   Are we happy with that? I think it works in the sense that
#   when a numpy operation takes a matrix and a vector, the vector is
#   broadcasted to its left, and is therefore interpreted as a row vector.

#   !! We should clearly document this behaviour.

# * The creation of numeric vectors on the python side is currently
#   quite verbose (`Array.from_any([0, 0])`, because `Array([0, 0])`
#   is interpreted as "create an empty array with shape [0, 0]").
#   We could either
#   - introduce a concise helper (e.g., `num`) to make this less verbose:
#     `Array.from_any([0, 0])` -> `num([0, 0])`
#   - Interpret lists of numbers as Arrays rather than Cells. But this is
#     problematic when parsing the output of a mpython_endpoint call, since
#     lists of numbers do mean "cell" in this context.

# * I've added support for "object arrays" (such as nifti or cfg_dep)
#   in DelayedArray:
#   > `a.b[0] = nifti("path")` means that `a.b` contains a 1x1 nifti object.
#   However, I only support 1x1 object, and the index must be 0 or -1.
#   There might be a way to make this more generic, but it needs more thinking.
#   The 1x1 case is all we need for batch jobs (it's required when building
#   jobs with dependencies).

#   It might be useful to have a `ObjectArray` type (with `MatlabClass`
#   as a base class?) for such objects -- It'll help with the logic in
#   delayed arrays. It should be detectable by looking for `class(struct(...))`
#   in the constructor when parsing the matlab code, although there are
#   cases where the struct is created beforehand, e.g.:
#   https://github.com/spm/spm/blob/main/%40nifti/nifti.m#L12

#   Maybe there's a programmatic way in matlab to detect if a class is
#   a pure object or an object array? It seems that old-school classes
#   that use the class(struct) constructor are always object arrays.
#   With new-style classes, object arrays can be constructed after the
#   fact:
#   https://uk.mathworks.com/help/matlab/matlab_oop/creating-object-arrays.html

#   After more thinking, it also means that we have again a difference in bhv
#   between `x{1} = object` and `x(1) = object`. In the former case, x is
#   a cell that contains an object, whereas in the latter x is a 1x1 object
#   array.

# * We should probably implement a helper to convert matlab batches into
#   python batches.
# """