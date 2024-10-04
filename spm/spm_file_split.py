from spm.__wrap__ import _Runtime


def spm_file_split(*args, **kwargs):
  """  Convert a 4D volume file into a series of 3D volume files  
    FORMAT Vo = spm_file_split(V, odir)  
    V         - filename or spm_vol struct  
    odir      - output directory [default: same as input]  
     
    Vo        - spm_vol struct array of output files  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_file_split.m)
  """

  return _Runtime.call("spm_file_split", *args, **kwargs)
