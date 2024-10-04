from spm.__wrap__ import _Runtime, _MatlabClassWrapper


class file_array(_MatlabClassWrapper):
  def __init__(self, *args, _objdict=None, **kwargs):
    """  Function for creating file_array objects.  
    FORMAT a = file_array(fname,dim,dtype,offset,scl_slope,scl_inter,permission)  
    a          - file_array object  
    fname      - filename  
    dim        - dimensions (default = [0 0] )  
    dtype      - datatype   (default = 'uint8-le')  
    offset     - offset into file (default = 0)  
    scl_slope  - scalefactor (default = 1)  
    scl_inter  - DC offset, such that dat = raw*scale + inter (default = 0)  
    permission - Write permission, either 'rw' or 'ro' (default = 'rw')  
   __________________________________________________________________________  
    
      Documentation for file_array  
         doc file_array  
    
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/file_array.m)
    """

    if _objdict is None:
      _objdict = _Runtime.call("file_array", *args, **kwargs)
    super().__init__(_objdict)

  def cat(self, *args, **kwargs):
    """  Concatenate file_array objects.  The result is a non-simple object  
    that can no longer be reshaped.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/cat.m)
    """

    return _Runtime.call("cat", self._as_matlab_object(), *args, **kwargs)


  def ctranspose(self, *args, **kwargs):
    """  Transposing not allowed  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/ctranspose.m)
    """

    return _Runtime.call("ctranspose", self._as_matlab_object(), *args, **kwargs)


  def disp(self, *args, **kwargs):
    """  Display a file_array object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/disp.m)
    """

    return _Runtime.call("disp", self._as_matlab_object(), *args, **kwargs)


  def display(self, *args, **kwargs):
    """  Display a file_array object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/display.m)
    """

    return _Runtime.call("display", self._as_matlab_object(), *args, **kwargs)


  def double(self, *args, **kwargs):
    """  Convert to double precision  
    FORMAT double(fa)  
    fa - a file_array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/double.m)
    """

    return _Runtime.call("double", self._as_matlab_object(), *args, **kwargs)


  def end(self, *args, **kwargs):
    """  Overloaded end function for file_array objects.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/end.m)
    """

    return _Runtime.call("end", self._as_matlab_object(), *args, **kwargs)


  def fieldnames(self, *args, **kwargs):
    """  Fieldnames of a file-array object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/fieldnames.m)
    """

    return _Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)


  def full(self, *args, **kwargs):
    """  Convert to numeric form  
    FORMAT full(fa)  
    fa - a file_array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/full.m)
    """

    return _Runtime.call("full", self._as_matlab_object(), *args, **kwargs)


  def horzcat(self, *args, **kwargs):
    """  Horizontal concatenation of file_array objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/horzcat.m)
    """

    return _Runtime.call("horzcat", self._as_matlab_object(), *args, **kwargs)


  def initialise(self, *args, **kwargs):
    """  Initialise file on disk  
     
    This creates a file on disk with the appropriate size by explicitly  
    writing data to prevent a sparse file.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/initialise.m)
    """

    return _Runtime.call("initialise", self._as_matlab_object(), *args, **kwargs)


  def isnan(self, *args, **kwargs):
    """  Logical array containing true where the elements of file_array are NaN's  
    FORMAT isnan(fa)  
    fa - a file_array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/isnan.m)
    """

    return _Runtime.call("isnan", self._as_matlab_object(), *args, **kwargs)


  def length(self, *args, **kwargs):
    """  Overloaded length function for file_array objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/length.m)
    """

    return _Runtime.call("length", self._as_matlab_object(), *args, **kwargs)


  def loadobj(self, *args, **kwargs):
    """  loadobj for file_array class  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/loadobj.m)
    """

    return _Runtime.call("loadobj", self._as_matlab_object(), *args, **kwargs)


  def ndims(self, *args, **kwargs):
    """  Number of dimensions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/ndims.m)
    """

    return _Runtime.call("ndims", self._as_matlab_object(), *args, **kwargs)


  def numel(self, *args, **kwargs):
    """  Number of simple file arrays involved.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/numel.m)
    """

    return _Runtime.call("numel", self._as_matlab_object(), *args, **kwargs)


  def numeric(self, *args, **kwargs):
    """  Convert to numeric form  
    FORMAT numeric(fa)  
    fa - a file_array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/numeric.m)
    """

    return _Runtime.call("numeric", self._as_matlab_object(), *args, **kwargs)


  def permute(self, *args, **kwargs):
    """  file_array objects can not be permuted  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/permute.m)
    """

    return _Runtime.call("permute", self._as_matlab_object(), *args, **kwargs)


  def reshape(self, *args, **kwargs):
    """  Overloaded reshape function for file_array objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/reshape.m)
    """

    return _Runtime.call("reshape", self._as_matlab_object(), *args, **kwargs)


  def size(self, *args, **kwargs):
    """  Method 'size' for file_array objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/size.m)
    """

    return _Runtime.call("size", self._as_matlab_object(), *args, **kwargs)


  def subsasgn(self, *args, **kwargs):
    """  Overloaded subsasgn function for file_array objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/subsasgn.m)
    """

    return _Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)


  def subsref(self, *args, **kwargs):
    """  SUBSREF Subscripted reference  
    An overloaded function...  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/subsref.m)
    """

    return _Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)


  def transpose(self, *args, **kwargs):
    """  file_array objects can not be transposed  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/transpose.m)
    """

    return _Runtime.call("transpose", self._as_matlab_object(), *args, **kwargs)


  def vertcat(self, *args, **kwargs):
    """  Vertical concatenation of file_array objects.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@file_array/vertcat.m)
    """

    return _Runtime.call("vertcat", self._as_matlab_object(), *args, **kwargs)


