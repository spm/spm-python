from spm.__wrapper__ import Runtime


def _read_vtk_xml(*args, **kwargs):
  """  READ_VTK_XML reads a XML-formatted vtk file containing points in 3D and  
    connecting elements.  
     
    this function is a trial-and-error based implementation to read xml-style  
    vtk files. There is some documentation online, which seems somewhat  
    incomplete, or at least not fully understood by me.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_vtk_xml.m)
  """

  return Runtime.call("read_vtk_xml", *args, **kwargs)
