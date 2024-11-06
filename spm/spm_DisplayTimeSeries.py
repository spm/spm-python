from spm.__wrapper__ import Runtime


def spm_DisplayTimeSeries(*args, **kwargs):
    """
      Build a GUI for 'smart' time series display  
        FORMAT [ud] = spm_DisplayTimeSeries(y,options)  
        IN:  
          - y: the txn data, where t is the number of time sample, and p the  
               number of 'channels'  
          - options: a structure (default is empty), which allows to adapt this  
                     function to specific needs. Optional fields are:  
              .hp: the handle of the parent figure/object. This is used to  
              include the time series display in a panel/figure. By default, a  
              new figure will be created.  
              .Fsample: the sample rate of the data (in Hz)  
              .events: a nex1 structure vector containing the time indices of the  
              events and their type (if any). Default is empty. Basic structure  
              contains fields .time and .type (see below).  
              .M: a pxn matrix premultiplied to the data when plotted (default is  
              1).  
              .bad a px1 binary vector containing the good/bad status of the  
              channels. Default is zeros(p,1).  
              .transpose: a binary variable that transposes the data (useful for  
              file_array display). Using options.transpose = 1 is similar to do  
              something similar to plot(y'). Default is 0.  
              .minY: the min value of the plotted data (used to define the main  
              axes limit). Default is calculated according to the offset.  
              .maxY: the max value of the plotted data (used to define the main  
              axes limit). Default is calculated according to the offset.  
              .minSizeWindow: minimum size of the plotted window (in number of  
              time samples). {min([200,0.5*size(y,1)]}  
              .maxSizeWindow: maximum size of the plotted window (in number of  
              time samples). {min([5000,size(y,1)])}  
              .ds: an integer giving the number of displayed time samples when  
              dynamically moving the display time window. Default is 1e4. If you  
              set it to Inf, no downsampling is applied.  
              .callback: a string or function handle which is evaluated after  
              each release of the mouse button (when moving the patch or clicking  
              on the slider). Default is empty.  
              .tag: a string used to tag both axes  
              .pos1: a 4x1 vector containing the position of the main display  
              axes {[0.13 0.3 0.775 0.655]}  
              .pos2: a 4x1 vector containing the position of the global power  
              display axes {[0.13 0.05 0.775 0.15]}  
              .pos3: a 4x1 vector containing the position of the temporal slider  
              {[0.13 0.01 0.775 0.02]}  
              .itw: a vector containing the indices of data time samples  
              initially displayed in the main axes {1:minSizeWindow}  
              .ytick: the 'ytick' property of the main axes  
              .yticklabel: the 'yticklabel' property of the main axes  
              .offset: a px1 vector containing the vertical offset that has to be  
              added to each of the plotted time series  
              !! .ytick, .yticklabel and .offset can be used to display labelled  
              time series one above each other !!  
        OUT:  
          - ud: a structure containing all relevant information about the  
          graphical objects created for the GUI. This is useful for manipulating  
          the figure later on (see below).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DisplayTimeSeries.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DisplayTimeSeries", *args, **kwargs)
