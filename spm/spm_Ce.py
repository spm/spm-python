from spm.__wrapper__ import Runtime


def spm_Ce(*args, **kwargs):
    """
      Error covariance constraints (for serially correlated data)  
        FORMAT [C] = spm_Ce(v,a)  
        FORMAT [C] = spm_Ce('ar',v,a)  
        v  - (1 x n) v(i) = number of observations for i-th block  
        a  - AR coefficient expansion point  [Default: a = []]  
          
        a  = [] (default) - block diagonal identity matrices specified by v:  
         
          C{i}  = blkdiag( zeros(v(1),v(1)),...,AR(0),...,zeros(v(end),v(end)))  
          AR(0) = eye(v(i),v(i))  
         
        otherwise:  
         
          C{i}     = AR(a) - a*dAR(a)/da;  
          C{i + 1} = AR(a) + a*dAR(a)/da;  
         
        FORMAT [C] = spm_Ce('fast',v,tr)  
        v  - (1 x n) v(i) = number of observations for i-th block  
        tr - repetition time  
         
        See also: spm_Q.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Ce.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Ce", *args, **kwargs)
