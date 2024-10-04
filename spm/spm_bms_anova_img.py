from spm.__wrap__ import _Runtime


def spm_bms_anova_img(*args, **kwargs):
  """  Log Bayes Factor against null for ANOVA; functional imaging data  
    FORMAT [P,g,prior] = spm_bms_anova_img(P,g,prior)  
     
    P         Cell array of filenames eg from SPM.xY.P with N cells  
    g         [N x 1] vector with entries 1,2,3 etc denoting group membership  
    prior     Specification of a single group is equivalent to a one sample t-test.  
              For this case you can specify 'unit' or 'jzs' (default) priors  
              See spm_bms_ttest.m and spm_bms_anova.m for more details  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_anova_img.m)
  """

  return _Runtime.call("spm_bms_anova_img", *args, **kwargs)
