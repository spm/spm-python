from spm.__wrap__ import _Runtime


def pm_get_defaults(*args, **kwargs):
  """  FORMAT defval = pm_get_defaults(defstr)  
    Return the defaults value associated with identifier "defstr".  
    Currently, this is a '.' subscript reference into the global  
    "defaults" variable defined in spm_defaults.m.  
     
    FORMAT spm_get_defaults(defstr, defval)  
    Sets the defaults value associated with identifier "defstr". The new  
    defaults value applies immediately to:  
    * new modules in batch jobs  
    * modules in batch jobs that have not been saved yet  
    This value will not be saved for future sessions of SPM. To make  
    persistent changes, edit spm_defaults.m.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_get_defaults.m)
  """

  return _Runtime.call("pm_get_defaults", *args, **kwargs)
