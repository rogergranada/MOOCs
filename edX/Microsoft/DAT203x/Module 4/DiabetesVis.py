def azureml_main(frame1):
    import matplotlib
    matplotlib.use('agg')  
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import statsmodels.graphics.boxplots as sm

    Azure = True
    
## Create a series of bar plots for the various levels of the
## string columns in the data frame by readmi_class. 
    names = list(frame1)
    num_cols = frame1.shape[1]
    for indx in range(num_cols - 1):
        if(frame1.ix[:, indx].dtype not in [np.int64, np.int32, np.float64]):
            temp1 = frame1.ix[frame1.readmi_class == 'YES', indx].value_counts()
            temp0 = frame1.ix[frame1.readmi_class == 'NO', indx].value_counts() 
        
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            ax1 = fig.add_subplot(1, 2, 1)
            ax0 = fig.add_subplot(1, 2, 2) 
            temp1.plot(kind = 'bar', ax = ax1)
            ax1.set_title('Values of ' + names[indx] + '\n for readmitted patients')
            temp0.plot(kind = 'bar', ax = ax0)
            ax0.set_title('Values of ' + names[indx] + '\n for patients not readmitted')
            
            if(Azure == True): fig.savefig('bar_' + names[indx] + '.png')


## Now make some box plots of the columbns with numerical values.
    for indx in range(num_cols):
        if(frame1.ix[:, indx].dtype in [np.int64, np.int32, np.float64]):
            temp1 = frame1.ix[frame1.readmi_class == 'YES', indx]
            temp0 = frame1.ix[frame1.readmi_class == 'NO', indx]  
        
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            ax1 = fig.add_subplot(1, 2, 1)
            ax0 = fig.add_subplot(1, 2, 2) 
            ax1.boxplot(temp1.as_matrix())
            ax1.set_title('Box plot of ' + names[indx] + '\n for readmitted patients')
            ax0.boxplot(temp0.as_matrix())
            ax0.set_title('Box plot of ' + names[indx] + '\n for patients not readmitted')
            
            if(Azure == True): fig.savefig('box_' + names[indx] + '.png')
            
    return frame1
    