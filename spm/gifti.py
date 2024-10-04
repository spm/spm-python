from spm.__wrap__ import _Runtime, _MatlabClassWrapper


class gifti(_MatlabClassWrapper):
  def __init__(self, *args, _objdict=None, **kwargs):
    """  GIfTI Geometry file format class  
    Geometry format under the Neuroimaging Informatics Technology Initiative  
    (NIfTI):  
                    http://www.nitrc.org/projects/gifti/  
                         http://nifti.nimh.nih.gov/  
   __________________________________________________________________________  
    
      Documentation for gifti  
         doc gifti  
    
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/gifti.m)
    """

    if _objdict is None:
      _objdict = _Runtime.call("gifti", *args, **kwargs)
    super().__init__(_objdict)

  def display(self, *args, **kwargs):
    """  Display method for GIfTI objects  
    FORMAT display(this)  
    this   -  GIfTI object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/display.m)
    """

    return _Runtime.call("display", self._as_matlab_object(), *args, **kwargs)


  def export(self, *args, **kwargs):
    """  Export a GIfTI object into specific MATLAB struct  
    FORMAT s = export(this,target)  
    this   - GIfTI object  
    target - string describing target output [default: MATLAB]  
    s      - a structure containing public fields of the object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/export.m)
    """

    return _Runtime.call("export", self._as_matlab_object(), *args, **kwargs)


  def fieldnames(self, *args, **kwargs):
    """  Fieldnames method for GIfTI objects  
    FORMAT names = fieldnames(this)  
    this   -  GIfTI object  
    names  -  field names  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/fieldnames.m)
    """

    return _Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)


  def isfield(self, *args, **kwargs):
    """  Isfield method for GIfTI objects  
    FORMAT tf = isfield(this,field)  
    this   -  GIfTI object  
    field  -  string of cell array  
    tf     -  logical array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/isfield.m)
    """

    return _Runtime.call("isfield", self._as_matlab_object(), *args, **kwargs)


  def plot(self, *args, **kwargs):
    """  plot method for GIfTI objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/plot.m)
    """

    return _Runtime.call("plot", self._as_matlab_object(), *args, **kwargs)


  def save(self, *args, **kwargs):
    """  Save GIfTI object in a GIfTI format file  
    FORMAT save(this,filename,encoding)  
    this      - GIfTI object  
    filename  - name of GIfTI file to be created [Default: 'untitled.gii']  
    encoding  - optional argument to specify encoding format, among  
                ASCII, Base64Binary, GZipBase64Binary, ExternalFileBinary.  
                [Default: 'GZipBase64Binary']  
    ordering  - optional argument to specify array element ordering, among  
                ColumnMajorOrder, RowMajorOrder  
                [Default: 'ColumnMajorOrder']  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/save.m)
    """

    return _Runtime.call("save", self._as_matlab_object(), *args, **kwargs)


  def saveas(self, *args, **kwargs):
    """  Save GIfTI object in external file format  
    FORMAT saveas(this,filename,format)  
    this      - GIfTI object  
    filename  - name of file to be created [Default: 'untitled.vtk']  
    format    - optional argument to specify encoding format, among  
                VTK (.vtk,.vtp), Collada (.dae), IDTF (.idtf), Wavefront OBJ  
                (.obj), JavaScript (.js), JSON (.json), FreeSurfer  
                (.surf,.curv), MZ3 (.mz3) [Default: VTK]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/saveas.m)
    """

    return _Runtime.call("saveas", self._as_matlab_object(), *args, **kwargs)


  def struct(self, *args, **kwargs):
    """  Struct method for GIfTI objects  
    FORMAT s = struct(this)  
    this   -  GIfTI object  
    s      -  a structure containing public fields of the object  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/struct.m)
    """

    return _Runtime.call("struct", self._as_matlab_object(), *args, **kwargs)


  def subsasgn(self, *args, **kwargs):
    """  Subscript assignment for GIfTI objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/subsasgn.m)
    """

    return _Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)


  def subsref(self, *args, **kwargs):
    """  Subscript referencing for GIfTI objects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@gifti/subsref.m)
    """

    return _Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)


