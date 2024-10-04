from spm.__wrap__ import _Runtime


def ft_sourcemovie(*args, **kwargs):
  """  FT_SOURCEMOVIE displays the source reconstruction on a cortical mesh  
    and allows the user to scroll through time with a movie.  
     
    Use as  
      ft_sourcemovie(cfg, source)  
    where the input source data is obtained from FT_SOURCEANALYSIS, or a  
    a parcellated source structure (i.e. contains a brainordinate field) and  
    cfg is a configuration structure that should contain  
     
      cfg.funparameter    = string, functional parameter that is color coded (default = 'avg.pow')  
      cfg.maskparameter   = string, functional parameter that is used for opacity (default = [])  
     
    To facilitate data-handling and distributed computing you can use  
      cfg.inputfile   =  ...  
    If you specify this option the input data will be read from a *.mat  
    file on disk. This mat files should contain only a single variable named 'data',  
    corresponding to the input structure.  
     
    See also FT_SOURCEPLOT, FT_SOURCEINTERPOLATE, FT_SOURCEPARCELLATE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourcemovie.m)
  """

  return _Runtime.call("ft_sourcemovie", *args, **kwargs)
