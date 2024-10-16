from spm.__wrapper__ import Runtime


def _read_mat(*args, **kwargs):
  """  READ_MAT reads a matrix from an ascii or binary MBF format file  
     
     Usage: m         = loadmat('file');  
        or  [m,extra] = loadmat('file');  
       
     LOADMAT('file') returns the matrix stored in 'file' and  
     the extra information stored at the bottom of that file.  
     LOADMAT works for binary as well as asci matrix files.  
       
     See also WRITE_MAT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mat.m)
  """

  return Runtime.call("read_mat", *args, **kwargs)
