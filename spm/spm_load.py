from spm.__wrap__ import _Runtime


def spm_load(*args, **kwargs):
  """  Load text and numeric data from file  
    FORMAT x = spm_load(f,v,hdr)  
    f   - filename (can be gzipped) {txt,mat,csv,tsv,json,npy}  
    v   - name of field to return if data stored in a structure [default: '']  
          or index of column if data stored as an array  
    hdr - detect the presence of a header row for csv/tsv [default: true]  
     
    x   - corresponding data array or structure  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_load.m)
  """

  return _Runtime.call("spm_load", *args, **kwargs)
