from spm.__wrap__ import _Runtime, _MatlabClassWrapper


class nifti(_MatlabClassWrapper):
  def __init__(self, *args, _objdict=None, **kwargs):
    """  Create a NIFTI-1 object  
   __________________________________________________________________________  
    
      Documentation for nifti  
         doc nifti  
    
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/nifti.m)
    """

    if _objdict is None:
      _objdict = _Runtime.call("nifti", *args, **kwargs)
    super().__init__(_objdict)

  def cifti(self, *args, **kwargs):
    """  Extract CIFTI-2 extension from a NIfTI-2 file and export data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/cifti.m)
    """

    return _Runtime.call("cifti", self._as_matlab_object(), *args, **kwargs)


  def create(self, *args, **kwargs):
    """  Create a NIFTI-1 file  
    FORMAT create(obj)  
    Write out the header information for the nifti object  
     
    FORMAT create(obj,wrt)  
    Also write out an empty image volume if wrt==1  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/create.m)
    """

    return _Runtime.call("create", self._as_matlab_object(), *args, **kwargs)


  def disp(self, *args, **kwargs):
    """  Disp a NIFTI-1 object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/disp.m)
    """

    return _Runtime.call("disp", self._as_matlab_object(), *args, **kwargs)


  def display(self, *args, **kwargs):
    """  Display a NIFTI-1 object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/display.m)
    """

    return _Runtime.call("display", self._as_matlab_object(), *args, **kwargs)


  def fieldnames(self, *args, **kwargs):
    """  Fieldnames of a NIFTI-1 object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/fieldnames.m)
    """

    return _Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)


  def structn(self, *args, **kwargs):
    """  Convert a NIFTI-1 object into a form of struct  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/structn.m)
    """

    return _Runtime.call("structn", self._as_matlab_object(), *args, **kwargs)


  def subsasgn(self, *args, **kwargs):
    """  Subscript assignment  
    See subsref for meaning of fields.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/subsasgn.m)
    """

    return _Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)


  def subsref(self, *args, **kwargs):
    """  Subscript referencing  
     
    Fields are:  
    dat         - a file-array representing the image data  
    mat0        - a  9-parameter affine transform (from qform0)  
                  Note that the mapping is from voxels (where the first  
                  is considered to be at [1,1,1], to millimetres.  See  
                  mat0_interp for the meaning of the transform.  
    mat         - a 12-parameter affine transform (from sform0)  
                  Note that the mapping is from voxels (where the first  
                  is considered to be at [1,1,1], to millimetres.  See  
                  mat1_interp for the meaning of the transform.  
    mat_intent  - intention of mat.  This field may be missing/empty.  
    mat0_intent - intention of mat0. This field may be missing/empty.  
    intent      - interpretation of image. When present, this structure  
                  contains the fields  
                  code   - name of interpretation  
                  params - parameters needed to interpret the image  
    diminfo     - MR encoding of different dimensions.  This structure may  
                  contain some or all of the following fields  
                  frequency  - a value of 1-3 indicating frequency direction  
                  phase      - a value of 1-3 indicating phase direction  
                  slice      - a value of 1-3 indicating slice direction  
                  slice_time - only present when "slice" field is present.  
                               Contains the following fields  
                               code     - ascending/descending etc  
                               start    - starting slice number  
                               end      - ending slice number  
                               duration - duration of each slice acquisition  
                  Setting frequency, phase or slice to 0 will remove it.  
    timing      - timing information.  When present, contains the fields  
                  toffset - acquisition time of first volume (seconds)  
                  tspace  - time between successive volumes (seconds)  
    descrip     - a brief description of the image  
    cal         - a two-element vector containing cal_min and cal_max  
    aux_file    - name of an auxiliary file  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@nifti/subsref.m)
    """

    return _Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)


