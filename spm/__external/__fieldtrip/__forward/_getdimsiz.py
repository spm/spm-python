from spm.__wrapper__ import Runtime


def _getdimsiz(*args, **kwargs):
    """
      GETDIMSIZ  
         
        Use as  
          dimsiz = getdimsiz(data, field)  
        or  
          dimsiz = getdimsiz(data, field, numdim)  
         
        MATLAB will not return the size of a  field in the data structure that has trailing  
        singleton dimensions, since those are automatically squeezed out. With the optional  
        numdim parameter you can specify how many dimensions the data element has. This  
        will result in the trailing singleton dimensions being added to the output vector.  
         
        Example use  
          dimord = getdimord(datastructure, fieldname);  
          dimtok = tokenize(dimord, '_');  
          dimsiz = getdimsiz(datastructure, fieldname, numel(dimtok));  
         
        See also GETDIMORD, GETDATFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/getdimsiz.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getdimsiz", *args, **kwargs)
