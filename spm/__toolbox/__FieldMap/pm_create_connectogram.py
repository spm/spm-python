from spm._runtime import Runtime


def pm_create_connectogram(*args, **kwargs):
    """
      Create vectors corresponding to a connectogram based on label-map.  
        FORMAT [ii,jj,nn,pp] = pm_create_connectogram(rima,pm)  
        or  
        FORMAT [N,P] = pm_create_connectogram(rima,pm)  
         
        Input:  
        rima      : Label map consisting of connected regions indentified  
                    by unique labels.  
        pm        : Phasemap.  
         
        Output:  
        EITHER  
        ii        : Array of row indicies.  
        jj        : Array of column indicies.  
        nn        : Array of no. of voxels in borders between regions.  
                    So e.g. if ii[10]=5, jj[10]=9 and nn[10]=123 it  
                    means that regions 5 and 9 have a common border  
                    (are connected) and that this border has 123 voxels.  
        pp        : Array of sum of phase differences between regions.  
                    So e.g. if ii[10]=5, jj[10]=9 and pp[10]=770.2 it  
                    means that regions 5 and 9 have a common border  
                    (are connected) and that for paired voxels across  
                    this border the sum of phase differenes is 770.2.  
                    N.B. the subtraction is phi(ii(i))-phi(jj(i)),  
                    which in the example above means that the phase is  
                    smaller in region 9 than in region 5.  
         
        OR  
         
        N         : Sparse matrix where N(i,j) for i<j signify the number  
                    of voxels along the common border between regions labelled  
                    i and j in rima.  
                    and  
        P         : Sparse matrix where P(i,j) for i<j signify the sum of phase  
                    differences along the common border between regions labelled  
                    i and j in rima. Note that it is phi(i)-phi(j), i.e. the phase  
                    of the lower region number minus the phase of the higher  
                    region number.  
         
        This is a gateway function to pm_create_connectogram  
        (do the job) which is a mex-file. The job of this  
        routine is to create the sparse matrices from the  
        vectors returned by create_connectogram (because  
        the sparse format is a bit scary to handle in a mex-  
        file).  
         
        A very valid question would be "If you are going to return the  
        vectors ii, jj, nn and pp, why on earth do you go via the Matlab  
        sparse function?".  
        It's just because it allows us to write a very sloppy C-routine  
        to create the vectors, and then use Matlab sparse to identify  
        and remove any duplicate connections in there.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_create_connectogram.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pm_create_connectogram", *args, **kwargs)
