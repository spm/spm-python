from spm.__wrap__ import _Runtime


def mne_write_label_file(*args, **kwargs):
  """   
    write_read_label_file(filename,label)  
      
    Writes label file. The returned structure has the following fields  
     
        filename      output file  
        label         a stucture containing the stc data with fields:  
     
        comment        comment for the first line of the label file  
        vertices       vertex indices (0 based, column 1)  
        pos            locations in meters (columns 2 - 4 divided by 1000)  
        values         values at the vertices (column 5)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_label_file.m)
  """

  return _Runtime.call("mne_write_label_file", *args, **kwargs, nargout=0)
