from spm.__wrap__ import _Runtime


def spm_get_dataset(*args, **kwargs):
  """  Download a dataset from an online repository  
    FORMAT spm_get_dataset(repo, name, outdir)  
    repo   - name of repository, one of ['spm', 'openfmri']  
    name   - name of dataset, e.g. 'auditory' or 'ds000117'  
    rev    - revision of dataset [default: '']  
    outdir - output directory [default: pwd]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_get_dataset.m)
  """

  return _Runtime.call("spm_get_dataset", *args, **kwargs, nargout=0)
