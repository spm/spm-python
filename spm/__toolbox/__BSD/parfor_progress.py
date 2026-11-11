from spm._runtime import Runtime


def parfor_progress(*args, **kwargs):
    r"""
      from https://github.com/dumbmatter/parfor_progress/blob/master/parfor_progress.m  
       PARFOR_PROGRESS Progress monitor (progress bar) that works with parfor.  
          PARFOR_PROGRESS works by creating a file called parfor_progress.txt in  
          your working directory, and then keeping track of the parfor loop's  
          progress within that file. This workaround is necessary because parfor  
          workers cannot communicate with one another so there is no simple way  
          to know which iterations have finished and which haven't.  
         
          PARFOR_PROGRESS(N) initializes the progress monitor for a set of N  
          upcoming calculations.  
         
          PARFOR_PROGRESS updates the progress inside your parfor loop and  
          displays an updated progress bar.  
         
          PARFOR_PROGRESS(0) deletes parfor_progress.txt and finalizes progress  
          bar.  
         
          To suppress output from any of these functions, just ask for a return  
          variable from the function calls, like PERCENT = PARFOR_PROGRESS which  
          returns the percentage of completion.  
         
          Example:  
         
             N = 100;  
             parfor_progress(N);  
             parfor i=1:N  
                pause(rand); % Replace with real code  
                parfor_progress;  
             end  
             parfor_progress(0);  
         
          See also PARFOR.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/parfor_progress.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("parfor_progress", *args, **kwargs)
